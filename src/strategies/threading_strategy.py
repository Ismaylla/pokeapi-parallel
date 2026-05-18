import os
import threading
from queue import Queue

from src.api.pokeapi import (
    get_pokemon_list,
    get_pokemon_data,
    get_pokemon_image_url
)

from src.download.image_downloader import download_image


OUTPUT_DIR = "data/images/threading"


def worker(queue):
    """
    Worker executado por cada thread.
    """

    while not queue.empty():

        pokemon = queue.get()

        try:

            name = pokemon["name"]
            url = pokemon["url"]

            print(f"[{threading.current_thread().name}] Processing {name}")

            pokemon_data = get_pokemon_data(url)

            image_url = get_pokemon_image_url(pokemon_data)

            output_path = os.path.join(
                OUTPUT_DIR,
                f"{name}.png"
            )

            download_image(image_url, output_path)

            print(f"[{threading.current_thread().name}] Downloaded {name}")

        except Exception as error:

            print(f"Error processing pokemon: {error}")

        finally:

            queue.task_done()


def run(limit=10, num_threads=4):
    """
    Executa download usando threading.
    """

    pokemons = get_pokemon_list(limit)

    queue = Queue()

    for pokemon in pokemons:
        queue.put(pokemon)

    threads = []

    for index in range(num_threads):

        thread = threading.Thread(
            target=worker,
            args=(queue,),
            name=f"Thread-{index + 1}"
        )

        thread.start()

        threads.append(thread)

    queue.join()

    for thread in threads:
        thread.join()