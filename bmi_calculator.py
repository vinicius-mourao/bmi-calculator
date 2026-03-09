# importing the necessary library for plotting
import matplotlib.pyplot as plt

# Creating function to calculate BMI
def bmiCalculator(weight, height):
    bmi = weight / (height ** 2)
    return bmi

# Creating function to determine BMI category based on calculated BMI
def bmiCategory(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    elif 30 <= bmi < 35:
        return "Obesity Class I"
    elif 35 <= bmi < 40:
        return "Obesity Class II"
    elif bmi >= 40:
        return "Obesity Class III"
    else: return "Invalid BMI"

# Creating function to plot BMI categories and indicate user's BMI on the graph
def plotBMICategories(bmi):
    plt.axvspan(0, 18.5, 0.0, 1.0, color='blue', alpha=0.5, label='Underweight')
    plt.axvspan(18.5, 25, 0.0, 1.0, color='green', alpha=0.5, label='Normal weight')
    plt.axvspan(25, 30, 0.0, 1.0, color='yellow', alpha=0.5, label='Overweight')
    plt.axvspan(30, 35, 0.0, 1.0, color='orange', alpha=0.5, label='Obesity Class I')
    plt.axvspan(35, 40, 0.0, 1.0, color='red', alpha=0.5, label='Obesity Class II')
    plt.axvspan(40, 50, 0.0, 1.0, color='darkred', alpha=0.5, label='Obesity Class III')
    plt.xlabel('BMI')
    plt.title('BMI Categories')
    plt.axvline(x = bmi, color = 'black', linestyle = '--', label='Your BMI')
    plt.legend()


# Creating function to request user input for weight and height, with error handling for invalid inputs and ensuring that weight and height are positive numbers. Also, if height is entered in centimeters, it converts it to meters.
def requestInput():
    print("Welcome to the BMI Calculator!")
    try: 
        weight = float(input("Write your weight in kg: "))
        height = float(input("Write your height in meters: "))
    except ValueError:
        print("Invalid input. Please enter numeric values for weight and height.")
        return None
    if weight <= 0 or height <= 0:
        print("Weight and height must be positive numbers.")
        return
    if height > 3:
        height = height / 100
    return weight, height



# Creating and running main function to execute the BMI calculation, category determination, and plotting of BMI categories based on user input.
def main():
    result = requestInput()
    if result is None:
        return
    weight, height = result
    bmi = bmiCalculator(weight, height)
    category = bmiCategory(bmi)
    print("Your BMI is: ", round(bmi, 2))
    print("Your BMI category is: ", category)
    plotBMICategories(bmi)
    plt.yticks([])
    plt.show()
main()
