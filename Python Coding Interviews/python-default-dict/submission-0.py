from collections import defaultdict
from typing import List, Dict


def count_chars(s: str) -> Dict[str, int]:
    char_dict = defaultdict(int)
    for c in s:
        char_dict[c] += 1
    return char_dict


def nested_list_to_dict(nums: List[List[int]]) -> Dict[int, List[int]]:
    output_dict = defaultdict(list)
    for nums_rows in nums:
        output_dict[nums_rows[0]] += nums_rows[1:]
    return output_dict


# do not modify below this line
print(count_chars("hello"))
print(count_chars("helloworld"))
print(count_chars("areallylongstringwhyareyoureadingthishahalol"))

print(nested_list_to_dict([[1, 2, 3], [4, 5, 6], [1, 4]]))
print(nested_list_to_dict([[1, 2, 3, 4], [4, 5, 6, 7], [1, 4, 5, 6]]))
print(nested_list_to_dict([[5, 2, 3, 4, 5], [4, 5, 6, 7, 8], [5, 6, 7, 8, 9]]))
print(nested_list_to_dict([[3, 2, 3, 4, 5], [4, 5, 6, 7, 8], [5, 6, 7, 8]]))
