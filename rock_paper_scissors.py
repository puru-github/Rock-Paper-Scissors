import random
you = input("Your turn : rock(r), paper(p), scissor(s)?\n")

li  = ["r", "p", "s"]
comp = random.choice(li)

if comp == "s" and you == "p":
    print("you loose")
elif comp == "s"  and you == "r":
    print("you win")
elif comp == "r" and you == "p":
    print("you win")
elif comp == "r" and you == "s":
    print("you loose")
elif comp == "p" and you == "r":
    print("you loose")
elif comp == "p" and you == "s":
    print("you win")
elif comp == you:
    print("it'a tie ")
else:
    print("press right keyword")
print(f"computer choose {comp}")






