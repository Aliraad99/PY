import signal
from fastapi import FastAPI
from app.database import engine, Base, get_db
from app.Routes.AuthRoutes import router as AuthRoutes
from app.Routes.UserRoutes import router as UserRoutes
from app.Routes.BlogRoutes import router as BlogRoutes


app = FastAPI()

app.include_router(AuthRoutes, prefix="/Auth", tags=["Auth"])
app.include_router(UserRoutes, prefix="/Users", tags=["Users"])
app.include_router(BlogRoutes, prefix="/Blogs", tags=["Blogs"])
