# define a function 
def palindrome(n):
    # check the condition 
    if n == n[::-1]:
         return "yes palindrome"
    else:
         return "no palindrome"
#   to check via example   
print(palindrome("racecar"))