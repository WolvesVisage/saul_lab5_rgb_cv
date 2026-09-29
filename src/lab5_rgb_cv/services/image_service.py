import cv2
import numpy as np


def analizar_imagen_rgb(path: str):
    imagen_bgr = cv2.imread(path)

    if imagen_bgr is None:
        raise ValueError("No se pudo leer la imagen")

    # OpenCV carga en BGR; convertimos a RGB
    imagen_rgb = cv2.cvtColor(imagen_bgr, cv2.COLOR_BGR2RGB)

    # Separación de canales
    r = imagen_rgb[:, :, 0]
    g = imagen_rgb[:, :, 1]
    b = imagen_rgb[:, :, 2]

    medias = {
        "R": float(np.mean(r)),
        "G": float(np.mean(g)),
        "B": float(np.mean(b))
    }

    desviaciones = {
        "R": float(np.std(r)),
        "G": float(np.std(g)),
        "B": float(np.std(b))
    }

    total = medias["R"] + medias["G"] + medias["B"]

    if total > 0:
        porcentajes = {
            canal: round(valor / total * 100, 2)
            for canal, valor in medias.items()
        }
    else:
        porcentajes = {"R": 0.0, "G": 0.0, "B": 0.0}

    canal_dominante = max(medias, key=medias.get)

    # Reto adicional: clasificación simple basada en reglas
    if medias["R"] > medias["G"] and medias["R"] > medias["B"]:
        etiqueta = "ROJIZO"
    elif medias["G"] > medias["R"] and medias["G"] > medias["B"]:
        etiqueta = "VERDOSO"
    else:
        etiqueta = "AZULADO"

    return {
        "alto": int(imagen_rgb.shape[0]),
        "ancho": int(imagen_rgb.shape[1]),
        "canales": int(imagen_rgb.shape[2]),
        "media_rgb": {k: round(v, 2) for k, v in medias.items()},
        "desviacion_rgb": {k: round(v, 2) for k, v in desviaciones.items()},
        "participacion_rgb_pct": porcentajes,
        "canal_dominante": canal_dominante,
        "etiqueta": etiqueta
    }
