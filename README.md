# advanced-authentication-and-authroization-using-django-and-jwt

This project demonstrates an enterprise-grade authentication and authorization mechanism for a B2C/B2B application capable of handling millions of concurrent users. It uses **Django**, **Django REST Framework**, and **JWT** (via `djangorestframework-simplejwt`) to ensure secure, scalable, and high-performance user authentication.

## Key Architectural Considerations

- **Scalability:**
  - Stateless JWT-based authentication allows horizontal scaling without sticky sessions.
  - Microservices-ready architecture: this authentication service can be extracted into a standalone microservice.
  - Use of caching layers (e.g., Redis, Memcached) can be plugged in easily to handle token blacklisting or throttle requests.
- **Security:**
  - Short-lived JWT access tokens and refresh tokens for re-authentication.
  - Secure password hashing using Django’s default `PBKDF2` password hasher.
  - HTTPS enforcement and secure environment variable management.
- **Consistency and Reliability (CAP Theorem):**
  - The system can favor availability and partition tolerance by using stateless tokens.
  - Token validation does not rely heavily on central storage (except optional blacklists), enhancing availability.
- **OOP Principles & Design Patterns:**
  - **Service Layer Pattern:** Business logic encapsulated in `services.py`, decoupling it from views and models.
  - **Repository Pattern:** Data access is abstracted into `repositories.py`.
  - **SOLID Principles:** Each class and function has a single responsibility; interfaces are well-defined.

## Technologies and Concepts Used

- **Django**
- **Django REST Framework**
- **djangorestframework-simplejwt** for JWT handling
- **PostgreSQL** (recommended for production), SQLite (default dev)
- **Environment Variables** management via `.env` file
- **OOP (Encapsulation, Inheritance, Polymorphism)**
- **Design Patterns**: Service layer, Repository pattern
- **RESTful API** design best practices
- **12-Factor App** principles

## Directory Structure

```bash
advanced-authentication-and-authorization-using-django-and-jwt/
├─ README.md                          # Project documentation and instructions.
├─ .env                               # Environment variables for sensitive data and configuration.
├─ requirements.txt                   # List of Python dependencies required for the project.
├─ manage.py                          # Entry point to run Django commands (e.g., runserver, migrate).
└─ myproject/                         # Main Django project directory.
   ├─ __init__.py                     # Marks the directory as a Python package.
   ├─ asgi.py                         # ASGI configuration for asynchronous server deployments.
   ├─ settings.py                     # Main settings and configurations for the Django project.
   ├─ urls.py                         # Root URL routing configuration for the project.
   ├─ wsgi.py                         # WSGI configuration for deploying the project to production servers.
   └─ users/                          # Custom Django app for authentication and user management.
      ├─ __init__.py                  # Marks the directory as a Python package.
      ├─ admin.py                     # Registers the User model for the Django admin interface.
      ├─ apps.py                      # App configuration for the "users" app.
      ├─ migrations/                  # Database migration files for the "users" app.
      │  └─ __init__.py               # Marks the migrations directory as a Python package.
      ├─ models.py                    # Defines the User model and related database schema.
      ├─ serializers.py               # Serializers to convert User data between Python objects and JSON.
      ├─ services.py                  # Contains business logic (e.g., user registration).
      ├─ repositories.py              # Abstracts data access logic for cleaner code.
      ├─ permissions.py               # Custom permission classes for role-based access control.
      ├─ tests.py                     # Unit tests for the "users" app's models, views, and services.
      ├─ urls.py                      # URL routing specific to the "users" app endpoints.
      └─ views.py                     # API views for user registration, login, and protected endpoints.
```

## Environment Variables

```bash
SECRET_KEY=Django strong secret key
DEBUG=Debug mode toggle (True/False)
ALLOWED_HOSTS=Allowed hosts for this environment (e.g. 127.0.0.1,localhost)
DATABASE_URL=Database URL for PostgreSQL in production (e.g. sqlite:///db.sqlite3)
JWT_ACCESS_TOKEN_LIFETIME=JWT access token lifetime in minutes (e.g. 5)
JWT_REFRESH_TOKEN_LIFETIME=JWT refresh token lifetime in days (e.g. 1)
```

## Running the Application Locally

- **Ensure all Environment Variables are Set**:
    - Verify that the .env file contains all the necessary variables.

- **Install the requirements**:

```bash
pip install -r requirements.txt
```

- **Generate Migrations for the 'users' App**:

If no migration files are found inside the myproject/users/migrations/ folder, then run the following command to generate the migration files.

```bash
python manage.py makemigrations users
```

Verify that the migration file is created inside the myproject/users/migrations/ folder.

- **Apply migrations**:

```bash
python manage.py migrate
```

- **Run the development server**:

```bash
python manage.py runserver
```

- **Open your browser and visit:**:

```bash
http://127.0.0.1:8000/admin/
```

## Testing the Application

- **Submitting Data**: Use Postman or CURL to submit API request.
    - **Register**: POST http://127.0.0.1:8000/api/users/register/

    ```bash
    curl -X POST -H "Content-Type: application/json" -d '{"email":"test@example.com","password":"YourPassword123"}' http://127.0.0.1:8000/api/users/register/
    ```

    - **Obtain JWT token**: POST http://127.0.0.1:8000/api/users/token/

    ```bash
    curl -X POST -H "Content-Type: application/json" -d '{"email":"test@example.com","password":"YourPassword123"}' http://127.0.0.1:8000/api/users/token/
    ```

    - **Protected endpoint (requires Authorization: Bearer <access_token>)**: POST http://127.0.0.1:8000/api/users/me/

    ```bash
    curl -X GET -H "Authorization: Bearer <access_token>" http://127.0.0.1:8000/api/users/me/
    ```

## Deploying to AWS

- **Set up AWS environment (e.g., AWS EC2 or ECS):**
  - Provision an EC2 instance or container environment with Docker.
- **Production Dependencies:**
  - Use a production-grade database (e.g., Amazon RDS Postgres).
  - Update DATABASE_URL in .env with RDS connection string.
- **Build and Run:**
  - Install dependencies.
  - Set DEBUG=False and configure ALLOWED_HOSTS.
  - Run python manage.py migrate.
  - Serve with a production-grade server (e.g., gunicorn) behind Nginx.
- **Scaling:**
  - Run multiple Gunicorn workers.
  - Use AWS Load Balancer for distributing load across multiple EC2 instances.
  - Cache JWT blacklists in Redis (e.g., AWS ElastiCache) if required.
- **CI/CD Integration:**
  - Use GitHub Actions or AWS CodePipeline for continuous integration.
  - Automated tests run on each commit.

## License

*This project is licensed under the MIT License.*
