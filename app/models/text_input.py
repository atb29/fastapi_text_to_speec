from pydantic import BaseModel
from typing import Optional

class TextInput(BaseModel):
    text: str
    speaker: str = "en_speaker_6"
    language: str = "en"
    save_to_file: bool = False
    file_path: Optional[str] = None