'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurrences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    if len(word) < 1:
        return 0
    elif word[0:2] == 'th':
        return 1 + count_th(word[1:])
    else:
        return count_th(word[1:])

# TEST CASES FOR Algorithms_Questions.md
# def a(n):
#     a = 0
#     while (a < n * n * n):
#       a = a + n * n
#     return a

# print('a:', a(4))
# print('a:', a(5))
# print('a:', a(6))
# print('a:', a(7))
# print('a:', a(8))

# def find_sum(n):
#     sum = 0
#     for i in range(n):
#       j = 1
#       while j < n:
#         j *= 2
#         sum += 1
#     return sum

# print('sum:', find_sum(5))
# print('sum:', find_sum(6))
# print('sum:', find_sum(7))
# print('sum:', find_sum(8))
# print('sum:', find_sum(9))

# def bunnyEars(bunnies):
#       if bunnies == 0:
#         return 0

#       return 2 + bunnyEars(bunnies-1)
# print('bunny:', bunnyEars(1))
# print('bunny:', bunnyEars(2))
# print('bunny:', bunnyEars(3))
# print('bunny:', bunnyEars(4))
# print('bunny:', bunnyEars(5))