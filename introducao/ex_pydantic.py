from pydantic import BaseModel, validator

class User(BaseModel):
    
    name: str
    age: int
    email: str
    
    @validator('email')
    def validar_email(cls, email):
        if '@' not in email:
            raise ValueError('Invalid e-mail')
        return email
    

user = User(name="Leo", age=26, email='leogmail.com')
print(user)