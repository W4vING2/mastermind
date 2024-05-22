import random

count = 0
point_wd = 0
point_wf = 0
colours = ["red", "yellow", "green", "brown", "blue", "black", "white", "gray", "purple", "pink"]

c1 = random.choice(colours)
c2 = random.choice(colours)
c3 = random.choice(colours)
c4 = random.choice(colours)
newcolour = [c1, c2, c3, c4]

print(colours)
print("guess my combination of colours")
choice1 = input("1-st colour?: ")
choice2 = input("2-nd colour?: ")
choice3 = input("3-rd colour?: ")
choice4 = input("4-th colour?: ")
choice4 = choice4.lower()
choice1 = choice1.lower()
choice3 = choice3.lower()
choice2 = choice2.lower()

again = True
while again == True:
    if choice1 == newcolour[0] and choice2 == newcolour[1] and choice3 == newcolour[2] and choice4 == newcolour[3]:
        print("well done")
        again = False
    else:
        if choice1 == newcolour[0]:
            point_wd = point_wd + 1
        elif choice1 == newcolour[1]:
            point_wf = point_wf + 1
        elif choice1 == newcolour[2]:
            point_wf = point_wf + 1
        elif choice1 == newcolour[3]:
            point_wf = point_wf + 1

        if choice2 == newcolour[0]:
            point_wf = point_wf + 1
        elif choice2 == newcolour[1]:
            point_wd = point_wd + 1
        elif choice2 == newcolour[2]:
            point_wf = point_wf + 1
        elif choice2 == newcolour[3]:
            point_wf = point_wf + 1

        if choice3 == newcolour[0]:
            point_wf = point_wf + 1
        elif choice3 == newcolour[1]:
            point_wf = point_wf + 1
        elif choice3 == newcolour[2]:
            point_wd = point_wd + 1
        elif choice3 == newcolour[3]:
            point_wf = point_wf + 1

        if choice4 == newcolour[0]:
            point_wf = point_wf + 1
        elif choice4 == newcolour[1]:
            point_wf = point_wf + 1
        elif choice4 == newcolour[2]:
            point_wf = point_wf + 1
        elif choice4 == newcolour[3]:
            point_wd = point_wd + 1

        print(point_wd, "right colour on the right position", point_wf, "right colour on the incorrect position")
        print("try again")
        choice1 = input("1-st colour?: ")
        choice2 = input("2-nd colour?: ")
        choice3 = input("3-rd colour?: ")
        choice4 = input("4-th colour?: ")
    count = count + 1
    point_wf = 0
    point_wd = 0
print(count, "attempts")
print("see ya")


