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






# print(vector[0])
# print(vector[1])
    
# print(vector)

# print(vector[0]**2)
# print(vector[1]**2)
# print(vector[0] **2 + vector[1] **2)

# print(math.sqrt(25))