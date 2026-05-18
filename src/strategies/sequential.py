import os
from src.utils.file_utils import clear_directory

from src.api.pokeapi import (
    get_pokemon_list,
    get_pokemon_data,
    get_pokemon_image_url
)

from src.download.image_downloader import download_image


OUTPUT_DIR = "data/images/sequential"


def run(limit=10):
    """
    Executa download sequencial das imagens.
    """

    clear_directory(OUTPUT_DIR)

    pokemons = get_pokemon_list(limit)

    for pokemon in pokemons:

        name = pokemon["name"]
        url = pokemon["url"]

        print(f"Processing {name}...")

        try:

            pokemon_data = get_pokemon_data(url)

            image_url = get_pokemon_image_url(pokemon_data)

            output_path = os.path.join(
                OUTPUT_DIR,
                f"{name}.png"
            )

            download_image(image_url, output_path)

            print(f"Downloaded {name}")

        except Exception as error:

            print(f"Error processing {name}: {error}")