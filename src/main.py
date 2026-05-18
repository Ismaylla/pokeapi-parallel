from src.strategies.sequential import run as sequential_run

from src.strategies.threading_strategy import (run as threading_run)

from src.strategies.multiprocessing_strategy import (run as multiprocessing_run)

from src.benchmark.benchmark import (benchmark, clear_results_file)

if __name__ == "__main__":
    
    clear_results_file()

    # benchmark(
    #     strategy_name="sequential",
    #     strategy_function=run,
    #     limit=100,
    #     repetitions=10,
    #     workers=1
    # )

    # # THREADING
    # benchmark(
    #     strategy_name="threading",
    #     strategy_function=threading_run,
    #     limit=100,
    #     repetitions=10,
    #     workers= 8
    # )

    # MULTIPROCESSING
    benchmark(
        strategy_name="multiprocessing",
        strategy_function=multiprocessing_run,
        limit=100,
        repetitions=10,
        workers=8
    )