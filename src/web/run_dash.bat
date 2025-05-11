@echo off
pushd "%~dp0\..\.."

call .venv\Scripts\activate.bat
set PYTHONPATH=%CD%\src

start "Dash App" cmd /c "python src/web/main.py"

timeout /t 2 >nul
start http://127.0.0.1:8050

popd
pause
