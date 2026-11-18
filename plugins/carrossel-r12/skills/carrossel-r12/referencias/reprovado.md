# O que o dono da marca reprovou, e o que vale

Cada linha custou uma versão refeita (a maioria no carrossel irmão do Convello, em 15/11/2026, e vale igual aqui; as da R12 vieram na proposta de SEO, em 16/11/2026). Leia antes de desenhar uma peça nova e antes de mandar qualquer coisa.
A coluna "Quem garante" diz se o motor já impede (motor) ou se depende de você (você).

## Material

| Reprovado | O que vale | Quem garante |
| --- | --- | --- |
| Print antigo de site ou campanha que já mudou | Print novo, da versão no ar (`material.md`, item 1) | você |
| Print de cliente sem autorização, ou com nome, telefone ou valor que ele não liberou | Autorização anotada no `copy.md` da peça; o resto vira desenho genérico | você |
| Tela inventada fingindo ser trabalho da R12, número de resultado inventado | Só trabalho real e número que quem pediu passou | você |
| Print com erro na tela, página em branco ou aviso de cookie cobrindo | Olhar cada print antes de usar | você |
| Montagem em página HTML | PhotoCraft, pelo `montar.py`: sai PSD com camadas | motor (o `conferir.py` exige o PSD) |
| Rosto que muda entre a capa e o final do mesmo carrossel | A mesma pessoa nos dois, com a capa de referência | você |
| O mesmo homem e os mesmos elementos de um carrossel para o outro | Personagem, pose, posição, objetos e peças novos a cada carrossel. Só a planta se repete | você |
| Rosto de pessoa real feito por IA | Foto de verdade, com licença livre e crédito | você |
| Pele alaranjada, luz quente | Pele clara e natural (o bloco 4 de `modelos-de-prompt/pessoa.md` já pede) | você, olhando a imagem |
| Recorte da foto do Gemini levando a parede junto | `alisar.py` e a `<foto>-lisa.png`: o motor recorta pela máscara e dá erro se ela cobre mais de 70% da foto | motor |
| Logo em cima do cabelo | A pessoa não toca a caixa da logo | motor (dá erro) |

## Roteiro e texto

| Reprovado | O que vale | Quem garante |
| --- | --- | --- |
| Roteiro escrito sem quem pediu ver, montado direto | Roteiro de quem pediu, ou roteiro mostrado em texto antes de montar | você |
| Travessão em qualquer lugar | Dois-pontos, vírgula ou ponto | motor |
| Emoji, dado inventado, concorrente citado, cliente citado sem autorização | Ver `copy.md` | motor (emoji) e você |
| Quebra de linha feia, palavra sozinha na linha | Quebra escolhida à mão | motor (texto de apoio) e você (título) |
| Texto grudado em outra peça | Respiros da régua (24, 40, 48, 64, 80) | você, com a régua |
| Slide cheio de texto: nota, ressalva, rótulo e cartão empilhados ("vai poluir e ficar difícil de ler") | Título grande, uma imagem, o fio; apoio só quando indispensável (`copy.md`, seção 3) | motor avisa (`conferir.py`) e você |
| Mudar frase de roteiro aprovado no redesenho | Roteiro travado: o redesenho muda só a arte | você |
| Legenda longa, de 2.000 caracteres | Legenda curta com cara de post, emoji quando ajuda (exemplo em `copy.md`, seção 5) | motor avisa e você |
| Título gigante em todo slide, "cara de site" | Título das páginas em Oswald 82 a 92. Palavra gigante (até 256) só na capa e no final | motor |
| Fonte "com cara de site" (Sora), Fira Sans, Anton | Oswald no título e na palavra de impacto, IBM Plex Sans no texto | motor |
| Espaçamento exagerado entre as letras ("E S P A Ç A M E N T O"), em selo, chamada ou rótulo | Espaçamento normal (0); só o aperto leve da linha pequena da capa (-10) | motor |

## Visual

| Reprovado | O que vale | Quem garante |
| --- | --- | --- |
| Brilho espalhado (glow), "poluído" | Fundo limpo: degradê leve com grão | motor |
| Fundo de cor forte com frase grande centralizada; foto ocupando o slide de conteúdo com texto por cima ("poluído, nem parece slide, parece site") | O estilo da proposta de SEO, com combinações novas de molde, ritmo e capa (`moldes.md`) | motor |
| Fundo verde-água ou o fundo de ondas do manual da marca ("poluído") | Claro quase branco e escuro `#161616` com toque de verde | motor |
| Todos os carrosséis com o mesmo layout, a mesma ordem de texto e a mesma capa | Direção de arte própria por carrossel, capa diferente, 3+ moldes nos slides do meio | você |
| Capa ou final com a foto inteira escurecida, ou escurecida em faixas que deixam listra na parede ("poluído, essa sombra") | Degradê único e liso, só onde vai o título (`escurecer='baixo'` ou `'cima'`) | você |
| Capa com elementos novos (palavra em tarja, palavra escura atrás da pessoa, enfeite) | Capa limpa igual à da proposta de SEO; só muda onde o título, a pessoa e o objeto ficam | você |
| Todos os personagens das capas na mesma pose, segurando celular | Cada capa com outra pose e outro gesto ligado ao assunto (notebook, balcão da loja, apontando para cima, braços cruzados) | você |
| Fundo chapado, "cru" | Degradê leve com grão, no claro e no escuro | motor |
| Verde `#95db30` como letra no fundo claro (não dá leitura) | Verde de leitura `#3f7a0f` no claro | motor |
| Slides todos do mesmo fundo | Capa, claro, escuro, claro, escuro... final | motor |
| Escuro em cima de escuro, claro em cima de claro | Fundo claro com peça escura, fundo escuro com peça clara ou verde | você |
| Contador de slide (2/9) | Nada. O fio já mostra que continua | você |
| Numeração (01, 02, bolinha 1 2 3) | Ícone 3D ou ícone de traço grande no lugar do número | você |
| Cartão, selo ou bolinha por cima de foto ou de print | Nada por cima. Rótulo de fora, com linha fina | você |
| Logo só com o símbolo, logo pequena | Logo completa (símbolo R12 e "company") no topo | motor |
| Caixa ou faixa branca atrás da logo ("pqp"), faixa escura no topo | Logo direto no fundo | motor |
| Logo com contorno branco ("podre") | A logo dos arquivos de `marca/`, sem contorno: a escura no claro, a de "company" claro no escuro | motor |
| Botão em aba no rodapé (cópia de outra agência) | O fio | motor |
| Ícone pequeno boiando na frente da pessoa | Objeto 3D grande atrás dela, meio escondido | você, com `atras=` |
| Ícone "tapado" atrás da lista, na emenda | A peça que atravessa fica por cima | você |
| Tracinho claro na borda do ícone recortado | `objeto()` já come a franja antes de aparar | motor |
| Pessoa pequena, objeto fora do quadro | Rosto grande (400 a 600 px) e o que ela olha aparecendo acima do título | motor, com as medidas certas |
| Final diferente da capa | O mesmo desenho: pessoa, linha, palavra gigante e, no rodapé, a chamada | motor |

## Jeito de trabalhar

| Reprovado | O que vale |
| --- | --- |
| Demora sem mostrar nada ("Q demora") | Mandar a capa assim que ficar pronta, depois o resto |
| "Aqui está" com imagem só no terminal | O terminal não mostra imagem para quem pediu: diga o caminho de cada arquivo para abrir (ou envie pelo jeito que a sua ferramenta tiver) |
| Perguntar gosto em texto | Montar 3 ou 4 opções numa imagem só: quem pediu escolhe riscando |
| Trocar a foto quando pediram só luz melhor | Mexer só no que foi pedido |
| Demora com vários carrosséis em fila | Um agente por carrossel, vários carrosséis em paralelo; montagem uma de cada vez (trava `flock`) |
