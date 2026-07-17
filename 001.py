print("Welcome to the tip calculator!")
total= float(input("what was the Total bill? $"))
tip_per= float(input("How much tip would you like to give? 10, 12, or 15? "))
split=int(input("How many peopl to split the bill? "))
total_mony= (total + (tip_per*0.01*total))/split
print(f"Each person should pay: ${str(round(total_mony,2))}")
