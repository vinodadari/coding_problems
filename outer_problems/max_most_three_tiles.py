"""
There is an array A of N integers and three tiles. 
Each tile can cover two neighbouring numbers from the array but cannot intersect with another tile. 
It also cannot be placed outside the array, even partially.


Write a function:

def solution (A)
    that, given an array A of N integers, returns the maximum sum of numbers that can be covered using at most three tiles.
	
Examples:
1. Given A = [2, 3, 5, 2, 3, 4, 6, 4, 1], the function should return 25. There is only one optimal placement of tiles: (3, 5), (3, 4), (6,4).
2. Given A = [1, 5, 3, 2, 6, 6, 10, 4, 7, 2, 1], the function should return 35. One of the three optimal placements of tiles is (5, 3), (6, 10), (4, 7).
3. Given A = [1, 2, 3, 3, 2], the function should return 10. There is one optimal placement of tiles: (2, 3), (3,2). Only two tiles can be used because A is too small to contain another one.
4. Given A = [5, 10, 3], the function should return 15. Only one tile can be used.


Write an efficient algorithm for the following assumptions:
• N is an integer within the range [2..100,000];
* each element of array A is an integer within the range [0..1,000,000].

------------------------------------------------------------------------

solution approach

A = [2,3,5,2,3,4,6,4,1]

assumptions:
* count of A should with in 2 and 100000
* each element of A should be with in 0 to 1000000

# i will apply the filter for elements
# i will write the condition for count of A

    output -> three tiles -> 6 integers
        cond 1 - no repetative nums more than 2
        654433
        654321
        654311
        664433 - 63 64 34
        you should know the repetative int
            then you can map with non-repetative num
"""


def get_max_elements(A: list):
    max_elements = []
    for i in range(0, len(A)):
        max_num = max(A)
        if max_num not in max_elements:
            max_elements.append(max_num)
            A.remove(max_num)
        else:
            is_repetative_more_than_two = (
                True if 2 < max_elements.count(max_num) else False
            )
            if is_repetative_more_than_two is False:
                max_elements.append(max_num)
                A.remove(max_num)
        if 6 <= len(max_elements):
            return max_elements
    return max_elements


def solution(A):
    filtered_element_within_range = list(
        filter(lambda value: (0 <= value) and (value <= 10**6), A)
    )
    count_A = len(list(filtered_element_within_range))
    print(filtered_element_within_range)
    tiles = []

    if (2 <= count_A) and (count_A <= 10**5):
        max_elements = sorted(get_max_elements(A))
        while 0 < max_elements.__len__():
            tile_node_1 = min(max_elements)
            for _ in range(0, len(max_elements)):
                tile_node_2 = max_elements[_]
                if tile_node_1 < tile_node_2:
                    tile = (tile_node_1, tile_node_2)
                    if tile not in tiles:
                        tiles.append(tile)
                        max_elements.remove(tile_node_1)
                        max_elements.remove(tile_node_2)
                        break

        return tiles


if __name__ == "__main__":
    A = [2, 3, 5, 2, 3, 4, 6, 4, 1]
    A = [6, 6, 4, 4, 3, 3, 3]
    output = solution(A)
    print(output)
