import os
import requests


def download_image(image_url, output_path):
    """
    Faz download da imagem e salva no disco.
    """

    if image_url is None:
        return

    response = requests.get(image_url, timeout=10)

    response.raise_for_status()

    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path, "wb") as file:
        file.write(response.content)