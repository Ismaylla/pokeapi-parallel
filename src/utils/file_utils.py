import os


def clear_directory(directory_path):

    os.makedirs(directory_path, exist_ok=True)

    for file_name in os.listdir(directory_path):

        file_path = os.path.join(
            directory_path,
            file_name
        )

        if os.path.isfile(file_path):

            os.remove(file_path)