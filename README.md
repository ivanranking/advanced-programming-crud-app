# AP Capstone – Facilities Module (Weeks 1–2)

This repo contains a complete Django implementation of the **Facilities** module:
- CRUD (list, detail, create, edit, delete)
- Search & filter (by type, partner, location, capability) + free-text search
- Sort and paginate
- Bootstrap UI
- Basic unit tests

## Quickstart

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt

python manage.py migrate
python manage.py runserver
```

Open http://127.0.0.1:8000/ to view the Facilities list.

## Create superuser (optional, for admin)
```bash
python manage.py createsuperuser
```

## Project Structure

- `facilities/models.py` – `Facility` model aligned with the capstone spec
- `facilities/forms.py` – create/update form with capability normalization
- `facilities/views.py` – class-based views with messages & pagination
- `facilities/filters.py` – search & filter helper
- `facilities/templates/facilities/` – Bootstrap templates
- `facilities/tests.py` – smoke tests for CRUD & filtering
- `ap_capstone/settings.py` – SQLite config

## Notes for Week 2 Safeguards
When you add Projects/Services/Equipment, override `FacilityDeleteView.delete()` to block deletion if related records exist.

## Evaluator Mapping (ASP.NET MVC / CodeIgniter)
- **Model** ↔ `models.py` (`Facility`)
- **Controller** ↔ class-based views (`List/Detail/Create/Update/Delete`)
- **View** ↔ Django templates (similar to Razor/CI views)
- **Routing** ↔ `facilities/urls.py`
