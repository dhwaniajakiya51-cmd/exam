from pydantic import BaseModel, Field, EmailStr


class StudentCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    email: EmailStr
    course: str = Field(..., min_length=1, max_length=100)
    semester: int = Field(..., ge=1, le=12)


class Student(StudentCreate):
    id: int = Field(..., gt=0)






# import re
# from pydantic import BaseModel, Field, field_validator


# class StudentCreate(BaseModel):
#     name: str = Field(..., min_length=2, max_length=100)
#     email: str
#     course: str = Field(..., min_length=2, max_length=100)
#     semester: int = Field(..., ge=1, le=12)

#     @field_validator("email")
#     @classmethod
#     def validate_email(cls, value):
#         value = value.strip()

#         if not re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", value):
#             raise ValueError("Invalid email address")

#         return value


# class StudentUpdate(StudentCreate):
#     pass


# class StudentResponse(StudentCreate):
#     id: int
    
    
#   Q2. a. Create a FastAPI application (without database) for  library book inventory,storing data in an in-memory dictionary. 
#    (i) Define a Pydantic model Book with ibsn(str), title(str), author(str), copies(int,must be 0 or more).
#    (ii) Create POST /books (return HTTP 400 if the ISBN already exists) , GET/books to list all books, GET/books/{isbn} (return HTTP 404 if not found).    
#   b. Extend the above application:
#       (i) Add PATCh /books/{isbn} borrow that reduces the number odf copies by one, and return HTTP 409 if no copies are available.
#       (ii) Add a GET/health endpoint that returns{"ststus":"ok"}.
#       (iii) Write the pip command to install the required packages and the uvicorn command to start the app.
         
    
    
    
    
    
    
#     Q1. a. Create a FastAPI application(without database) for managing students,storing data in an in-memory python list. 
#     (i) Define a Pydantic model Student with id(int), name(str), course(str), marks(float,must be between0 and 100).
#     (ii) Create POST /students to add a student,GET/students/{id} to fetch one student(return HTTP 404 if not found)
#     b. Extend the above application:
#         (i) Add PUT /students/{id} to update student and DELETE /students/{id} to delete a student.
#         (ii) Add an optional query parameter course to GET / students to filter students by course.
#         (iii) Write the uvicorn command to run the app with auto-reload and stste the URL where Swagger UI can be tested.