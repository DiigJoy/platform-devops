param()

$ErrorActionPreference = "Stop"

Write-Host "==> Creando venv en .venv"
python -m venv .venv

Write-Host "==> Activando venv"
& .\.venv\Scripts\Activate.ps1

Write-Host "==> Instalando uv"
pip install uv

Write-Host "==> Instalando pre-commit"
uv pip install pre-commit
pre-commit install

Write-Host "==> Bootstrap global OK"
Write-Host "==> Siguiente: .\\scripts\\bootstrap-iot-agri.ps1"
