@echo off
:: ----  CONFIG  ---------------------------------------------------
set PROJECT_DIR=D:\Academia Nenos curs Python Developer\Proiect final Academie Nenos Python\nenos_face_tracking_repo
set PYTHONPATH=src
set HOST=127.0.0.1
set PORT=8080
:: -----------------------------------------------------------------

pushd "%PROJECT_DIR%"
call ".venv\Scripts\activate.bat"
set PYTHONPATH=%PYTHONPATH%
echo Starting API on http://%HOST%:%PORT% ...
uvicorn api.main:app --host %HOST% --port %PORT% --reload
popd
