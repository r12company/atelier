# Instalador do Atelier para o Claude Code (Windows, PowerShell).
#
#   irm https://raw.githubusercontent.com/r12company/atelier/main/scripts/instalar.ps1 | iex
#
# Só uma skill: baixe o arquivo e rode   .\instalar.ps1 carrossel-r12
# Teste com uma cópia local:            $env:ORIGEM = "C:\caminho\do\repositorio"; .\instalar.ps1
#
# O que faz: baixa a versão mais nova do repositório, copia as skills para %USERPROFILE%\.claude\skills\ (a versão
# que já existia fica guardada como <nome>.antiga) e roda o checar.py para dizer o que ainda falta.
# Pode rodar quantas vezes quiser.
param([string[]]$Skills = @('carrossel-convello', 'carrossel-r12'))
$ErrorActionPreference = 'Stop'
$Repo = 'r12company/atelier'
$Destino = Join-Path $env:USERPROFILE '.claude\skills'
$Tmp = Join-Path ([System.IO.Path]::GetTempPath()) ("atelier-" + [guid]::NewGuid())
New-Item -ItemType Directory -Path $Tmp | Out-Null

try {
    # 1. Baixar o repositório
    if ($env:ORIGEM) {
        $Fonte = $env:ORIGEM
        Write-Host "Usando a cópia local em $Fonte"
    } elseif (Get-Command git -ErrorAction SilentlyContinue) {
        Write-Host 'Baixando o Atelier (git)...'
        git clone -q --depth 1 "https://github.com/$Repo.git" (Join-Path $Tmp 'atelier')
        $Fonte = Join-Path $Tmp 'atelier'
    } else {
        Write-Host 'Baixando o Atelier (sem git, pelo arquivo do GitHub)...'
        $Zip = Join-Path $Tmp 'atelier.zip'
        Invoke-WebRequest -UseBasicParsing "https://github.com/$Repo/archive/refs/heads/main.zip" -OutFile $Zip
        Expand-Archive $Zip -DestinationPath $Tmp
        $Fonte = (Get-ChildItem $Tmp -Directory | Select-Object -First 1).FullName
    }

    # 2. Copiar as skills
    New-Item -ItemType Directory -Force -Path $Destino | Out-Null
    foreach ($Nome in $Skills) {
        $Origem = Join-Path $Fonte "plugins\$Nome\skills\$Nome"
        if (-not (Test-Path (Join-Path $Origem 'SKILL.md'))) {
            throw "Não existe a skill `"$Nome`". As que existem: carrossel-convello, carrossel-r12."
        }
        $Alvo = Join-Path $Destino $Nome
        if (Test-Path $Alvo) {
            $Antiga = "$Alvo.antiga"
            if (Test-Path $Antiga) { Remove-Item -Recurse -Force $Antiga }
            Move-Item $Alvo $Antiga
            Write-Host "Já existia a skill ${Nome}: a versão anterior ficou guardada em $Antiga"
        }
        Copy-Item -Recurse $Origem $Alvo
        Write-Host "Skill $Nome instalada em $Alvo"
    }
    $Skill = Join-Path $Destino $Skills[0]

    # 3. O que falta para montar
    Write-Host ''
    if (-not (Get-Command photocraft-cli -ErrorAction SilentlyContinue)) {
        Write-Host 'PhotoCraft (o programa que o Atelier usa para montar): baixe o ...-windows-x64-portable.zip em'
        Write-Host '  https://github.com/storytold/photocraft/releases, descompacte e ponha a pasta no PATH (tem o photocraft-cli.exe).'
    }
    Write-Host "Fontes: abra a pasta $Skill\fontes, clique duas vezes em cada .ttf e em Instalar."
    Write-Host 'No Windows a montagem automática funciona melhor dentro do WSL (Ubuntu): lá rode o instalador de Linux.'
    Write-Host 'Sem montagem, as skills fazem roteiro, legenda e pedidos de imagem, e a montagem vai pelo caminho B (Photoshop ou Figma).'
    $Py = Get-Command python -ErrorAction SilentlyContinue
    if (-not $Py) { $Py = Get-Command py -ErrorAction SilentlyContinue }
    if ($Py) {
        Write-Host ''
        & $Py.Source (Join-Path $Skill 'motor\checar.py')
    } else {
        Write-Host 'Falta o Python 3 (python.org, marque "Add python.exe to PATH" na instalação).'
    }
    Write-Host ''
    Write-Host 'Pronto. Abra o Claude Code e peça, por exemplo: faz um carrossel do Convello sobre <o tema>.'
} finally {
    Remove-Item -Recurse -Force $Tmp -ErrorAction SilentlyContinue
}
