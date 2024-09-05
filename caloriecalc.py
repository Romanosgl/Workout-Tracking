


# Katch-McArdle multiplier needed for total daily energy expenditure(TDEE)
McArdle_multiplier = {
    "Sedentary": 1.2,
    "Lightly Active": 1.375,
    "Moderately Active": 1.55,
    "Very Active": 1.725,
    "Extremely Active": 1.9
}


def personal_data():
    while True:
        print('Enter your age(years):')
        age = input()
        try:
            age = int(age)
        except:
            print('Please use numeric digits.')
            continue
        if age < 1:
            print('Please enter a positive number.')
            continue
        break
    while True:
        gender = input("Choose male or female: ")
        gender = gender.upper()
        if gender == "MALE" or gender == "FEMALE":
            break
        else:
            continue
    while True:
        weight = input("Please input your weight in kg:")
        try:
            weight = int(weight)
        except:
            print("Please use numeric digits.")
            continue
        if weight < 1:
            print("Please provide a positive number.")
            continue
        break
    while True:
        height = input("Plese input your height in cm: ")
        try:
            height = int(height)
        except:
            print("Please use numeric digits.")
            continue
        if weight < 1:
            print("Please provide a positive number.")
            continue  
        break
    return height,weight,age,gender

def find_bmr(gender,height,age,weight):
    if gender == "MALE":
        BMR = (10 * weight) + (6.25 * height) - (5 * age) + 5
        return BMR
    elif gender == "FEMALE":
        BMR = (10 * weight) + (6.25 * height) - (5 * age) - 161
        return BMR

def find_activity_level():
    while True:
        print("Choose your activity level from:\n Sedentary(little to no exercise)\n Lighly Active(exercise 1-3times/week)\n Moderately Active(3-5times/week)\n Very Active(Heavy Exercise6-7 times/week\n Extremely Active(strenuous training 2x/day)")
        activity_level = input()
        if activity_level in McArdle_multiplier:
            break
        else:
            print("Please choose a valid activity level.")
            continue    
    return activity_level

#Find Total Daily Energy Expenditure
def find_tdee(bmr,activity_level):
    multiplier = McArdle_multiplier.get(activity_level, 1.2)  # Default to Sedentary if not found
    TDEE = bmr * multiplier
    return TDEE

def find_weight_goal(weight):
    while True:    
        goal_weight = input("What is your desired goal weight:")
        try:
            goal_weight = int(goal_weight)
        except:
            print("Please use numeric digits.")
            continue
        if goal_weight < 1:
            print("Please provide a positive number")
            continue
        break
    
    net_weight = goal_weight - weight
    if net_weight == 0:
        print("Your current weight is already your goal weight.")
        return 0
        
    while True: 
        loss_pace = input("How much weight do you plan to lose per week(Choose from:0.25kg, 0.5kg and 1kg) ")
        if loss_pace not in ["0.25", "0.5", "1"]:
            print("Please choose one of the above three options.")
            continue
        loss_pace = float(loss_pace)
        break
    loss_date = net_weight / loss_pace #in weeks (should add abs() if planning to use the same function for gain)
    return loss_date
    
if __name__ == "__main__":
    height, weight, age, gender = personal_data()
    bmr = find_bmr(gender, height, age, weight)
    print(f"Your BMR is: {bmr}")
    activity_level = find_activity_level()
    tdee = find_tdee(bmr, activity_level)
    print(f"Your TDEE is: {tdee}")
    loss_date = find_weight_goal(weight)
    if loss_date != 0:
        print(f"It will take approximately {loss_date:.2f} weeks to reach your goal weight.")