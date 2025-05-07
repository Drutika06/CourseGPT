from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routes import course

app = FastAPI(title="CourseGPT API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(course.router)