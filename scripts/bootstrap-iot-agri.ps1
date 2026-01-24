param(
  [switch]$SkipNode
)

$ErrorActionPreference = "Stop"

Write-Host "==> Creando venv en .venv"
python -m venv .venv

Write-Host "==> Activando venv"
& .\.venv\Scripts\Activate.ps1

Write-Host "==> Instalando uv"
pip install uv

Write-Host "==> Instalando deps API"
uv pip install -r apps/iot-agri/api/requirements.txt

Write-Host "==> Instalando deps scripts"
uv pip install -r apps/iot-agri/requirements-dev.txt

if (-not $SkipNode) {
  Write-Host "==> Instalando deps web"
  Push-Location apps/iot-agri/web
  npm install
  Pop-Location
}

Write-Host "==> Bootstrap OK"
