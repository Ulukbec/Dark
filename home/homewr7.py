def get_list() -> list:
    return list(range(0, 1_0000, 2))


class Solution:
    def __init__(self):
        pass

    def find_target(self, ist, target):
        if target not in ist:
            return f'Такого числа нету !'
        start = 0
        end = len(ist) - 1
        mid = (start + end) // 2
        while target != ist[mid]:
            if target > ist[mid]:
                start = mid
            elif target < ist[mid]:
                end = mid
            mid = (start + end) // 2
        return mid


element = int(input('Введите значение :'))
ist = get_list()
solution = Solution()
print(f'Index of: {solution.find_target(ist, element)}')
