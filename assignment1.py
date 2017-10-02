# Assignment 1
# Created by: Chris Karpinski
# Created for: COMP1005A
# Created on: September 2017
# This program converts between units of various quantities

# below defining a list of constants for unit conversions (conversion factors)

KELVIN_TO_CELSIUS = 273.15
METER_PER_SECOND_TO_KM_PER_HOUR = 3.6
KILOCALORIES_TO_JOULES = 4184
LIGHT_YEARS_TO_PARSECS = 0.30661
ACRES_TO_SQUARE_METERS = 4046.86
GALLONS_TO_LITRES = 3.78541
PSI_TO_PASCALS = 6894.76
POUNDS_TO_KILOGRAMS = 2.2


# below (options 1 to 10) are functions for carrying out each unit conversion
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
        
    return letter    

def option2(kelvinTemp): 
    
    celsiusTemp = kelvinTemp - KELVIN_TO_CELSIUS
    
    return celsiusTemp
 
def option3(meterPerSecondSpeed): 
    
    kilometerPerHourSpeed = meterPerSecondSpeed*METER_PER_SECOND_TO_KM_PER_HOUR
    
    return kilometerPerHourSpeed

def option4(kiloCalories): 
    
    joule = kiloCalories*KILOCALORIES_TO_JOULES
    
    return joule

def option5(lightYearDistance): 
    
    parsecDistance = lightYearDistance*LIGHT_YEARS_TO_PARSECS
    
    return parsecDistance

def option6(decimalValue):
    
    binaryValue = bin(decimalValue)
        
    return binaryValue

def option7(acres):
    
    squareMeters = acres*ACRES_TO_SQUARE_METERS
        
    return squareMeters

def option8(gallons):
    
    litres = gallons*GALLONS_TO_LITRES
        
    return litres

def option9(psi):
    
    pascals = psi*PSI_TO_PASCALS
        
    return pascals

def option10(pounds):
    
    kilograms = pounds/POUNDS_TO_KILOGRAMS
        
    return kilograms


# this function below handles all numerical input values for each conversion 
# and makes sure there is no error in user input
def handleError(inputString, minVal = float("-inf"), maxVal = float("inf"), intRequired = False): 
    # input validation function to be used to verify all numerical inputs
    # and catch exceptions
    
    validOption = False # validOption records if the input is valid
    
    while(not validOption): 
        # keep asking for the user to validate their input until the input is valid
        try:
            # using a try, catch (try, except) to catch a string being inputed
            # for a numerical value
            numericalValue = float(input(inputString))
             
            if numericalValue < minVal or numericalValue > maxVal: 
                # if the input is outside the allowed numerical range, 
                # tell the user to re-input it in the correct range
                print("Please enter a value between " + str(minVal) + " and " + str(maxVal))
                validOption = False
            elif intRequired and (numericalValue != int(numericalValue)): 
                # if the input is not an integer, (for the binary to decimal conversion), tell the user to input a non-negative integer
                print("Please enter an integer")
                validOption = False                
            else: 
                if intRequired:
                    return int(numericalValue) # return an int if an integer is required (for decimal to binary conversion)
                else: 
                    return numericalValue # otherwise, just return the float value
            
        except: 
            # ask the user to re-input a value if it is non-numerical
            print ("Please enter a numerical value")
            validOption = False

name = input("Please enter your name: ") # ask for the user's name

# present all the options for the user to select
print("Hello", name + ". Welcome to your personal unit converter!", end = "\n\n")

while True: 
    print("Please choose one of the following unit conversions: ", end = "\n\n")
    print("1: Convert percent to letter grade")
    print("2: Convert Kelvin to Celsius")
    print("3: Convert m/s to km/hour")
    print("4: Convert kilocalories to joules")
    print("5: Convert light years to parsecs")
    print("6: Convert decimal to binary")
    print("7: Convert acres to square meters")
    print("8: Convert gallons to litres")
    print("9: Convert PSI (Pounds per square inch) to Pascals")
    print("10: Convert pounds to kilograms", end = "\n\n")
    option = input("Select which number conversion you would like: ")
    
    # below (options 1 to 10) send off the required arguments for the unit conversion 
    # (i.e. string saying what to input, the allowed range of inputs, and that the input
    # must be an integer for binary)
    if option == "1": 
        
        inputArg = handleError("Enter the percent grade: ", 0, 100)
        print(inputArg, "%", "is an", option1(inputArg))
        
    elif option == "2": 
        
        inputArg = handleError("Enter the kelvin temperature: ", minVal = 0)
        print(inputArg, "Kelvin", "is", option2(inputArg), "degrees Celsius")        
        
    elif option == "3": 
        
        inputArg = handleError("Enter the speed in m/s: ", minVal = 0)
        print(inputArg, "m/s", "is", option3(inputArg), "km/hour")        
        
    elif option == "4": 
    
        inputArg = handleError("Enter the energy in kiloCalories: ", minVal = 0)
        print(inputArg, "kilocalories", "is", option4(inputArg), "joules")        
        
    elif option == "5":
        
        inputArg = handleError("Enter the distance in light years: ", minVal = 0)
        print(inputArg, "light-years", "is", option5(inputArg), "parsecs")        
        
    elif option == "6": 
        
        inputArg = handleError("Enter a non-negative integer decimal value: ", minVal = 0 ,intRequired = True)
        print(inputArg, "in decimal", "is", option6(inputArg), "in binary")        
        
    elif option == "7":
    
        inputArg = handleError("Enter the area in acres: ", minVal = 0)
        print(inputArg, "acres", "is", option7(inputArg), "meters squared")         
        
    elif option == "8": 
    
        inputArg = handleError("Enter the number of gallons: ", minVal = 0)
        print(inputArg, "gallons", "is", option8(inputArg), "litres")        
    
        
    elif option == "9": 
       
        inputArg = handleError("Enter the volume in PSI (Pounds per Square Inch): ", minVal = 0)
        print(inputArg, "PSI (pounds per square inch)", "is", option9(inputArg), "pascals")  
        
    elif option == "10":
        
        inputArg = handleError("Enter the mass in pounds: ", minVal = 0)
        print(inputArg, "pounds", "is", option10(inputArg), "kilograms")            
        
    else: 
        # if a valid option for unit conversion was not selected, ask to re-select
        print("Invalid input. Please re-select an option.")
        continue
        
    # close the program with a goodbye message    
    print()
    print("-------------------------------------------------", end = "\n\n")
    print("Goodbye,", name + ". Thank you for using unit converter!")
    break







