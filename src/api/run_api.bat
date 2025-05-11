@echo off
REM Ne mutăm în rădăcina repo-ului
pushd "%~dp0\..\.."

REM Activăm virtualenv-ul
call .venv\Scripts\activate.bat

REM Adăugăm src în PYTHONPATH
set PYTHONPATH=%CD%\src

REM Pornim API-ul
start "API Server" cmd /c "uvicorn src.api.main:app --host 127.0.0.1 --port 8080 --reload"

REM Dăm un mic delay
timeout /t 2 >nul

REM Deschidem browser-ul automat la Swagger UI
start http://127.0.0.1:8080/docs

popd
pause
