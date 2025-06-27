# 🧠 Django Internship Assignment API

This project is developed as part of an internship evaluation and demonstrates full-stack backend development using:

* Django + Django REST Framework (DRF)
* JWT Authentication
* Celery + Redis for background tasks
* Telegram Bot Integration using `python-telegram-bot`
* Environment variable management with `python-decouple`

---

## 📋 Features Implemented

| Feature                     | Description                                                              |
| --------------------------- | ------------------------------------------------------------------------ |
| 🔓 Public API               | Accessible by anyone (`/api/public/`)                                    |
| 🔐 Protected API            | Requires JWT token (`/api/protected/`)                                   |
| 🔑 JWT Auth                 | Token generation via `/api/token/` and refresh via `/api/token/refresh/` |
| 🔁 Celery with Redis        | Background email sending on user registration                            |
| 🤖 Telegram Bot             | Captures Telegram username on `/start` command                           |
| 𞷾 Clean Code & GitHub Repo | Modular, documented, `.env`-based, and version-controlled                |

---

## 🛠 Setup Instructions

### 1. 🔃 Clone the Repository

```bash
git clone https://github.com/yourusername/django-internship-assignment-api.git
cd django-internship-assignment-api
```

### 2. 🐍 Create & Activate Virtual Environment

```bash
python -m venv env
env\Scripts\activate       # Windows
# or
source env/bin/activate    # macOS/Linux
```

### 3. 📆 Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔐 Environment Variables

Create a `.env` file in the root directory:

```env
DEBUG=True
SECRET_KEY=your-django-secret-key
ALLOWED_HOSTS=127.0.0.1,localhost
TG_BOT_TOKEN=your-telegram-bot-token
```

---

## 🚀 Run the Server

```bash
python manage.py migrate
python manage.py runserver
```

Visit: [http://127.0.0.1:8000/api/public/](http://127.0.0.1:8000/api/public/)

---

## 📬 Start Celery Worker

Make sure Redis is running in background.

```bash
celery -A core worker -l info
```

---

## 🤖 Start Telegram Bot

```bash
python manage.py shell
>>> from api.telegram_bot import run_bot
>>> run_bot()
```

Send `/start` to your bot in Telegram. Your username will be saved to the DB.

---

## 🔐 Authentication Guide

* `POST /api/token/` — Login with username & password to get JWT
* `POST /api/token/refresh/` — Refresh access token
* `GET /api/public/` — Public route
* `GET /api/protected/` — Requires `Authorization: Bearer <access_token>`

---

## 🧶 Test Email Task (Background)

Inside Django shell:

```python
from api.tasks import send_welcome_email
send_welcome_email.delay("youremail@example.com")
```

---

## 📁 Folder Structure (Short)

```bash
core/
|
├── core/               # Django project
│   ├── settings.py
│   ├── celery.py
|
├── api/                # App: APIs + Telegram + Tasks
│   ├── views.py
│   ├── urls.py
│   ├── tasks.py
│   ├── telegram_bot.py
|
├── manage.py
├── .env
├── README.md
```

---

## 👨‍💼 Developer

* **Name:** T. Anil Kumar
* **Email:** [tholletianil728@gmail.com](mailto:tholletianil728@gmail.com)

---


