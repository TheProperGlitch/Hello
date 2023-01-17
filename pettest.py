def petest():
    color = input("What color is the pet: ")
    kind = input("What kind of animal is the pet: ")
    name = input("What is the name of the pet: ")
    print(f"Your pet is a {color} {kind} named {name}.")

def notest():
    ogstring = input("gib string: ")
    exitstring = ""
    for word in ogstring.split(" "):
        if word == "is":
            exitstring += "is not "
        else:
            exitstring += f"{word} "
    print(exitstring)

def initals():
    ogstring = input("gib name: ")
    exitstring = ""
    for word in ogstring.split(" "):
        exitstring += f"{word[0]}."
    print(exitstring)

def graduate():
    grade = int(input("Gib grade: "))
    print(f"You have {13 - grade} years left to graduate.")
    



choice = input("(p)et test, (n)ot test, (i)nitials, (g)raduate: ")
if choice == "p":
    petest()
elif choice == "n":
    notest()
elif choice == "i":
    initals()
elif choice == "g":
    graduate()
