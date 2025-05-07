@echo off
:: ----  CONFIG -----------------------------------------------------
set PROJECT_DIR=D:\Academia Nenos curs Python Developer\Proiect final Academie Nenos Python\nenos_face_tracking_repo
set PYTHONPATH=src
set DASH_HOST=127.0.0.1
set DASH_PORT=8050
:: -----------------------------------------------------------------

pushd "%PROJECT_DIR%"
call ".venv\Scripts\activate.bat"
set PYTHONPATH=%PYTHONPATH%
echo Starting Dash on http://%DASH_HOST%:%DASH_PORT% ...
python -m src.web.main
popd
