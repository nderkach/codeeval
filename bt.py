

points = set()
points.add((0,0))

def sum_of_digits(number):
    return sum(map(int, str(number)))

def is_good(x, y):
    return sum_of_digits(abs(x))+sum_of_digits(abs(y)) <= 19

def add_neighbors(x, y):
    print len(points)
    print points
    for (i, j) in [(x+1, y), (x, y+1), (x-1, y), (x, y-1)]:
        if is_good(i, j) and (i, j) not in points:
            points.add((i, j))

if __name__ == "__main__":
    while True:
        for tu in points:
            le = len(points)
            add_neighbors(tu[0], tu[1])
            if len(points) > le:
                break

        if le == len(points):
            break

    print len(points)
