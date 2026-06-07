# Script de configuração inicial do ambiente (Windows)
Write-Host "Configurando o ambiente de testes E2E..." -ForegroundColor Cyan

# 1. Criação do Ambiente Virtual
Write-Host "1. Criando virtual environment (.venv)..." -ForegroundColor Yellow
python -m venv .venv

# 2. Ativação do ambiente
Write-Host "2. Ativando .venv..." -ForegroundColor Yellow
$venvPath = ".\.venv\Scripts\Activate.ps1"
if (Test-Path $venvPath) {
    & $venvPath
} else {
    Write-Host "Erro ao ativar o ambiente virtual." -ForegroundColor Red
    exit
}

# 3. Instalação das dependências
Write-Host "3. Instalando dependências do requirements.txt..." -ForegroundColor Yellow
python -m pip install --upgrade pip
pip install -r requirements.txt

# 4. Instalação do navegador do Playwright
Write-Host "4. Instalando drivers do Playwright (Chromium)..." -ForegroundColor Yellow
playwright install chromium

Write-Host "=============" -ForegroundColor Green
Write-Host "✅ Ambiente configurado com sucesso!" -ForegroundColor Green
Write-Host "Para rodar os testes, use o comando: pytest" -ForegroundColor White
