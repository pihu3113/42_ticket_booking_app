# Ticket Booking System

A Django-based movie ticket booking system with MySQL, Docker, and CI/CD (Jenkins) support.

---

## Features
- User registration, login, and booking history
- List of movies (shows) with available seats and prices
- Book tickets for available shows
- MySQL database backend
- Minimal, wireframe-style UI
- DevOps: Docker, Docker Compose, Jenkins pipeline

---

## Local Development Setup

### 1. Clone the Repository
```sh
git clone <your-repo-url>
cd ticket_booking_system
```

### 2. Create and Activate a Virtual Environment (optional but recommended)
```sh
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```sh
pip install -r requirements.txt
```

### 4. Setup MySQL Database
- Make sure MySQL is running.
- Create a database named `ticket_db` and a user with the credentials in `settings.py` or your environment variables.

### 5. Run Migrations
```sh
python manage.py makemigrations
python manage.py migrate
```

### 6. Create a Superuser (for admin access)
```sh
python manage.py createsuperuser
```

### 7. (Optional) Add Sample Movies
```sh
python manage.py add_sample_movies
```

### 8. Run the Development Server
```sh
python manage.py runserver
```

Visit [http://localhost:8000](http://localhost:8000)

---

## Docker & Docker Compose Setup

### 1. Build and Start Services
```sh
docker-compose up --build
```
- The web app will be available at [http://localhost:8000](http://localhost:8000)
- MySQL runs in a container 

### 2. Stopping Services
```sh
docker-compose down
```

### 3. Common Issues
- **Port 3306 already in use:** Change the host port in `docker-compose.yml` (e.g., `3307:3306`).
- **Site can't be reached:**
  - Make sure both `web` and `db` containers are running (`docker ps`).
  - Check logs: `docker-compose logs web` and `docker-compose logs db`.
  - Wait a few seconds after startup for the DB to initialize.
- **Database errors:** Ensure your Django settings use:
  - `DB_HOST=db`
  - `DB_PORT=3306`
  - `DB_NAME=ticket_db`
  - `DB_USER=root`
  - `DB_PASSWORD=krc077@msql`

---

## CI/CD with Jenkins
- The `Jenkinsfile` defines build, test, and deploy stages using Docker Compose.
- To use Jenkins:
  1. Set up a Jenkins server with Docker installed.
  2. Add this repo as a pipeline project.
  3. Jenkins will use the `Jenkinsfile` for CI/CD.

---

## Environment Variables
You can override DB and Django settings using environment variables (see `docker-compose.yml`).

---

## Admin Access
- Visit `/admin` to manage movies, venues, and bookings.

---

## License
MIT (or specify your license) 