import math

class KMeans:
    def __init__(self):
        pass

    def get_points(self, keys):
        return [self.node_map[key] for key in keys]

    def cluster(self, k, node_map):
        self.k = k
        self.node_map = node_map
        self.center_points = []
        self.cluster_map = {}
        self.keys = [key for key in self.node_map.keys()]

        for index in range(0, k):
            self.center_points.append(self.node_map[self.keys[index]])
            self.cluster_map[index] = [self.keys[index]]

        for index in range(k, len(self.keys)):
            min_index = self.closest_center_point_index(self.keys[index])
            self.cluster_map[min_index].append(self.keys[index])

        isChanged = True

        while isChanged:
            self.calc_center_points()
            temp_cluster_map = {}
            isChanged = False

            for index in range(0, len(self.keys)):
                min_index = self.closest_center_point_index(self.keys[index])

                if min_index in temp_cluster_map:
                    temp_cluster_map[min_index].append(self.keys[index])
                else:
                    temp_cluster_map[min_index] = [self.keys[index]]

                if not self.keys[index] in self.cluster_map[min_index]:
                    isChanged = True
                else:
                    isChanged = isChanged or False

            self.cluster_map = temp_cluster_map

        return self.cluster_map

    def closest_center_point_index(self, key):
        point = self.node_map[key]

        min_index = 0
        min_distance = self.calc_distance(point, self.center_points[0])

        for index in range(1, self.k):
            distance = self.calc_distance(point, self.center_points[index])

            if min_distance > distance:
                min_distance = distance
                min_index = index

        return min_index

    def calc_distance(self, a, b):
        return math.sqrt(sum([(a[index] - b[index])**2 for index in range(0, len(a))]))

    def calc_center_points(self):
        for index in range(0, self.k):
            center_point = self.calc_center_point(self.get_points(self.cluster_map[index]))
            self.center_points[index] = center_point

    def calc_center_point(self, cluster):
        if len(cluster) == 0:
            return ()

        if len(cluster) == 1:
            return cluster[0]

        result = cluster[0]

        for cIndex in range(1, len(cluster)):
            result = tuple([result[index] + cluster[cIndex][index] for index in range(0, len(result))])

        num = len(cluster)

        return tuple([x/num for x in result])


if __name__ == "__main__":
    km = KMeans()

    node_map = {
        "A": (0,),
        "B": (2,),
        "C": (2.5,),
        "D": (5,),
        "E": (7,)
    }

    cluster_map = km.cluster(2, node_map)
    print(cluster_map)