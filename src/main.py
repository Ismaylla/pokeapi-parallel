from src.strategies.sequential import run

from src.benchmark.benchmark import benchmark



if __name__ == "__main__":

    benchmark(
        strategy_name="sequential",
        strategy_function=run,
        limit=10,
        repetitions=3
    )