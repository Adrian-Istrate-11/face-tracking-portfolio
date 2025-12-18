# Versiunea Adrian (Python 3.12) – GET & DELETE implementate

> **Autor**: Adrian Istrate  
> **Compatibilitate**: Testat pe Windows cu Python 3.12  
> **Stare**: Separat de `main`

##  Funcționalități implementate
-  Adăugare angajați (`PUT /employees`)
-  Afișare toți angajații (`GET /employees`)
-  Ștergere angajat după ID (`DELETE /employees/{id}`)

##  Fișiere modificate
Toate modificările au fost făcute pas cu pas, doar în logica pentru „employee”:

| Fișier                                      | Cale                                      | Tip modificare |
|--------------------------------------------|-------------------------------------------|----------------|
| `employees.py`                             | `src/api/routers/`                        | Adăugat `GET`, `DELETE` |
| `employees.py`                             | `src/common/data_transfer_objects/`       | Adăugat `EmployeeDto` |
| `employees.py`                             | `src/db/sql/models/`                      | Adăugat `extend_existing=True` |
| `employees.py`                             | `src/db/sql/queries/`                     | Adăugat funcții `get_all_employees_from_db` și `delete_employee_by_id` |

##  Cum se testează
1. Pornește serverul local cu:
   ```bash
   uvicorn api.main:app --reload
   ```

2. Accesează documentația:
   ```http
   http://127.0.0.1:8000/docs
   ```

3. Testează cele 3 funcții:
   - `PUT /employees` – adaugă angajat
   - `GET /employees` – returnează lista angajaților
   - `DELETE /employees/{id}` – șterge un angajat după ID

