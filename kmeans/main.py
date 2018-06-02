from kmeans import kmeans
import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    N = 3000
    K = 6
    # print(np.random.randint(1, 101, N))
    x = np.random.randint(1, 10001, N)
    y = np.random.randint(1, 10001, N)

    points = [(x[index], y[index]) for index in range(0, N)]
    print(points)
    node_map = {}
    for index in range(0, N):
        node_map[index] = points[index]

    print(node_map)

    km = kmeans()
    clusterd_map = km.cluster(K, node_map)
    color = []

    for index in range(0, N):
        keys = clusterd_map.keys()

        for key in keys:
            if index in clusterd_map[key]:
                color.append(key)
                break

    plt.scatter(x, y, c=color, alpha=0.5)
    plt.show()