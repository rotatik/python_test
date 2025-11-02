from pydantic import BaseModel, EmailStr


class SuserRegister(BaseModel):
    email: EmailStr
    password: str

    class Config:
        orm_mode = True
