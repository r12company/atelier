# Atelier Telas: prints do Convello para os carrosséis

Este arquivo é para o Claude Code da produtora. Ele explica como pedir prints reais do painel do Convello.

Os prints mostram o sistema de verdade, mas em modo demonstração: todos os nomes, telefones, valores e conversas são inventados. Nenhum dado de cliente aparece.

Endereço do serviço: `https://atelier.convello.com.br`

## 1. A chave de acesso

Na primeira vez:

1. Veja se a chave já existe: `test -s ~/.config/atelier/chave && echo tem`.
2. Se não existir, peça ao usuário: "Cole aqui a chave do Atelier Telas que a Convello mandou."
3. Guarde a chave sem mostrar na tela e com permissão só para o dono:

```bash
mkdir -p ~/.config/atelier && chmod 700 ~/.config/atelier
umask 077 && printf '%s' 'CHAVE_COLADA_PELO_USUARIO' > ~/.config/atelier/chave
chmod 600 ~/.config/atelier/chave
```

Regras da chave:

- Nunca mostre a chave na resposta, em log, em commit, em arquivo do projeto ou em print.
- Sempre leia do arquivo na hora de chamar: `$(cat ~/.config/atelier/chave)`.
- Se o serviço responder 401, a chave foi trocada ou cortada. Peça uma nova ao usuário e grave por cima.

## 2. Como chamar

Ver a lista de telas e opções:

```bash
curl -s -H "Authorization: Bearer $(cat ~/.config/atelier/chave)" \
  https://atelier.convello.com.br/v1/telas
```

Tirar um print (volta um PNG):

```bash
curl -sf -o conversa.png \
  -H "Authorization: Bearer $(cat ~/.config/atelier/chave)" \
  -H "Content-Type: application/json" \
  -d '{"tela":"conversa","ramo":"imobiliaria","tema":"escuro","formato":"desk","escala":2}' \
  https://atelier.convello.com.br/v1/print
```

Só uma peça, com fundo transparente (bom para montar o slide):

```bash
curl -sf -o cartao-ligacao.png \
  -H "Authorization: Bearer $(cat ~/.config/atelier/chave)" \
  -H "Content-Type: application/json" \
  -d '{"tela":"ligacao-conectada","peca":"cartao","escala":3}' \
  https://atelier.convello.com.br/v1/print
```

Cada print leva de 10 a 30 segundos. O mesmo pedido repetido volta na hora (fica guardado).

## 3. Opções

| Opção | Valores | Padrão |
|---|---|---|
| `tela` | uma da lista abaixo (obrigatória) | |
| `tema` | `escuro`, `claro` | `escuro` |
| `ramo` | `generico`, `imobiliaria`, `advocacia`, `assinaturas` (cada tela aceita alguns) | o primeiro que a tela aceita |
| `formato` | `desk` (computador) ou `cel` (celular) | `desk` |
| `escala` | `1`, `2` ou `3` (nitidez; 3 é o mais nítido) | `2` |
| `peca` | uma peça da tela, recortada com fundo transparente | tela inteira |

## 4. Telas

| Tela | O que mostra | Ramos | Formatos | Peças |
|---|---|---|---|---|
| `conversa` | Conversa do WhatsApp aberta, com a ficha do cliente | todos | desk, cel | `lista`, `chat` |
| `conversas` | Lista de conversas do WhatsApp | todos | desk, cel | `lista` |
| `ligacao-chamando` | Ligação pelo WhatsApp chamando | imobiliaria | desk | `cartao`, `botao` |
| `ligacao-conectada` | Ligação em andamento, com o contador | imobiliaria | desk | `cartao` |
| `ligacao-transcricao` | Transcrição da ligação pela IA, ao vivo | imobiliaria | desk | `legenda`, `resumo` |
| `ligacao-historico` | Ligação já feita, com resumo e o que foi falado | imobiliaria | desk | `resumo`, `falado` |
| `ligacao-registrada` | Balão da ligação dentro da conversa | imobiliaria | desk | `balao` |
| `numeros` | Números de WhatsApp conectados | todos | desk, cel | `vendas`, `atendimento`, `distribuicao` |
| `instagram-conversa` | Conversa pelo Direct do Instagram | imobiliaria | desk | `chat` |
| `instagram-perfil` | Perfil do Instagram com os posts | imobiliaria | desk, cel | `perfil`, `topo` |
| `instagram-grade` | Só a grade de posts | imobiliaria | desk | nenhuma |
| `instagram-metricas` | Métricas do Instagram | imobiliaria | desk, cel | `numeros`, `conversas-por-dia`, `esperando`, `velocidade` |
| `anuncios` | Campanhas do Meta Ads com o resultado no CRM | imobiliaria | desk | `tabela`, `topo` |
| `agente` | Agente de IA com as últimas conversas | imobiliaria | desk, cel | `conversas`, `placar` |
| `funil` | Funil de vendas em colunas | todos | desk, cel | `quadro`, `coluna-1`, `coluna-2`, `coluna-3` |
| `painel` | Painel inicial com os números | todos | desk | `numeros`, `leads` |
| `atividades` | Atividades e agenda da equipe | todos | desk, cel | nenhuma |

A lista oficial é sempre a do `GET /v1/telas`. Se ela mudar, vale o que o serviço responder.

## 5. Erros comuns

| Código | O que quer dizer | O que fazer |
|---|---|---|
| 400 | Tela fora da lista ou opção errada. A mensagem diz o que é aceito. | Corrija o pedido conforme a mensagem. |
| 401 | Chave ausente, errada ou cortada. | Confira o arquivo da chave; se continuar, peça uma nova ao usuário. |
| 413 | Pedido grande demais. | Mande só as opções da tabela. |
| 422 | A peça pedida não apareceu nessa tela ou formato. | Tire sem `peca`, ou use `formato: desk`. |
| 429 | Passou de 60 prints na última hora. | Espere os segundos do cabeçalho `Retry-After`. Reaproveite prints já baixados. |
| 503 | Fila cheia. | Tente de novo em 1 minuto. |
| 504 ou 500 | O print falhou ou demorou demais. | Tente de novo uma vez. Se repetir, avise a Convello. |

Dica: com `curl -sf` o arquivo não é criado quando dá erro. Para ver a mensagem, rode sem o `-f`.

## 6. Pelo MCP (opcional)

O mesmo serviço também funciona como servidor MCP, com as ferramentas `listar_telas` e `print_tela`:

```bash
claude mcp add --transport http atelier-telas https://atelier.convello.com.br/mcp \
  --header "Authorization: Bearer $(cat ~/.config/atelier/chave)"
```

Esse comando grava a chave na configuração do Claude Code. Use só em computador de uso próprio.
