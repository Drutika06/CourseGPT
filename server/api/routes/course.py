from fastapi import APIRouter, Query
from services import openai_service

router = APIRouter()

@router.get("/generate_lesson", tags=["Lesson"])
def generate_lesson(topic: str = Query(..., description="Topic for the lesson")):
    """
    Generate a lesson plan using AI based on the given topic.
    """
    return openai_service.generate_lesson(topic)