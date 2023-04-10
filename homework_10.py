# 1 method
def palindrome(s):
    s = s.strip()
    s = s.lower()
    return s == s[::-1]
s = input("Wtight your palindrome: ")

print(palindrome(s))

# 2 method
# def palindrome(s):
#     s = s.strip()
#     s = s.lower()
#     n = len(s) // 2
#     for i in range(n):
#         if s[i] != s[-i - 1]:
#             return False
#     return True
#
# s = input("Введите строку для проверки: ")
# print(palindrome(s))

# # For a test
# "    aBC cba " # True
# "a BCQcb a    " # True
# " ab bca"  # False