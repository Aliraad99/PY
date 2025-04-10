from app.database import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey

class Blog(Base):
    __tablename__ = 'Blogs'
    Id = Column(Integer, primary_key=True, index=True)
    Title = Column(String)
    Body = Column(String)
    Likes = Column(Integer, nullable= True)
    
    PostedBy = Column(Integer, ForeignKey('Users.Id'))
    
    User = relationship("User", back_populates="Blogs")
        