# Payloads Manager

A Django-based web application for managing aircraft interior payload components and related engineering work items. The system models payload parts, tracks associated tasks, and provides a dashboard for engineering workload visibility.

---

## Features

### Part Management
- Store part number, name, description, and status (Proposed, Approved, Deprecated)
- View detailed part pages with associated work items

### Work Item Tracking
- Add work items linked to specific parts
- Track title, description, priority (High, Medium, Low), and due date
- Priority and due dates are visually styled for readability

### Dashboard
- Displays total parts and total work items
- Highlights number of high-priority tasks
- Shows work items due in the next seven days
- Includes an "Upcoming Work Items" list with direct part links

---

## Technology Stack
- Python 3  
- Django 6  
- SQLite (development)  
- HTML templates with inline CSS  
- Gunicorn (production)

---
Note: The current version focuses on viewing parts and adding work items. Parts and tasks are created through the Django Admin interface, while the public-facing UI supports viewing parts and adding work items only. Editing and deletion features are not implemented yet and are planned as future enhancements.

### Future Enhancements
- Add edit/delete capabilities for Parts and Work Items
- Add user authentication and role permissions
- Support inline status updates and task completion tracking
- Implement REST API endpoints (Django REST Framework)
- Deployment automation and persistent cloud database

## Setup Instructions

```bash
git clone <repository-url>
cd payloads-manager

python -m venv .venv
source .venv/bin/activate       # Windows: .venv\Scripts\activate

pip install -r requirements.txt
python manage.py migrate
python manage.py runserver


