from fastapi import APIRouter

router = APIRouter()

@router.get("/text_to_speech")
async def text_to_speech():
    return {"message": "Text-to-speech endpoint"}