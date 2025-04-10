from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.Auth.Authentication import get_current_user
from app.Repositories import BlogRepos as blog_repos
from app.Schemas.BlogSchema import BlogSchema
from app.Schemas.BlogUserSchema import BlogUserSchema
from app.database import get_db
from typing import List


router = APIRouter(
     dependencies=[Depends(get_current_user)]
)

@router.get("/GetAllBlogs", response_model=List[BlogSchema])
async def GetAllUsers(db: AsyncSession = Depends(get_db)):
    db_blogs = await blog_repos.GetAllBlogs(db)

    return db_blogs

@router.get("/GetBlogById/{BlogId}", response_model=BlogSchema)
async def GetBlogById(BlogId:int, db: AsyncSession = Depends(get_db)):
    db_blog = await blog_repos.GetBlogById(BlogId,db)
    return db_blog

@router.get("/GetBlogWithUser/{BlogId}", response_model=BlogUserSchema)
async def GetBlogWithUser(BlogId:int, db: AsyncSession = Depends(get_db)):
    db_blog = await blog_repos.get_blog_with_user(BlogId, db)

    return db_blog

@router.post("/SaveBlog", response_model=BlogSchema)
async def SaveBlog(Blog:BlogSchema, db: AsyncSession = Depends(get_db)):

    db_blog = await blog_repos.SaveBlog(Blog, db)
    if not db_blog:
        raise HTTPException(status_code=400, detail="Failed to save blog.")
    return db_blog
