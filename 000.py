#day 1

print( "th")

print("Hellow " + input("what is your name: ")+ " i hope you are doing well" )

print(f"{len(input("what is your name: "))} this was your name caractour")

print("Wellcome to the Band Name Generater.")
print("what is the name of the city you grew up in?")       #or  print("what is the name of the city you grew up in?\n")
city=input()
print("what is your pet's name?")
pet=input()
print("Your band name could be " + city + " " + pet)



first_numbe = int(input())
out = []

for _ in range(first_numbe):
    item = input().replace(" ", "")
    if len(item) == 4 and item.isdigit() and item[0] == item[1] == item[2] == item[3]:
        out.append("YES")
    else:
        out.append("NO")

print("this was the out put")
for result in out:
    print(result)
    