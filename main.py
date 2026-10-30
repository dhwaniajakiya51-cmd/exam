from fastapi import FastAPI
from routes.student_routes import router as student_router

app = FastAPI(
    title="Student CRUD Application",
    description="FastAPI application for managing student records",
    version="1.0.0"
)

app.include_router(student_router)


@app.get("/")
def home():
    return {
        "message": "Welcome to the Student CRUD Application"
    }

















# from fastapi import FastAPI
# from routes.student_routes import router as student_router

# app = FastAPI()

# app.include_router(student_router)