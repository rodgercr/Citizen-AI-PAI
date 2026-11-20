@echo off
cd /d "%~dp0"
set "PAI_PY=%~dp0..\..\work\pai_env\Scripts\python.exe"
if not exist "%PAI_PY%" (
  if not exist ".venv\Scripts\python.exe" py -3.11 -m venv .venv
  set "PAI_PY=%~dp0.venv\Scripts\python.exe"
)
"%PAI_PY%" -X utf8 iniciar_local.py
pause
