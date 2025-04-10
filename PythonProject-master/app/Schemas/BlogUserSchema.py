from pydantic import BaseModel
from app.Schemas.UserSchema import UserSchema


class BlogUserSchema(BaseModel):
    Id:int
    Title: str
    Body: str
    Likes:int
    PostedBy:int
    
    PostedByUser: "UserSchema"
    
    class Config:
        from_attributes  = True