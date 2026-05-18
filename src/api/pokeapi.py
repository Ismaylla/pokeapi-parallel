import requests

BASE_URL = "https://pokeapi.co/api/v2/pokemon"


def get_pokemon_list(limit=10):
    """
    Retorna uma lista de pokémons com nome e URL.
    """

    response = requests.get(
        f"{BASE_URL}?limit={limit}",
        timeout=10
    )

    response.raise_for_status()

    data = response.json()

    return data["results"]


def get_pokemon_data(url):
    """
    Retorna os dados completos de um pokémon.
    """

    response = requests.get(url, timeout=10)

    response.raise_for_status()

    return response.json()


def get_pokemon_image_url(pokemon_data):
    """
    Extrai a URL da imagem do pokémon.
    """

    return pokemon_data["sprites"]["front_default"]