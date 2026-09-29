from pathlib import Path
import shutil

from fastapi import FastAPI, UploadFile, File, HTTPException
from lab5_rgb_cv.services.image_service import analizar_imagen_rgb

app = FastAPI(title="API de Análisis RGB")

DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)


@app.post("/analyze-rgb")
def analyze_rgb(file: UploadFile = File(...)):
    path = DATA_DIR / file.filename

    with open(path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    try:
        resultado = analizar_imagen_rgb(str(path))
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc))

    return {
        "mensaje": "Análisis RGB exitoso",
        "archivo": file.filename,
        "resultado": resultado
    }
