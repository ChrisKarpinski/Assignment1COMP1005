# Assignment 1
# Created by: Chris Karpinski
# Created for: COMP1005A
# Created on: September 16, 2017
# This program converts between various units of quantities


def option1(percentGrade):
    
    if percentGrade <= 100 and percentGrade >= 80: 
        letter = "A"
    elif percentGrade < 80 and percentGrade >= 70:
        letter = "B"
    elif percentGrade < 70 and percentGrade >= 60: 
        letter = "C"
    elif percentGrade < 60 and percentGrade >= 50:
        letter = "D"
    else: 
        letter = "F"
        
    return str(percentGrade) + "% is an " + letter    

def option2(kelvinTemp): 
    
    celsiusTemp = kelvinTemp - 273.15
    
    return "The kelvin temperature: " + str(kelvinTemp) + " is " + str(celsiusTemp) + " degrees Celsius."
 
def option3(meterPerSecondSpeed): 
    
    kilometerPerHourSpeed = meterPerSecondSpeed*3.6
    
    return str(metersPerSecondSpeed) + " m/s is " + str(kilometerPerHourSpeed) + " in km/hour."

def option4(usDollarValue): 
    
    chineseYuanValue = usDollarValue*6.55
    
    return str(usDollarValue) + " USD is " + str(chineseYuanValue) + " in Chinese Yuan."

def option5(lightYearDistance): 
    
    parsecDistance = lightYearDistance*0.30661
    
    return str(lightYearDistance) + " lightyears is " + str(parsecDistance) + " parsecs."

def option6(binaryValue):
    
    decimalValue = 0
    for i in range(len(binaryValue)-1): 
        decimalValue = decimalValue + 2^i * int(binaryValue[len(binaryValue) - 1 - i])
        
    return binaryValue + " in binary is " + str(decimalValue) + " in decimal (base 10)."


def handleError(minVal, maxVal, inputString): 
    # input validation function to be used to verify all numerical inputs
    # and catch exceptions
    validOption = False
    
    while(not validOption): 
        
        try: 
            numericalValue = float(input(inputString))
            if numericalValue < minVal or numericalValue > maxVal: 
                print("Please enter a value between " + str(minVal) + " and " + str(maxVal))
                validOption = False
            else: 
                return numericalValue
        except: 
            print ("Please enter a numerical value")
            validOption = False
            # could have also tried if (type(numericalValue) == float) for error
#def handleError(minVal, inputString): 
    




name = input("Please enter your name: ")

print("Hello", name + ". Welcome to your personal unit converter!", end = "\n\n")
print("Please choose one of the following unit conversions: ", end = "\n\n")
print("1: Convert percent to letter grade")
print("2: Convert Kelvin to Celsius")
print("3: Convert m/s to km/hour")
print("4: Convert US dollars to Chinese Yuan")
print("5: Convert light years to parsecs")
print("6: Convert binary decimal")
print("7: Convert acres to square meters")
print("8: Convert gallons to litres")
print("9: Convert PSI (Pounds per square inch) to Pascals")
print("10: Convert pounds to kilograms", end = "\n\n")
option = input("Select which number conversion you would like: ")

if option == "1": 
    
    #
    #validOption = False
    
   # while (not validOption): 
        # this while loop combined with the try and except sequence validates user input
       # try :
         #   gradePercent = float(input("Enter the percent grade: "))
           # if gradePercent < 0 or gradePercent > 100: 
            #    print ("Please enter a value between 0 and 100")
             #   validOption = False
           # else:    
            #    validOption = True
      #  except : 
           # print ("Please enter a numerical value.")
           # validOption = False

    print(option1(handleError(0, 100, "Enter the percent grade: ")))
    
elif option == "2": 
    
    print(option2(handleError(0, "Enter the kelvin temperature")))
    
elif option == "3": 
    meterPerSecond = input("Enter the speed in m/s: ")
    print(option3(handleError(0, "Enter the speed in m/s")))
    
elif option == "4": 
    usDollar = input("Enter the amount in USD(US dollars): ")
    print(option4(float(usDollar)))
    
elif option == "5":
    lightYear = input("Enter the distance in light years: ")
    print(option5(float(lightYear)))
    
elif option == "6": 
    binaryInt = input("Enter the binary value: ")
    print(option6(str(binaryInt)))
    
elif option == "7":
    acreDistance = input("Enter the distance in acres: ")
    print (option7(float(acreDistance)))
    
elif option == "8": 
    gallonVolume = input("Enter the number of gallons: ")
    print (option8(float(gallonVolume)))
    
elif option == "9": 
    psiValue = input("Enter the volume in PSI (Pounds per Square Inch): ")
    print (option9(float(psiValue)))
    
else: 
    print("Invalid input, terminated.....")
    
print()
print("-------------------------------------------------", end = "\n\n")
print("Goodbye,", name + ". Thank you for using unit converter!")











