import math

vector = [3, 4]

def vector_magnitude(vector):
    return math.sqrt(vector[0] **2 + vector[1] **2)


def main():
    print(vector_magnitude([3, 4]))
    print(vector_magnitude([6, 8]))
    print(vector_magnitude([5, 12]))

if __name__ == "__main__":
    main()



def vector_add(a, b):
    return [a[0] + b[0], a[1] + b[1]]


def main():
    print(vector_add([2, 4], [3, 1]))
    print(vector_add([3, -2], [-1, 5]))

if __name__ == "__main__":
 
    main()

def vector_subtract(a, b):
    return [a[0] - b[0], a[1] - b[1]]

def main():
    print(vector_subtract([5, 4], [2, 1]))
    print(vector_subtract([3, -2], [-1, 5]))

if __name__ == "__main__":
    main()



# print(vector[0])
# print(vector[1])
    
# print(vector)

# print(vector[0]**2)
# print(vector[1]**2)
# print(vector[0] **2 + vector[1] **2)

# print(math.sqrt(25))