from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field

app = FastAPI()

# (i) Define the Pydantic Book model
class Book(BaseModel):
    isbn: str
    title: str
    author: str
    copies: int = Field(..., ge=0)


# In-memory dictionary to store books
books = {}


# (ii) POST /books - Add a new book
@app.post("/books", status_code=status.HTTP_201_CREATED)
def create_book(book: Book):
    if book.isbn in books:
        raise HTTPException(
            status_code=400,
            detail="ISBN already exists"
        )

    books[book.isbn] = book
    return book


# GET /books - List all books
@app.get("/books")
def get_all_books():
    return books


# GET /books/{isbn} - Get a book by ISBN
@app.get("/books/{isbn}")
def get_book(isbn: str):
    if isbn not in books:
        raise HTTPException(
            status_code=404,
            detail="Book not found"
        )

    return books[isbn]


# (b)(i) PATCH /books/{isbn} - Borrow a book
@app.patch("/books/{isbn}")
def borrow_book(isbn: str):
    if isbn not in books:
        raise HTTPException(
            status_code=404,
            detail="Book not found"
        )

    book = books[isbn]

    if book.copies == 0:
        raise HTTPException(
            status_code=409,
            detail="No copies available"
        )

    book.copies -= 1
    return book


# (b)(ii) GET /health - Health check
@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/")
def home():
    return {"message": "FastAPI application is running"}








# from fastapi import FastAPI
# from routes.student_routes import router as student_router

# app = FastAPI(
#     title="Student CRUD Application",
#     description="FastAPI application for managing student records",
#     version="1.0.0"
# )

# app.include_router(student_router)


# @app.get("/")
# def home():
#     return {
#         "message": "Welcome to the Student CRUD Application"
#     }

















# from fastapi import FastAPI
# from routes.student_routes import router as student_router

# app = FastAPI()

# app.include_router(student_router)