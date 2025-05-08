# carbon-equity-assessment

A Django-based web application for the technical assessment.

---

## 🚀 Setup instructions

### Create a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
```

### Install dependencies
```bash
pip install -r requirements.txt
```

### Create .env file in project root
```bash
cp .env.example .env
```

### Generate secret key
```bash
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```
Update `.env` file with the secret you generated 

### Database setup
- Ensure postgresql is installed and running
- Create the database and user
    ```bash
    CREATE DATABASE carbon_equity_db
    CREATE USER your_username WITH PASSWORD 'your_password'
    ```
- Generate a user and password for the carbon_equity_db
- Update .env file with these values:
    ```
    DB_USER=your_username
    DB_PASSWORD=your_password
    ```

### Run the development server
```
python manage.py runserver
```

Visit [http://127.0.0.1:8000/login](http://127.0.0.1:8000/login)