# 🥭 HIT237 Group 9 – Mango Pest & Disease Monitoring Web App

A Django web application developed as part of the HIT237 – Building Interactive Software unit.  
It allows users to register, manage mango farms, track pest and disease surveillance, and access a categorized pest/disease guide.

---

## 📦 Dependencies

This project uses the **Pillow** library for image handling in surveillance records.

### 📥 To Install Pillow:
```bash
pip install Pillow
```

---

## ⚙️ Setup Instructions

1. **Clone the repository**
```bash
git clone https://github.com/manishsinghbasnyat/hit237group9.git
cd hit237group9
```


2. **Apply migrations**
```bash
python manage.py migrate
```

3. **Run the development server**
```bash
python manage.py runserver
```

Access the app at: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 🧠 Key Features

- 🔐 User registration & login/logout
- 🏡 Farm management (add, view, edit, delete)
- 🐛 Pest & Disease catalog with detailed info
- 📋 Surveillance record form linked to user and farm
- 📊 Survey history and detail views
- 📚 Informational static pages: About, References

---

## 📁 App Structure Overview

### `accounts/` – Authentication & Farm CRUD

- `views.py`: Handles user registration, login, profile, and farm add/edit/delete
- `forms.py`: Custom user form, farm form
- `templates/accounts/`:
  - `register_user.html`, `login.html`, `profile.html`
  - `add_update_farm.html`, `farm_detail.html`, `farm_confirm_delete.html`

---

### `catalog/` – Pest & Disease Information

- `models.py`:
  - `Pest` and `Disease` models with description, control, lifecycle, and image fields
- `views.py`: Home, pest list, pest/disease detail, About, References
- `templates/catalog/`:
  - `pest_list.html`, `detail.html`, `about.html`, `references.html`

---

### `survey/` – Surveillance Recording

- `models.py`:
  - `Farm`: stores farm details and user ownership
  - `SurveillanceRecord`: links farm, user, pest(s), disease(s)
- `forms.py`:
  - `SurveillanceRecordForm` with custom date range validation and user-based farm filtering
- `views.py`:
  - Survey creation, history listing, and detail viewing
- `templates/survey/`:
  - `survey_home.html`, `surveillancerecord_form.html`, `my_surveys.html`, `survey_detail.html`

---

### `proj_mango/` – Project Configuration

- `settings.py`: Django settings, app registration, media/static setup
- `urls.py`: Includes routing for all apps
- `wsgi.py`, `asgi.py`: For deployment purposes

---

### `media/` – Uploaded Images

- Survey-related photos are stored here when submitted via forms

### `static/` – CSS & Image Assets

- `css/style.css`: Custom styling
- `images/`: Used in pest/disease catalog (e.g., Anthracnose, Mango scab)

### `templates/` – Base & Global Pages

- `base.html`: Shared layout across all templates
- `home.html`: Default landing page

---

## 🗃️ Database Design Summary

### Key Models

- `User`: Django’s built-in authentication system
- `Farm`: Linked to users; stores farm-specific data
- `Pest` / `Disease`: Descriptive models for catalog information
- `SurveillanceRecord`: Connects a user and their farm to the pests/diseases observed

### Relationships

- `User → Farm` (`ForeignKey`)
- `Farm → SurveillanceRecord` (`ForeignKey`)
- `SurveillanceRecord → Pest / Disease` (`ManyToManyField`)
- All deletions are protected by `CASCADE` behavior

---

## 👨‍💻 Authors

Developed by **Group 9**  
**HIT237 – Building Interactive Software**  
Charles Darwin University

