from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.Models.Blog import Blog as BlogModel
from app.Models.User import User as UserModel
from app.Schemas.BlogSchema import BlogSchema
from app.Schemas.BlogUserSchema import BlogUserSchema
from sqlalchemy.future import select

async def GetBlogById(BlogId: int, db: AsyncSession):
    result = await db.execute(select(BlogModel).filter(BlogModel.Id == BlogId))
    return result.scalars().first()

async def GetAllBlogs(db: AsyncSession):
    result = await db.execute(select(BlogModel))
    return result.scalars().all()

async def SaveBlog(BlogSc: BlogSchema, db: AsyncSession):
    db_blog: BlogModel
    if BlogSc.Id == 0 or BlogSc.Id is None:
        db_blog = BlogModel(
            Title=BlogSc.Title,
            Body=BlogSc.Body,
            Likes=BlogSc.Likes,
            PostedBy=BlogSc.PostedBy
        )
        db.add(db_blog)
    else:
        db_blog = await GetBlogById(db, BlogSc.Id)
        if db_blog is None:
            raise HTTPException(status_code=404, detail="Blog not found")
        db_blog.Title = BlogSc.Title
        db_blog.Body = BlogSc.Body
        db_blog.Likes = BlogSc.Likes

    await db.commit()
    await db.refresh(db_blog)
    return BlogSchema.from_orm(db_blog)

async def GeBlogWithUser(blog_id: int, db: AsyncSession):
    result = await db.execute(
        select(BlogModel)
        .join(UserModel, BlogModel.PostedBy == UserModel.Id)
        .filter(BlogModel.Id == blog_id)
    )
    blog = result.scalars().first()
    if not blog:
        raise HTTPException(status_code=404, detail="Blog not found")
    
    return BlogUserSchema.from_orm(blog)
