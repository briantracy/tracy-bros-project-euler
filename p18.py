

def maximum_path(triangle_text):
    '''
    Crux: the maximum path from a given point in the triangle is the value of
    the triangle at that point, plus the larger of the two maximum paths of the numbers
    adjacent in the row below. Since the last row is a degenerate case (there are no rows below),
    the maximum paths here are just the values in the last row.

    We can then compute the maximum paths moving upwards, with each row depending on the
    already computed values from the row below.

    We can now visit each element just once and compute all the maximum paths as we go.

    See problem 67, which uses this code on a much larger triangle
    '''
    triangle = [[int(num) for num in row.split(' ')] for row in triangle_text.split('\n')]
    # Create a map from (row, col) -> maximum path from that point
    max_path = {}
    for row in range(len(triangle))[::-1]:
        for col in range(row + 1):
            if row == len(triangle) - 1:
                # Final row, base case
                max_path[(row, col)] = triangle[row][col]
            else:
                max_path[(row, col)] = triangle[row][col] + \
                    max(max_path[(row + 1, col)], max_path[(row + 1, col + 1)])

    return max_path[(0, 0)]


if __name__ == '__main__':
    print(maximum_path(\
'''75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'''))
