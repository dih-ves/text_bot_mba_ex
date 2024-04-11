from fastapi import APIRouter, Request
from pydantic import BaseModel
from utils.tradutor import recebe_texto
from utils.gera_audio import transforma_texto_audio
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse


router = APIRouter(
    tags=['ETL extract, transform and load data.']
)


class Item(BaseModel):
    text: str | None = None


@router.post("/")
async def create_item(item: Item):
    traduzido = recebe_texto(item.text)
    transforma_texto_audio(traduzido)
    file_path = "exemplo.mp3"
    return FileResponse(path=file_path, filename="exemplo.mp3")
