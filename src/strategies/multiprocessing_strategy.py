import os
import multiprocessing

from src.api.pokeapi import (
    get_pokemon_list,
    get_pokemon_data,
    get_pokemon_image_url
)

from src.download.image_downloader import download_image


OUTPUT_DIR = "data/images/multiprocessing"


def worker(queue):
    """
    Worker executado por cada processo.
    """

    while not queue.empty():

        try:

            pokemon = queue.get_nowait()

        except:

            break

        try:

            name = pokemon["name"]
            url = pokemon["url"]

            process_name = multiprocessing.current_process().name

            print(f"[{process_name}] Processing {name}")

            pokemon_data = get_pokemon_data(url)

            image_url = get_pokemon_image_url(pokemon_data)

            output_path = os.path.join(
                OUTPUT_DIR,
                f"{name}.png"
            )

            download_image(image_url, output_path)

            print(f"[{process_name}] Downloaded {name}")

        except Exception as error:

            print(f"Error processing pokemon: {error}")


def run(limit=10, num_processes=4):
    """
    Executa download usando multiprocessing.
    """

    pokemons = get_pokemon_list(limit)

    queue = multiprocessing.Queue()

    for pokemon in pokemons:
        queue.put(pokemon)

    processes = []

    for index in range(num_processes):

        process = multiprocessing.Process(
            target=worker,
            args=(queue,),
            name=f"Process-{index + 1}"
        )

        process.start()

        processes.append(process)

    for process in processes:
        process.join()