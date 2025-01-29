weight= int(input("Enter your weight: "))
height =int(input("Enter your height: "))
bmi = weight/(height**2)
print("Your BMI :"+str(bmi))
if bmi < 16:
           print("Sever Thiness") 
elif bmi > 16 and bmi < 18.5:
            print("Under Weight")
elif bmi > 18.5 and bmi < 25:
            print("Normal")
elif bmi > 25 and bmi < 30:
            print("Over Weight")
else:
            print("Obese")

    