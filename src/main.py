from src.strategies.sequential import run

from src.benchmark.benchmark import (
    benchmark,
    clear_results_file
)



if __name__ == "__main__":
    
    clear_results_file()

    benchmark(
        strategy_name="sequential",
        strategy_function=run,
        limit=10,
        repetitions=3,
        workers=1
    )