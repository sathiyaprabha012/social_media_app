# Social Media Backend Clone using FastAPI

This project is a backend clone of a social media application, built using **FastAPI** and modern backend technologies. It covers everything from basic API setup to advanced features like authentication, database management, testing, and deployment via CI/CD pipelines.

---

## 🚀 Features

- High-performance asynchronous APIs using **FastAPI**
- **User authentication** with OAuth2 and JWT
- **Relational data modeling** with SQLAlchemy
- **Database migrations** with Alembic
- **Dockerized** environment for development and production
- **CI/CD** using GitHub Actions
- Full **testing suite** with Pytest
- Clean and modular **project structure**

---

## 📦 Tech Stack

| Layer         | Technologies Used                              |
|---------------|-------------------------------------------------|
| **Backend**   | FastAPI, Python 3.11, Uvicorn                   |
| **Frontend**  | Postman (for API testing and interaction)       |
| **Database**  | PostgreSQL                                      |
| **ORM**       | SQLAlchemy                                      |
| **Validation**| Pydantic                                        |
| **Auth**      | OAuth2, JWT                                     |
| **Migrations**| Alembic                                         |
| **Testing**   | Pytest, FastAPI TestClient                      |
| **DevOps**    | Docker, Docker Compose                          |
| **CI/CD**     | GitHub Actions                                  |
| **Version Control** | Git, GitHub                             |
| **Configuration** | Environment Variables via `.env` files     |

---

## ⚙️ How to run Locally :

## Steps
1. **Clone the repository**
   git clone https://github.com/sathiyaprabha012/social_media_app.git
   cd social-media-app
2. **Create a virtual environment**
   python -m venv venv
   On Windows: venv\Scripts\activate
3. **Install dependencies**
   pip install -r requirements.txt
4. **Configure environment variables**
   Configure environment variables (say for example) :
     DATABASE_HOSTNAME=localhost
     DATABASE_PORT=5432
     DATABASE_PASSWORD=yourpassword
     DATABASE_NAME=yourdb
     DATABASE_USERNAME=yourusername
     SECRET_KEY=your-secret-key
     ALGORITHM=HS256
     ACCESS_TOKEN_EXPIRE_MINUTES=30
5. **Run database migrations**
   alembic upgrade head
6. **Start the development server**
   uvicorn app.main:app --reload
7. **Access the FastApi :**
     Once the server is up and running, you can access the **FastAPI** documentation and interact with the API directly:
     1. **Automatic Documentation**:  
   FastAPI provides automatic, interactive API documentation using **Swagger UI** and **ReDoc**. Once the server is running, open your browser and go to:

   - **Swagger UI**: [http://localhost:8000/docs](http://localhost:8000/docs)
   - **ReDoc**: [http://localhost:8000/redoc](http://localhost:8000/redoc)
     
    2. **API Testing**:  (optional)
   You can use **Postman** or any other HTTP client to interact with the endpoints. Here's a quick guide for using **Postman**:
   - Import the collection for easy testing of all endpoints.
   - Set up **Authorization** headers by adding a **Bearer token** if authentication is required (use the `/login` endpoint to get the token).

---

## 🧪 Testing :

To run all tests: pytest -v

---

## 🐳 Docker Support 

To run using Docker: docker-compose up --build
