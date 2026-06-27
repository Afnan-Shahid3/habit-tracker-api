# Habit Tracker API

A REST API built with Django REST Framework for tracking daily and weekly habits. Supports user authentication, habit logging, filtering, searching, pagination, and habit summary statistics.

---

## Tech Stack

- Python 3
- Django
- Django REST Framework
- django-filter
- SQLite

---

## Features

- Token-based authentication (register, login, logout)
- Full CRUD for habits and habit habitlogs
- Ownership-based permissions (users can only access their own data)
- Filter habits by frequency, filter habitlogs by completion status and date
- Search habits by name
- Order habits and habitlogs by date
- Custom pagination (default 3 per page, max 5)
- Nested habit habitlogs inside habit detail response
- Summary endpoint with completion rate and streak stats

---

## Installation

```bash
# Clone the repository
git clone https://github.com/Afnan-Shahid3/habit-tracker-api.git
cd habit-tracker-api

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Create .env file
cp .env.example .env  # then add your SECRET_KEY

# Run migrations
python manage.py migrate

# Start the server
python manage.py runserver
```

---

## Environment Variables

Create a `.env` file in the root directory:

```
SECRET_KEY=your-secret-key-here
DEBUG=True
```

---

## API Endpoints

### Auth

| Method | Endpoint | Description | Auth Required |
|---|---|---|---|
| POST | `/api/auth/register/` | Register a new user | No |
| POST | `/api/auth/login/` | Login and get token | No |
| POST | `/api/auth/logout/` | Invalidate token | Yes |

### Habits

| Method | Endpoint | Description | Auth Required |
|---|---|---|---|
| GET | `/api/habits/` | List all your habits | Yes |
| POST | `/api/habits/` | Create a new habit | Yes |
| GET | `/api/habits/{id}/` | Retrieve a habit with nested habitlogs | Yes |
| PUT/PATCH | `/api/habits/{id}/` | Update a habit | Yes |
| DELETE | `/api/habits/{id}/` | Delete a habit | Yes |
| GET | `/api/habits/{id}/summary/` | Get stats for a specific habit | Yes |
| GET | `/api/habits/summary/` | Get overall stats across all habits | Yes |

### Habit Logs

| Method | Endpoint | Description | Auth Required |
|---|---|---|---|
| GET | `/api/habitlogs/` | List all your habitlogs | Yes |
| POST | `/api/habitlogs/` | Create a log entry | Yes |
| GET | `/api/habitlogs/{id}/` | Retrieve a log | Yes |
| PUT/PATCH | `/api/habitlogs/{id}/` | Update a log | Yes |
| DELETE | `/api/habitlogs/{id}/` | Delete a log | Yes |

---

## Authentication

All protected endpoints require a token in the request header:

```
Authorization: Token your-token-here
```

---

## Filtering, Searching & Ordering

### Habits

```
GET /api/habits/?frequency=daily
GET /api/habits/?frequency=weekly
GET /api/habits/?search=exercise
GET /api/habits/?ordering=created_at
GET /api/habits/?ordering=-created_at
GET /api/habits/?frequency=daily&search=exercise&ordering=-created_at
```

### Habit Logs

```
GET /api/habitlogs/?completed=true
GET /api/habitlogs/?completed=false
GET /api/habitlogs/?ordering=date
GET /api/habitlogs/?ordering=-date
```

---

## Pagination

Default page size is 3, maximum is 5. Clients can override using the `page_size` query param.

```
GET /api/habits/?page=2
GET /api/habits/?page_size=5
GET /api/habits/?page=1&page_size=2
```

Response format:

```json
{
    "count": 5,
    "next": "http://localhost:8000/api/habits/?page=2",
    "previous": null,
    "results": []
}
```

---

## Models

### Habit

| Field | Type | Description |
|---|---|---|
| name | CharField | Name of the habit |
| frequency | CharField | `daily` or `weekly` |
| created_at | DateTimeField | Auto-set on creation |
| user | ForeignKey | Owner of the habit |

### HabitLog

| Field | Type | Description |
|---|---|---|
| habit | ForeignKey | Related habit |
| date | DateField | Date of the log entry |
| completed | BooleanField | Whether habit was completed |

---

## Project Structure

```
habit-tracker-api/
├── core/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── habits/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   ├── permissions.py
│   ├── pagination.py
│   └── filters.py
├── .env
├── .gitignore
├── manage.py
└── requirements.txt
```

---

## Development Phases

| Phase | Description |
|---|---|
| Phase 1 | Project setup, models, migrations |
| Phase 2 | Serializers and basic CRUD endpoints |
| Phase 3 | Token authentication and ownership-based permissions |
| Phase 4 | Filtering, searching, and ordering |
| Phase 5 | Custom pagination |
| Phase 6 | Nested serializers and custom summary action endpoints |