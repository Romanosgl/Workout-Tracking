import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from caloriecalc import find_activity_level,find_bmr,find_tdee,find_weight_goal,McArdle_multiplier,personal_data

window = tk.Tk()
window.title("Calorie Calculator")
window.geometry("800x500")

image_path = "images/bicep.webp"
pil_image = Image.open(image_path)
tk_image = ImageTk.PhotoImage(pil_image)
window.iconphoto(True,tk_image)


label = ttk.Label(window,text="Gym Tracker", font=("consolas", 20))
label.pack()

frame = ttk.Frame(window, padding="10 10 10 10")
frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

bar_frame = ttk.Frame(window)
bar_frame.pack(fill=tk.X)

# Function to show calorie calculator inputs
def show_calorie_calculator():
    for widget in frame.winfo_children():
        widget.destroy()

    ttk.Label(frame, text="Enter your details", font=("consolas", 15)).pack(pady=10)

    ttk.Label(frame, text="Weight (kg):").pack(pady=5)
    weight_entry = ttk.Entry(frame)
    weight_entry.pack(pady=5)

    ttk.Label(frame, text="Height (cm):").pack(pady=5)
    height_entry = ttk.Entry(frame)
    height_entry.pack(pady=5)

    ttk.Label(frame, text="Age:").pack(pady=5)
    age_entry = ttk.Entry(frame)
    age_entry.pack(pady=5)

    ttk.Label(frame, text="Gender:").pack(pady=5)
    gender_combobox = ttk.Combobox(frame, values=["Male", "Female"])
    gender_combobox.pack(pady=5)

    ttk.Label(frame, text="Activity Level:").pack(pady=5)
    activity_combobox = ttk.Combobox(frame, values=list(McArdle_multiplier.keys()))
    activity_combobox.pack(pady=5)

    ttk.Label(frame, text="Goal Weight (kg):").pack(pady=5)
    goal_weight_entry = ttk.Entry(frame)
    goal_weight_entry.pack(pady=5)

    ttk.Label(frame, text="Weight Loss/Gain Pace per Week (kg):").pack(pady=5)
    pace_combobox = ttk.Combobox(frame, values=["0.25", "0.5", "1"])
    pace_combobox.pack(pady=5)

    result_label = ttk.Label(frame, text="")
    result_label.pack(pady=10)

    ttk.Button(frame, text="Calculate", command=calculate_calories).pack(pady=20)

def open_calorie_calculator():
    pass

calorie_calculator_button = ttk.Button(bar_frame, text="Calorie Calculator", command=show_calorie_calculator)
calorie_calculator_button.pack(side=tk.LEFT, padx=10, pady=10)

frame = ttk.Frame(window, padding="10 10 10 10")
frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

window.mainloop()
