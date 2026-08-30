gender = input("Enter your gender: ").lower()

if gender != "male" and gender !="female":
    print("Invalid input")
else:
    hemoglobin = int(input("Enter your value g/l: "))
    if gender == "female":
        if hemoglobin < 117:
            print("Your hemoglobin value is low")
        elif 117 <= hemoglobin <= 155:
            print("Your hemoglobin value is normal")
        elif  hemoglobin > 155:
             print("Your hemoglobin value is high")

    elif gender == "male":
        if hemoglobin < 134:
            print("Your hemoglobin level is low")
        elif 134 <= hemoglobin <= 167:
            print("Your hemoglobin value is normal")
        elif  hemoglobin > 167:
            print("Your hemoglobin value is high")
