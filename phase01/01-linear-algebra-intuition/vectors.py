import math


def vector_magnitude(vector):
    return math.sqrt(vector[0] **2 + vector[1] **2)


def vector_add(a, b):
    return [a[0] + b[0], a[1] + b[1]]


def vector_subtract(a, b):
    return [a[0] - b[0], a[1] - b[1]]



def scalar_multiply(k, vector):
    return [k * vector[0], k * vector[1]]


def dot_product(a, b):
    return a[0] * b[0] + a[1] * b[1]


def main():
    print(vector_magnitude([3, 4]))
    print(vector_magnitude([6, 8]))
    print(vector_magnitude([5, 12]))

    print(vector_add([2, 4], [3, 1]))
    print(vector_add([3, -2], [-1, 5]))

    print(vector_subtract([5, 4], [2, 1]))
    print(vector_subtract([3, -2], [-1, 5]))

    print(scalar_multiply(3, [2, -4]))
    print(scalar_multiply(6, [2, 4]))


    print(dot_product([2, 3], [4, 5]))

if __name__ == "__main__":
    main()

