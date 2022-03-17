import random


def unequal_random_assignments(data: list, num_clusters: int) -> list[int]:
    """Returns random cluster assignments for each indexed point in the dataset.
    Assignments are done by assigning a random cluster from 0 to clusters - 1 for each point.

    :param data: Dataset to cluster.
    :param num_clusters: Number of clusters.
    :return: Assignments to clusters.
    """
    return [random.randint(0, num_clusters - 1) for _ in data]


def equal_random_assignments(data: list, num_clusters: int) -> list[int]:
    """Returns random equal-sized cluster assignments for each indexed point in the dataset.
    Assignments are done using a round-robin assignment, followed by randomization.

    :param data: Dataset to cluster.
    :param num_clusters: Number of clusters.
    :return: Assignments to clusters.
    """
    assignments = [i % num_clusters for i in range(len(data))]
    random.shuffle(assignments)
    return assignments
