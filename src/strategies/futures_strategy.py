import os

from concurrent.futures import ThreadPoolExecutor

from src.api.pokeapi import (
    get_pokemon_list,
    get_pokemon_data,
    get_pokemon_image_url
)

from src.download.image_downloader import download_image


OUTPUT_DIR = "data/images/futures"


def process_pokemon(pokemon):
    """
    Processa um único pokémon.
    """

    try:

        name = pokemon["name"]
        url = pokemon["url"]

        print(f"Processing {name}")

        pokemon_data = get_pokemon_data(url)

        image_url = get_pokemon_image_url(pokemon_data)

        output_path = os.path.join(
            OUTPUT_DIR,
            f"{name}.png"
        )

        download_image(image_url, output_path)

        print(f"Downloaded {name}")

    except Exception as error:

        print(f"Error processing pokemon: {error}")


def run(limit=10, workers=4):
    """
    Executa download usando ThreadPoolExecutor.
    """

    pokemons = get_pokemon_list(limit)

    with ThreadPoolExecutor(max_workers=workers) as executor:

        executor.map(process_pokemon, pokemons)