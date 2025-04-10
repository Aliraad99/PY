from pydantic import BaseModel
from app.Schemas.UserSchema import UserSchema


class BlogSchema(BaseModel):
    Id:int
    Title: str
    Body: str
    Likes:int
    PostedBy:int
    
    class Config:
        from_attributes  = True
