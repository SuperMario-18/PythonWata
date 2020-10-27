




chicken = 23
goat = 678
pig = 1296
cow = 3848
sheep = 6769
money = int(input())
if money == 23:
    print("1 Chicken")
elif 23 < money < 678:
    print(money//chicken, "Chickens")
elif money == 678:
    print("1 Goat")
elif 678 < money < 1296:
    print(money//goat, "Goats")
elif money == 1296:
    print("1 pig")
elif 1296 < money < 3848:
    print(money//pig, "Pigs")
elif money == 3848:
    print("1 Cow")
elif 3848 < money < 6769:
    print(money//cow, "Cows")
elif money == 6769:
    print("1 Sheep")
else:
    print(money//sheep, "Sheep")


