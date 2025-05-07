# 1. Navighează în folderul proiectului
cd D:\Academia Nenos curs Python Developer\Proiect final Academie Nenos Python\nenos_face_tracking_repo

# 2. Activează mediul virtual (dacă nu e deja activat)
.venv\Scripts\activate

# 3. Setează PYTHONPATH (pentru ca importurile relative să meargă)
$env:PYTHONPATH = "src"

# 4. Rulează aplicația
uvicorn api.main:app --reload

# 5. Deschide browserul la:
# http://127.0.0.1:8000/docs
