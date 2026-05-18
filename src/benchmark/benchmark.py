import csv
import os

from statistics import mean

from src.utils.timer import measure_execution_time


RESULTS_DIR = "data/results/csv"
RESULTS_FILE = os.path.join(RESULTS_DIR, "results.csv")

def clear_results_file():

    if os.path.exists(RESULTS_FILE):

        os.remove(RESULTS_FILE)


def benchmark(
    strategy_name,
    strategy_function,
    limit=100,
    repetitions=10,
    workers=1
):

    execution_times = []

    print("\n===================================")
    print(f"Benchmark: {strategy_name}")
    print(f"Pokemons: {limit}")
    print(f"Executions: {repetitions}")
    print(f"Workers: {workers}")
    print("===================================\n")

    for execution in range(1, repetitions + 1):

        print(f"Execution {execution}...")

        if workers == 1:

            execution_time = measure_execution_time(
                strategy_function,
                limit
            )

        else:

            execution_time = measure_execution_time(
                strategy_function,
                limit,
                workers
            )

        execution_times.append(execution_time)

        print(f"Time: {execution_time:.2f} seconds\n")

    average_time = mean(execution_times)

    print("===================================")
    print(f"Average Time: {average_time:.2f} seconds")
    print("===================================\n")

    save_results(
        strategy_name,
        limit,
        workers,
        execution_times,
        average_time
    )


def save_results(
    strategy_name,
    limit,
    workers,
    execution_times,
    average_time
):

    os.makedirs(RESULTS_DIR, exist_ok=True)

    file_exists = os.path.isfile(RESULTS_FILE)

    with open(
        RESULTS_FILE,
        mode="a",
        newline=""
    ) as csv_file:

        writer = csv.writer(csv_file)

        if not file_exists:

            writer.writerow([
                "method",
                "quantity",
                "workers",
                "execution",
                "time_seconds"
            ])

        for index, execution_time in enumerate(execution_times):

            writer.writerow([
                strategy_name,
                limit,
                workers,
                index + 1,
                round(execution_time, 4)
            ])

        writer.writerow([
            strategy_name,
            limit,
            workers,
            "average",
            round(average_time, 4)
        ])