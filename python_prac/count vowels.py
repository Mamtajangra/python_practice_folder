# define a function 
def count_vowels(n):
    # suppose total vowels are 0 
    count = 0
    vowels = "aeiouAEIOU"
    # loop over the entire string 
    for i in n:
        # check each letter belongs to vowels 
        if i in vowels:
            # count increases if letter belongs to vowel 
            count = count + 1

# return 
    return count
# check how many vowels are in helloworld 
print(count_vowels("helloworld"))       
