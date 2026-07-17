num=int(input("give the number you want to cheack the even or odd: "))
if num%2==0:
  print("this is even number")
else:
  print("this is odd number")

height = int(input("tall me your height in cm: "))
if height >= 120:
  print("you can ride the rollercoaster")
  price=0
  imag=input("do you wan photo on the rollercoaster say 'yes' or 'no'!: ")
  if imag.casefold() == "YES".casefold():
    price+=3
  age=int(input("how old are you: "))
  if age <= 12:
    print(f"pay ${5+price} and go to the rollercoaster! \n thank you for coming!")
  elif age <= 18:
    print(f"pay ${7+price} and go to the garollercoasterme! \n thank you for coming!")
  else:
    print(f"pay $1{2+price} and go to the rollercoaster! \n thank you for coming!")
else:
  print("your hight was lower than the expacted hight sorry to tall you this")


              the good way of doint this work was 
height = int(input("Tell me your height in cm: "))
if height >= 120:
  print("You can ride the rollercoaster!")
  price = 0 
  imag = input("Do you want a photo? (yes/no): ")
  if imag.casefold() == "yes":
    price += 3
  age = int(input("How old are you: "))
  if age <= 12:
    total = 5 + price
  elif age <= 18:
    total = 7 + price
  else:
    total = 12 + price
  print(f"Pay ${total} and go to the rollercoaster!")
  print("Thank you for coming!")
else:
  print("Sorry, you are too short to ride!")

  

height=float(input("tall me your hight in m: "))
mass=float(input("tall me your mass kg: "))
bmi=mass/(height**2)
if bmi<18.5:
  print(f"you are Underweight in bmi of {round(bmi,2)}") 
elif bmi<24.9:
  print(f"you are Healthy / Normal Weight in bmi of {round(bmi,2)}")
else:
  print(f"you are Obesity in bmi of {round(bmi,2)}")
  
print("Welcome to pythone pizza Deliveries! ")
size = input("what size pizza do you want? S, M or L?: ")
papperoni=input("Do you wan paperoni in your pizza (y/n)?: ")
extra_cheese = input("Do you wan extra chees?(y/n): ")
chees=0
bill=0
if size.capitalize() == "S":
  bill += 15
elif size.capitalize() == "M":
  bill += 20
elif size.capitalize() == "L":
  bill += 25
else:
  print("you typed the wrong inputs.") 
if papperoni.capitalize()=="Y" and size.capitalize() == "S" :
  pap=2
elif papperoni.capitalize()=="Y" and (size.capitalize() == "M" or size.capitalize() == "L") :
  pap=3
else:
  pap=0
if extra_cheese.capitalize() == "Y":
  chees+=1
print(f"your final bill is: ${bill+pap+chees}.")



              the good way of doint this work was 
print("Welcome to pythone pizza Deliveries! ")
size = input("what size pizza do you want? S, M or L?: ")
papperoni=input("Do you wan paperoni in your pizza (y/n)?: ")
extra_cheese = input("Do you wan extra chees?(y/n): ")

chees=0
bill=0
valid_pizza = True 

if size.capitalize() == "S":
  bill += 15
elif size.capitalize() == "M":
  bill += 20
elif size.capitalize() == "L":
  bill += 25
else:
  print("You typed the wrong inputs.") 
  valid_pizza = False

if valid_pizza:
  if papperoni.capitalize()=="Y" and size.capitalize() == "S" :
    pap=2
  elif papperoni.capitalize()=="Y" and (size.capitalize() == "M" or size.capitalize() == "L") :
    pap=3
  else:
    pap=0

  if extra_cheese.capitalize() == "Y":
    chees+=1

  print(f"your final bill is: ${bill+pap+chees}.")


