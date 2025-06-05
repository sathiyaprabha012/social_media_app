# 📱 Social Media Backend Clone using FastAPI

A **backend clone of a social media application** built using **FastAPI** and modern backend technologies. This project demonstrates the entire backend development workflow—from API design to testing and CI/CD deployment.

---

## 🚀 Features

- ⚡ High-performance asynchronous APIs with **FastAPI**
- 🔐 User authentication with OAuth2 and JWT tokens
- 🧱 Relational data modeling using SQLAlchemy
- 🔄 Database migrations using Alembic
- 🐳 Fully Dockerized environment for development & production
- 🧪 Robust testing suite with Pytest
- 🔄 CI/CD pipeline using GitHub Actions
- ✅ Modular, scalable and clean project structure

---

## 📦 Tech Stack

| Layer              | Technologies Used                              |
|--------------------|-------------------------------------------------|
| **Backend**        | FastAPI, Python 3.11, Uvicorn                   |
| **API Testing**    | Postman                                         |
| **Database**       | PostgreSQL                                      |
| **ORM**            | SQLAlchemy                                      |
| **Validation**     | Pydantic                                        |
| **Authentication** | OAuth2, JWT                                     |
| **Migrations**     | Alembic                                         |
| **Testing**        | Pytest, FastAPI TestClient                      |
| **DevOps**         | Docker, Docker Compose                          |
| **CI/CD**          | GitHub Actions                                  |
| **Version Control**| Git, GitHub                                     |
| **Config**         | Environment variables via `.env` files          |

---

## ⚙️ How to Run Locally

1. **Clone the repository:**  
`git clone https://github.com/sathiyaprabha012/social_media_app.git && cd social_media_app`

2. **Create a virtual environment:**  
`python -m venv venv`  
On Windows: `venv\Scripts\activate`  
On Mac/Linux: `source venv/bin/activate`

3. **Install dependencies:**  
`pip install -r requirements.txt`

4. **Configure environment variables:**  
<pre>Create a `.env` file in the root directory and paste the following:```

DATABASE_HOSTNAME=localhost
DATABASE_PORT=5432
DATABASE_USERNAME=yourusername
DATABASE_PASSWORD=yourpassword
DATABASE_NAME=yourdb
SECRET_KEY=your-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30```</pre>


5. **Run database migrations:**  
`alembic upgrade head`

6. **Start the development server:**  
`uvicorn app.main:app --reload`

7. **Access the API docs:**  
- Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)  
- ReDoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)

---

## 🔍 API Testing

You can use **Postman** or any other HTTP client to test the API.  
- Import a Postman collection (optional).  
- To access protected routes, first call the `/login` endpoint to receive a JWT token and include it in the `Authorization` header as a **Bearer token**.

---

## 🧪 Run Tests

To run all tests using Pytest, execute:  
`pytest -v`

---

## 🐳 Docker Support

To build and run the app using Docker Compose:  
`docker-compose up --build`

---

## Video Demonstration :     [Demo](https://drive.google.com/file/d/1GTCkg_5FFhtO6ONdlLLWoOXpOhiPgG6j/view?usp=sharing)
