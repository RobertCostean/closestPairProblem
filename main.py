from math import sqrt
import matplotlib.pyplot as plt


def minDistance(points):
    if len(points) < 2:
        return float('inf'), ()

    if len(points) == 2:
        dist = sqrt((points[0][0] - points[1][0]) ** 2 + (points[0][1] - points[1][1]) ** 2)
        return dist, (points[0], points[1])

    points.sort(key=lambda p: p[0])

    n = len(points)
    if n % 2 == 0:
        median = (points[n // 2][0] + points[n // 2 - 1][0]) / 2
    else:
        median = points[n // 2][0]

    left_points = [p for p in points if p[0] <= median]
    right_points = [p for p in points if p[0] > median]

    min_left, pair_left = minDistance(left_points)
    min_right, pair_right = minDistance(right_points)

    delta = min(min_left, min_right)
    min_straddle, pair_straddle = straddleMin(points, median, delta)

    if min_left <= min(min_right, min_straddle):
        return min_left, pair_left
    elif min_right <= min(min_left, min_straddle):
        return min_right, pair_right
    else:
        return min_straddle, pair_straddle


def straddleMin(points, median, delta):
    points.sort(key=lambda p: p[1])
    minDist = float('inf')
    pair = ()
    n = len(points)
    for i, p1 in enumerate(points):
        for j, p2 in enumerate(points):
            if p1 == p2:
                continue
            if abs(p1[0] - p2[0]) > delta:
                continue
            dist = sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)
            if dist < minDist:
                minDist = dist
                pair = (p1, p2)
    return minDist, pair


def graphicalRepresentation(points, pair, median):
    xs, ys = zip(*points)
    plt.scatter(xs, ys)

    if pair:
        plt.plot([pair[0][0], pair[1][0]], [pair[0][1], pair[1][1]], 'r-')
    plt.plot([median, median], [0, max(ys)], 'g--')
    plt.show()


def main():
    points = [(1, 2), (1, 3), (4, 6), (6, 7)]
    n = len(points)
    if n % 2 == 0:
        median = (points[n // 2][0] + points[n // 2 - 1][0]) / 2
    else:
        median = points[n // 2][0]
    minDist, closestPair = minDistance(points)
    print(f"Minimum distance: {minDist:.2f}")
    print(f"Closest pair: {closestPair}")
    graphicalRepresentation(points, closestPair, median)


if __name__ == '__main__':
    main()
