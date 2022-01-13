import collections
def palin_anagram(s):
    c = collections.Counter(s)
    count = 0
    for i in c.values():
        if i % 2 != 0:
            if count == 0:
                count += 1
                continue
            return False
    return True

print(palin_anagram(input()))

#carrace
# {'c':2,
# 'a':2,
# 'r':2,
# 'e':1}
# c=0 1
# i=2 2 2 1
# true
# If count of the alphabet is odd viz. 'e' in "racecar" 
# then there should be only one alphabet that can be odd.
#  If all counts are even then it can be used to from a palindrome.


