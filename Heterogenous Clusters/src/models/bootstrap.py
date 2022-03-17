from typing import Callable

from objectives import fitness_dist as score_assignment


def bootstrap(data: list, num_clusters: int, method: Callable[[list, int], list[int]], iterations: int) -> list[int]:
    """Bootstraps to find best assignment by repeatedly calling method and returning highest scoring assignment

    :param data: Dataset to cluster.
    :param num_clusters: Number of clusters.
    :param method: Method for clustering. Should take in a dataset and number of clusters.
    :param iterations: Number of assignments to consider
    :return: Assignments to clusters.
    """
    best_assignment = method(data, num_clusters)
    best_score = score_assignment(best_assignment, num_clusters, data)

    for _ in range(iterations - 1):
        assignment = method(data, num_clusters)
        score = score_assignment(assignment, num_clusters, data)

        if score > best_score:
            best_score = score
            best_assignment = assignment

    return best_assignment
