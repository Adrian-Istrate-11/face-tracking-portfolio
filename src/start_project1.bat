@echo off
cd nenos_face_tracking_repo
set PYTHONPATH=src
uvicorn api.main:app --reload
start http://127.0.0.1:8000/docs
