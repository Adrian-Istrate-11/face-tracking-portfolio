@echo off
set PROJECT_DIR=D:\Academia Nenos curs Python Developer\Proiect final Academie Nenos Python\nenos_face_tracking_repo

start "API"  cmd /k ^
  "cd /d \"%PROJECT_DIR%\" ^&^& call .venv\Scripts\activate.bat ^&^& set PYTHONPATH=src ^&^& uvicorn api.main:app --host 127.0.0.1 --port 8080 --reload"

start "DASH" cmd /k ^
  "cd /d \"%PROJECT_DIR%\" ^&^& call .venv\Scripts\activate.bat ^&^& set PYTHONPATH=src ^&^& python -m src.web.main"

timeout /t 5 >nul
start http://127.0.0.1:8080/docs
start http://127.0.0.1:8050
