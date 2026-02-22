import random as ra
import time as t
def main():
    what_to_do = input("Let's check the leaderboard! W (Write in a name) / R (Read out the names)")
    if what_to_do.lower() == "w":
        write()
    elif what_to_do.lower() == "r":
        read_previous_best_nums()
def write():
    topTen = input("Who are the people at the top ten? (Separate with spaces) ")
    topTen = topTen.split(" ")
    f1 = open("peopleOn.txt", "w")
    for i in topTen:
        f1.write(str(f"{i}\n"))
    f1.close()
    repeat = 10
    while repeat > 0:
        new_num=ra.randint(1,999)
        if new_num in best_nums:
            new_num=ra.randint(1,999)
        good_num = input(f"Is {new_num} who should go with this number?  ")
        good_num = good_num.lower()
        best_nums.append(new_num)
        repeat -= 1
    print("Now writing to a file, your best numbers...")
    f=open("scores.txt", "w")
    f2 = open("peopleOn.txt", "w")
    for i in good_num:
        f2.write((f"{i}\n"))
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

best_nums = [1,2,3,4,5,6,7,8,9,10]
print(best_nums)
main()



