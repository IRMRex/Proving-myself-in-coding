import random as r
str_one = input("Enter a string with eight words ")
list_of_str_one = list(str_one)
print(list_of_str_one)
len_list_of_str_one = len(list_of_str_one)
print(len_list_of_str_one)
char_one = list_of_str_one[0]
index_of_space_one = list_of_str_one.index(" ")
char_two = list_of_str_one[index_of_space_one + 1]
print(char_one, char_two)
list_of_str_one.pop(index_of_space_one)
index_of_space_two = list_of_str_one.index(" ")
char_three = list_of_str_one[index_of_space_two + 1]
print(char_three)
list_of_str_one.pop(index_of_space_two)
index_of_space_three = list_of_str_one.index(" ")
char_four = list_of_str_one[index_of_space_three + 1]
print(char_four)
list_of_str_one.pop(index_of_space_three)
index_of_space_four = list_of_str_one.index(" ")
char_five = list_of_str_one[index_of_space_four + 1]
print(char_five)
list_of_str_one.pop(index_of_space_four)
index_of_space_five = list_of_str_one.index(" ")
char_six = list_of_str_one[index_of_space_five + 1]
print(char_six)
list_of_str_one.pop(index_of_space_five)
index_of_space_six = list_of_str_one.index(" ")
char_seven = list_of_str_one[index_of_space_six + 1]
print(char_seven)
list_of_str_one.pop(index_of_space_six)
index_of_space_seven = list_of_str_one.index(" ")
char_eight = list_of_str_one[index_of_space_seven + 1]
print(char_eight)
list_of_str_one.pop(index_of_space_seven)
print(char_one, char_two, char_three, char_four, char_five, char_six, char_seven, char_eight)

list_of_chars = [char_one, char_two, char_three, char_four, char_five, char_six, char_seven, char_eight]

len_list_of_chars = len(list_of_chars)
len_len_list_of_chars = len_list_of_chars - 1

cap_list_of_chars = []
r.randint(0,1)
for i in range(len_list_of_chars):
    if r.randint(0,1) == 0:
        cap_list_of_chars.append(list_of_chars[i].upper())
    else:
        cap_list_of_chars.append(list_of_chars[i])

print(cap_list_of_chars)

#hello my name is Ian and I code

print(list_of_str_one)