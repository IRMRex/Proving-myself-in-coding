import time as t #debug
list_of_nums = [8,2,9,5,8,1,5,0,9,7,9,9,1,6,2,8,1,8,4,0,1,4,8,9,2,0,9,5,2,1,0,4,1,7,5,4,2,4,9,4,8,1,8,6,1,8,9,3,8,0,2,4,2,1,3,1,5,2,8,5,9,9,7,0,4,9,9,1,4,0,8,8,4,2,5,6,6,4,7,4,2,0,3,5,1,2,8,5,2,4,1,1,5,4,6,1,6,2,9,3]# added commas to make it into a proper list.
len_list_of_nums = len(list_of_nums) #grab the length of the list
sorted_list=[]
alphabetized_list=[]
numbers_in_alpha = [8, 5,4,9,1, 7, 6, 3, 2, 0]
for i in range(len_list_of_nums):
    sorted_list=sorted(list_of_nums)
    eights = list_of_nums.count(8)
    fives = list_of_nums.count(5)
    fours = list_of_nums.count(4)
    nines = list_of_nums.count(9)
    ones = list_of_nums.count(1)
    sevens = list_of_nums.count(7)
    sixes = list_of_nums.count(6)
    threes = list_of_nums.count(3)
    twos = list_of_nums.count(2)
    zeros = list_of_nums.count(0)
    #this is the first way that i thought to do it. Sorry is not good. Also, I just didn't want to write out each number so i just used the number number. In can be edited if needed but it functionally works the same
while eights > 0:
    alphabetized_list.append(8)
    eights -= 1
while fives > 0:
    alphabetized_list.append(5)
    fives -= 1
while fours > 0:
    alphabetized_list.append(4)
    fours -= 1
while nines > 0:
    alphabetized_list.append(9)
    nines -= 1
while ones > 0:
    alphabetized_list.append(1)
    ones -= 1
while sevens > 0:
    alphabetized_list.append(7)
    sevens -= 1
while sixes > 0:
    alphabetized_list.append(6)
    sixes -= 1
while threes > 0:
    alphabetized_list.append(3)
    threes -= 1
while twos > 0:
    alphabetized_list.append(2)
    twos -= 1
while zeros > 0:
    alphabetized_list.append(0)
    zeros -= 1
print(sorted_list)
print("\n\nTime to alphabetize (hehe) \n\n")
print(alphabetized_list)
