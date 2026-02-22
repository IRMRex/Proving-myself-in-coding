import random as ra
import time as t
def main():
    what_to_do = input("Do you want to make a new set of great numbers, read them, or erase? w/r/e ")
    if what_to_do.lower() == "w":
        write()
    elif what_to_do.lower() == "r":
        read_previous_best_nums()
    elif what_to_do.lower() == "e":
        erase()
def write():
    repeat = 10
    while repeat > 0:
        new_num=ra.randint(1,999)
        if new_num in best_nums:
            new_num=ra.randint(1,999)
        good_num = input(f"Is {new_num} a good number? (y/n) ")
        good_num = good_num.lower()
        if good_num == "y":
            best_nums.append(new_num)
            print(best_nums)
        elif good_num == "n":
            print("New Num!!")
        repeat -= 1
    print("Now writing to a file, your best numbers...")
    f=open("scores.txt", "w")
    for i in best_nums:
        f.write(str(f"{i}\n"))
    f.close()
    main()
def read_previous_best_nums():
    print("Reading previous best numbers...")
    t.sleep(1)
    f = open("scores.txt", 'r')
    print(f.read())
    f.close()
    main()

def erase():
    print("Erasing all previous best numbers...")
    f = open("scores.txt", "w")
    f.write("")
    f.close()
    main()
best_nums = [849,288,207,910,999,67,45,888,100]
print(best_nums)
main()



