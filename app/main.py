from fastapi import FastAPI

from app.auth.controller import router as auth_router

app = FastAPI()

# Mount the auth router under /auth
app.include_router(auth_router, prefix="/auth")

