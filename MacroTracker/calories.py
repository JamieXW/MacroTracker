"""
File that contains functions for calorie and macronutrients calculators.
"""

def calorie_calculator(gender, activity_level, weight, height, age, goal):
    """
    Function that calculates calories based on certain factors.

    Args:
        gender (str): Gender of the user
        activity_level (float): Activity level factor
        weight (int): Weight of user in kilograms
        height (int): Height of user in centimeters
        age (int): Age of user in years
        goal (str): Goal of the user to gain or lose weight

    Returns:
        float: Calculated daily calories
    """

    if gender == "Male":
        base_calories = (10 * weight) + (6.25 * height) - (5 * age) + 5
    elif gender == "Female":
        base_calories = 10 * weight + 6.25 * height - 5 * age - 161
    calories = base_calories * activity_level
    if goal == "Gain Weight":
        calories = calories * 1.15
    elif goal == "Lose Weight":
        calories = calories * 0.85
    calories = round(calories, 2)
    return calories

def Macro_split(bodytype, calories):
    """
    Function that calculates the macronutrients split based on factors.

    Args:
        bodytype (str): Body type of the user
        calories (float): Suggested calories

    Returns:
        list: List containing the daily grams of
        protein, carbohydrates, and fats.
    """

    if bodytype == "Ectomorph":
        protein_calories = 0.25 * calories
        carb_calories = 0.55 * calories
        fat_calories = 0.20 * calories
    elif bodytype == "Mesomorph":
        protein_calories = 0.30 * calories
        carb_calories = 0.40 * calories
        fat_calories = 0.30 * calories
    elif bodytype == "Endomorph":
        protein_calories = 0.35 * calories
        carb_calories = 0.25 * calories
        fat_calories = 0.40 * calories
    protein_grams = protein_calories / 9
    protein_grams = round(protein_grams, 2)
    carb_grams = carb_calories / 4
    carb_grams = round(carb_grams, 2)
    fat_grams = fat_calories / 4
    fat_grams = round(fat_grams, 2)
    list = [protein_grams, carb_grams, fat_grams]
    return list

