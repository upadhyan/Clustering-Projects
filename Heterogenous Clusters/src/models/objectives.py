import numpy as np


def fitness_dist(ind, k, data):
    ind_np = np.array(ind)
    sum_dist = 0
    for i in range(k):
        temp = data[ind_np == i, :]
        size = temp.shape[0]
        if size != 0:
            centroid = np.mean(temp, axis=0)
            dist = (temp[:, 0] - centroid[0]) ** 2 + (temp[:, 1] - centroid[1]) ** 2 + (
                        temp[:, 2] - centroid[2]) ** 2 + (temp[:, 3] - centroid[3]) ** 2
            sum_dist = sum_dist + (np.sum(np.sqrt(dist)) / size)

    return sum_dist
