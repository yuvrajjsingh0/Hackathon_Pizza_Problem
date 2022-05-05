import sys
sys.stdin = open('data/a_an_example.in.txt', 'r')
#sys.stdin = open('data/b_basic.in.txt', 'r')
#sys.stdin = open('data/c_coarse.in.txt', 'r')
#sys.stdin = open('data/d_difficult.in.txt', 'r')
#sys.stdin = open('data/e_elaborate.in.txt', 'r')

n = int(input())
n *= 2
itemsToBeIncluded = []
itemsNotToBeIncluded = []
for i in range(n):
    if i%2 == 0:
        continue
    likes = input().split(' ')
    dislikes = input().split(' ')
    num_likes = int(likes.pop(0))
    num_dislikes = int(dislikes.pop(0))
    
    itemsToBeIncluded += likes
    itemsNotToBeIncluded += dislikes
    

for item in itemsNotToBeIncluded:
  if item in itemsToBeIncluded:
    itemsToBeIncluded.remove(item)
    
itemsToBeIncluded = list(dict.fromkeys(itemsToBeIncluded))

finalRet = str(len(itemsToBeIncluded)) + " "

for item in itemsToBeIncluded:
  finalRet += item + " "

print(finalRet)
