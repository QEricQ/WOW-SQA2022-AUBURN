import traceback

from typing import List, Any
from TestOrchestrator4ML_main.generation.main import generateAttack
from TestOrchestrator4ML_main.label_perturbation_attack.knn import predict, calculate_k, calculate_metrics
from TestOrchestrator4ML_main.generation.probability_based_label_perturbation import generate_malicious_instance


def fuzz(method, fuzzed_args: List[Any]):
    for args in fuzzed_args:
        try:
            result = method(*args)
        except Exception as e:
            print(e)
        else:
            print("Fuzz Passed")


if __name__ == "__main__":
    fuzz_testing = [
        (
            generateAttack, [
                (None, 1),
                (0, None),
                (1, 10),
                (2.2, 3.3),
                ("testing", "try"),
            ]
        ),
        (
            predict, [
                (None, None),
                ("one", "two"),
                (0.1, 0.4),
                (1, 2),
                ("prediction", 0)
            ]
        ),
        (
            calculate_k, [
                ("one", "two", "three", "four"),
                (None, 0, 1, None),
                (None, None, None, None),
                (1.1, 2.2, 3.3, 4.4),
                (1, 2, 3, 4),
            ]
        ),
        (
            calculate_metrics, [
                (None, None, None),
                (1, 2, 3),
                (1.1, 2.2, 3.3),
                ("metrics", "loading", "Error"),
                ("one", 2, 3),
            ]
        ),
        (
            generate_malicious_instance, [
                (1, 0, None),
                (None, None, None),
                ("instance", "random", "input"),
                (10, 20, 30),
                (10.01, 20.02, 30.03),
                ("playing", 2, "days")
            ]
        )
    ]
    for method, fuzzed_args in fuzz_testing:
        fuzz(method, fuzzed_args)
