"""
Main file where the GUI and macro tracking program is handled.
"""

import tkinter as tk

from tkinter import messagebox

from calories import calorie_calculator, Macro_split

from tkinterfuncs import add_placeholder_text

def main():
    """
    Main function which handles GUI and macro tracking.
    """

    # Input prompts
    gender = input("What is your gender? (Male/Female): ")
    active_status = input("What is your activity level? " + 
                          "(Limited, Light, Moderate, Very, Extreme): ")
    weight = int(input("What is your weight in kg?: "))
    height = int(input("What is your height in cm?: "))
    age = int(input("What is your age in years?: "))
    goal = input("What is your goal? (Gain Weight, Balanced, Lose Weight): ")
    bodytype = input("What is your body type? " +
                     "(Ectomorph, Mesomorph, Endomorph): ")

    if active_status == "Limited":
        activity_level = 1.2
    elif active_status == "Light":
        activity_level = 1.25
    elif active_status == "Moderate":
        activity_level = 1.375
    elif active_status == "Very":
        activity_level = 1.430
    elif active_status == "Extreme":
        activity_level = 1.5

    # Call functions to calculate calories and macronutrients.
    calories = calorie_calculator(gender, activity_level, 
                                  weight, height, age, goal)
    print(f"You need {calories} per day")
    macros = Macro_split(bodytype, calories)
    print(f"You need {macros[0]} grams of Protein for the day")
    print(f"You need {macros[1]} grams of Carbohydrates for the day")
    print(f"You need {macros[2]} grams of Fats for the day")
    message = "You can find the nutritional value of foods at \
nutritionvalue.org or look for the nutrition label on your food's packaging"
    print(message)
    consumed_macros = [0, 0, 0]

    def track_macronutrients():
        """
        Callback function for the Track Macronutrients button.

        Retrieves the user's input for macronutrients,
        updates consumed macronutrients, calculates and
        updates progress label, checks for exceeding values,
        and prompts for continued tracking.
        """

        protein = float(protein_entry.get())
        carbs = float(carbs_entry.get())
        fats = float(fats_entry.get())

        consumed_macros[0] += protein
        consumed_macros[1] += carbs
        consumed_macros[2] += fats

        progress = [consumed_macros[i] / macros[i] for i in range(3)]

        # Display progress bar.
        pt = ""
        for i in range(3):
            eaten = consumed_macros[i]
            suggested = macros[i]
            progress_value = int(progress[i] * 10)
            bar = '#' * progress_value + '-' * (10 - progress_value)
            macronutrient = ['Protein', 'Carbs', 'Fats'][i]
            pt += f"{macronutrient}: [{bar}] {eaten}/{suggested} grams\n"

        progress_label.config(text=pt)  # Update progress bar.

        # Check for exceeding macro values.
        exceeded_macros = []
        for i in range(3):
            if consumed_macros[i] > macros[i]:
                exceeded_macros.append(['Protein', 'Carbs', 'Fats'][i])

        if exceeded_macros:
            message = (
                f"You have exceeded the suggested intake for: "
                f"{', '.join(exceeded_macros)}"
            )
            messagebox.showwarning("Exceeded Intake", message)

        # Clear when rerun.
        protein_entry.delete(0, tk.END)
        carbs_entry.delete(0, tk.END)
        fats_entry.delete(0, tk.END)

        # Prompts user to continue tracking.
        choice = messagebox.askyesno("Continue Tracking", 
                        "Do you want to continue tracking?")
        if not choice:
            window.destroy()

    window = tk.Tk()
    window.title("Macronutrient Tracker")

    # Create and style labels.
    protein_label = tk.Label(window, text=f"You need {macros[0]} " + 
                             "grams of Protein for the day")
    protein_label.pack(pady=(10, 0))

    carbs_label = tk.Label(window, text=f"You need {macros[1]} " + 
                           "grams of Carbohydrates for the day")
    carbs_label.pack()

    fats_label = tk.Label(window, text=f"You need {macros[2]} " + 
                          "grams of Fats for the day")
    fats_label.pack()

    # Create and style entry fields with placeholder text.
    protein_entry = tk.Entry(window, width=30)
    protein_entry.pack(pady=(0, 10))
    add_placeholder_text(protein_entry, "Enter protein intake")

    carbs_entry = tk.Entry(window, width=30)
    carbs_entry.pack(pady=(0, 10))
    add_placeholder_text(carbs_entry, "Enter carbohydrate intake")

    fats_entry = tk.Entry(window, width=30)
    fats_entry.pack(pady=(0, 10))
    add_placeholder_text(fats_entry, "Enter fat intake")

    track_button = tk.Button(window, text="Track Macronutrients",
                             command=track_macronutrients)
    track_button.pack()

    progress_label = tk.Label(window)
    progress_label.pack()

    message_label = tk.Label(window, text=message)
    message_label.pack()

    window.mainloop()

if __name__ == "__main__":
    main()