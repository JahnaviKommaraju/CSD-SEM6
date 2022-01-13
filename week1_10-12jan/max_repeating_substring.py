# def maxRepeating(sequence,word):
#     count=0
#     for i in range(len(sequence)+1):
#         if word*i in sequence:
#             count=i
#     return count

sequence=input()
word=input()
print(sequence.count(word))
# print(maxRepeating(sequence,word))