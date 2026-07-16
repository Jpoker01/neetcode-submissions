import heapq
from typing import List


def get_reverse_sorted(nums: List[int]) -> List[int]:
    heap = []
    for num in nums:
        tuple_for_heap = (-num, num)
        heapq.heappush(heap, tuple_for_heap)
    
    reversed_nums = []
    while heap:
        popped_tuple = heapq.heappop(heap)
        reversed_nums.append(popped_tuple[1])
    return reversed_nums



# do not modify below this line
print(get_reverse_sorted([1, 2, 3]))
print(get_reverse_sorted([5, 6, 4, 2, 7, 3, 1]))
print(get_reverse_sorted([5, 6, -4, 2, 4, 7, -3, -1]))
