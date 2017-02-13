# -*- coding: utf-8 -*-


import sys

args = sys.argv



num_ppl = int(args[1])
cards = args[2]

print num_ppl
print cards

arr = ['']*num_ppl
# init array
#for index in range(0, num_ppl - 1):
#    print index
#    arr[index] = ''



keisu = 0
length_cards = len(cards)
# fill array
for i,v in enumerate(cards):


    if i % num_ppl == 0:
        keisu = keisu + 1
        if length_cards - i < num_ppl:
            break
    rap = num_ppl * keisu
    arr[i - rap] =  arr[i - rap] + str(v)




print arr






