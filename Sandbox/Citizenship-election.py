###if the person is citizen and the if yes then ask the age if over 18+ "you are eligible for voting"###
citizenship = input("Are you a citizen? ")
if citizenship == "yes":
    age = int(input("Enter your age: "))
    if age >= 18:
        print("You can vote")
    else:
        print("You cannot vote because you are underage")
else: 
    print("Not eligible")




    
    