import inflect
p = inflect.engine()

name = [] ; mylist =[]

try :
    while True :
        name.append(input("Name: \n").capitalize())
        print()

except EOFError :

    mylist = p.join((name))

    print("Adieu, adieu, to ", end="")

    for i in range(len(mylist)) :
        print(mylist[i], end="")

    print()
