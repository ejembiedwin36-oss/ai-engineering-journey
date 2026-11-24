matrix_a = [
    [1, 2],
    [3, 4]
]

matrix_b = [
    [5, 6],
    [7, 8]
]


# matrix_b = [
#     [5, 6, 7],
#     [8, 9, 10]
# ]

if len(matrix_a) != len(matrix_b) or len(matrix_a[0]) != len(matrix_b[0]):
    print("These matrices cannot be added because their shapes are different.")
else:

    result = []

    for row in range(len(matrix_a)):
        new_row = []

        for column in range(len(matrix_a[row])):
            addition = matrix_a[row][column] + matrix_b[row][column]
            new_row.append(addition)
        result.append(new_row)
    print(result)
