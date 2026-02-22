def test_one(list_of_strings_one,list_of_strings_two):
    len_list_of_strings_one = len(list_of_strings_one)
    len_list_of_strings_two = len(list_of_strings_two)
    if len_list_of_strings_one == len_list_of_strings_two or len_list_of_strings_one + 2 == len_list_of_strings_two or len_list_of_strings_one - 2 == len_list_of_strings_two or len_list_of_strings_one + 1 == len_list_of_strings_two or len_list_of_strings_one -1 == len_list_of_strings_two:
        print(len_list_of_strings_one, len_list_of_strings_two)
        print("Test one passed, strings are the same length")
        test_two(list_of_strings_one,list_of_strings_two, len_list_of_strings_one, len_list_of_strings_two)


def test_two(list_of_strings_one,list_of_strings_two, len_list_of_strings_one, len_list_of_strings_two):
        sort_list_of_strings_one = sorted(list_of_strings_one)
        sort_list_of_strings_two = sorted(list_of_strings_two)
        
        print(sort_list_of_strings_one, sort_list_of_strings_two)
        if sort_list_of_strings_one == sort_list_of_strings_two:
            print("\n\nTest two passed, strings are anagrams")



input_one = input("Enter a string separated by ' ' ")
input_two = input("Can you actually enter another one the same way? It'll be cool... I hope... ")
list_of_strings_one = input_one.split(" ")
list_of_strings_two = input_two.split(" ")
print(list_of_strings_one,list_of_strings_two)
test_one(list_of_strings_one,list_of_strings_two)