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
    
    
#  Q3. a. Extend your CI workflow into a CI/CD pipeline with two jobs,test and deploy:
# (i) The test job installas dependencies and runs pytest.
# (ii) The deploy job must run only after the test job succeds (use needs) and only for pushes to the main branch.
# (iii)  The delpoy job calls the RenderDeploy HOOK URL using curl, where the URL is stored as a GitHub secret named RENDER_DEPLOY_HOOK
    
    
    
    
# Q4. Write a docker-compose.yml file(no database) that:
# (i) Builds the FASTAPI app from the Dockerfile in the current folder and names the service api.
# (ii) Maps port 8000 of the host to port 8000 of the container.
