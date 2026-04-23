import tkinter as tk
from tkinter import ttk, PhotoImage


root = tk.Tk()
root.geometry("500x600")
root.title("Daily Deficit")
image_path = PhotoImage(file=r"/Users/breaunuh/Downloads/backgroundimage.png")
bg_image = ttk.Label(root, image=image_path)
bg_image.image = image_path
bg_image.place(x= 0, y= 0, anchor= "center")

header = tk.Label(root, text = "LETS TRACK YOUR CALORIES!", font = ("Helvetica", 20, "bold"))
header.pack(padx= 10, pady= 10)
weight_label = tk.Label(root, text ="Weight In lbs:", font = ("Arial", 12, "bold"))
weight_label.pack(padx= 10, pady= 10)
user_weight = tk.Entry(root)
user_weight.pack()

goal_label = tk.Label(root, text ="Daily Calorie Goal:", font = ("Arial", 12, "bold"))
goal_label.pack(padx= 10, pady= 10)
user_goal= tk.Entry(root)
user_goal.pack()

calories_label = tk.Label(root, text ="Calories Eaten:", font = ("Arial", 12, "bold"))
calories_label.pack(padx= 10, pady= 10)
user_calories = tk.Entry(root)
user_calories.pack()

time_label = tk.Label(root, text ="Exercise Time In Minutes:", font = ("Arial", 12, "bold"))
time_label.pack(padx= 10, pady= 10)
user_minutes = tk.Entry(root)
user_minutes.pack()

exercise_label = tk.Label(root, text ="Exercise Difficulty:", font = ("Arial", 12, "bold"))
exercise_label.pack(padx= 10, pady= 10)

choices = ["Easy","Medium","Hard"]
difficulty = tk.StringVar()
dropdown = tk.OptionMenu(root, difficulty, *choices)
dropdown.pack(padx= 10, pady= 10)

progress_bar = ttk.Progressbar(root, orient= 'horizontal', length = 300, mode= 'determinate')
progress_bar.pack(padx= 10, pady= 10)

def calculate_daily_goal():
    weight = int(user_weight.get())
    goal = int(user_goal.get())
    eaten = int(user_calories.get())
    time = int(user_minutes.get())
    difficultylevel = difficulty.get()

    if difficultylevel == "Easy":
        met = 3
    elif difficultylevel == "Medium":
        met= 6
    else:
        met = 10
    
    weight_kg = weight / 2.205
    total_cal_burn = (met * weight_kg*time)/60
    amount = eaten - total_cal_burn
    leftover =  goal - amount
    print(total_cal_burn)
    progress_bar['value'] = (amount/goal)*100
    if amount > goal:
        result.configure(text= f"Oops! You are over your goal by {abs(leftover)} calories")
    elif amount < goal:
        result.configure(text= f"Congrats! You have  {abs(leftover)} calories left")
    else:
        result.configure(text="Amazing you reached your goal!")
result = tk.Label(root, text="", font=("Arial", 12, "bold"))
result.pack(padx=10, pady=10)
button = tk.Button(root, text="Calculate", font=("Arial", 12), command=calculate_daily_goal)
button.pack(padx=10, pady=10)


root.mainloop()
