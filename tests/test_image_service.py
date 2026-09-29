import cv2
import numpy as np

from lab5_rgb_cv.services.image_service import analizar_imagen_rgb


def test_imagen_roja(tmp_path):
    # OpenCV almacena BGR: rojo puro = [0, 0, 255]
    imagen = np.zeros((20, 20, 3), dtype=np.uint8)
    imagen[:, :] = [0, 0, 255]

    path = tmp_path / "roja.png"
    cv2.imwrite(str(path), imagen)

    resultado = analizar_imagen_rgb(str(path))

    assert resultado["canal_dominante"] == "R"
    assert resultado["media_rgb"]["R"] == 255.0
    assert resultado["media_rgb"]["G"] == 0.0
    assert resultado["media_rgb"]["B"] == 0.0
