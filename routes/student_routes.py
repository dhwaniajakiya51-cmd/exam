from fastapi import APIRouter, Response, status

from models.student_model import Student, StudentCreate
from controllers import student_controller

router = APIRouter(
    prefix="/students",
    tags=["Students"]
)


# 1. Create Student
@router.post(
    "",
    response_model=Student,
    status_code=status.HTTP_201_CREATED
)
def create_student(student: StudentCreate):
    return student_controller.create_student(student)


# 2. Read All Students
@router.get(
    "",
    response_model=list[Student],
    status_code=status.HTTP_200_OK
)
def get_all_students():
    return student_controller.get_all_students()


# 3. Read Student by ID
@router.get(
    "/{student_id}",
    response_model=Student,
    status_code=status.HTTP_200_OK
)
def get_student_by_id(student_id: int):
    return student_controller.get_student_by_id(student_id)


# 4. Update Student
@router.put(
    "/{student_id}",
    response_model=Student,
    status_code=status.HTTP_200_OK
)
def update_student(student_id: int, student: StudentCreate):
    return student_controller.update_student(
        student_id,
        student
    )


# 5. Delete Student
@router.delete(
    "/{student_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_student(student_id: int):
    student_controller.delete_student(student_id)

    return Response(
        status_code=status.HTTP_204_NO_CONTENT
    )










# from fastapi import APIRouter, Response, status

# from models.student_model import (
#     StudentCreate,
#     StudentUpdate,
#     StudentResponse
# )

# from controllers import student_controller

# router = APIRouter(
#     prefix="/students",
#     tags=["Students"]
# )


# @router.post(
#     "",
#     response_model=StudentResponse,
#     status_code=status.HTTP_201_CREATED
# )
# def create_student(student: StudentCreate):
#     return student_controller.create_student(student)


# @router.get("", response_model=list[StudentResponse])
# def get_all_students():
#     return student_controller.get_all_students()


# @router.get(
#     "/{student_id}",
#     response_model=StudentResponse
# )
# def get_student_by_id(student_id: int):
#     return student_controller.get_student_by_id(student_id)


# @router.put(
#     "/{student_id}",
#     response_model=StudentResponse
# )
# def update_student(student_id: int, student: StudentUpdate):
#     return student_controller.update_student(
#         student_id,
#         student
#     )


# @router.delete(
#     "/{student_id}",
#     status_code=status.HTTP_204_NO_CONTENT
# )
# def delete_student(student_id: int):
#     student_controller.delete_student(student_id)

#     return Response(
#         status_code=status.HTTP_204_NO_CONTENT
#     )