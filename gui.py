import tkinter as tk
import pandas as pd
from sklearn.model_selection import train_test_split
from joblib import dump, load
from lightgbm import LGBMRegressor
from PIL import ImageTk,Image


# Load the trained model
model = load(r'''C:\Users\prana\Downloads\bicycle_count_model (1).joblib''')

def predict_count():
    # Get the input values from the GUI
    season = int(season_input.get())
    holiday = int(holiday_input.get())
    workingday = int(workingday_input.get())
    weather = int(weather_input.get())
    temp = float(temp_input.get())
    atemp = float(atemp_input.get())
    humidity = float(humidity_input.get())
    windspeed = float(windspeed_input.get())
    year = int(year_input.get())
    month = int(month_input.get())
    day = int(day_input.get())
    dayofweek = int(dayofweek_input.get())
    hour = int(hour_input.get())

    # Prepare the input data
    input_data = pd.DataFrame({
        'season': [season],
        'holiday': [holiday],
        'workingday': [workingday],
        'weather': [weather],
        'temp': [temp],
        'atemp': [atemp],
        'humidity': [humidity],
        'windspeed': [windspeed],
        'year': [year],
        'month': [month],
        'day': [day],
        'dayofweek': [dayofweek],
        'hour': [hour]
    })

    # Make the prediction
    count = model.predict(input_data)[0]
    ans = round(count)

    # Update the output label
    count_output.config(text=str(ans))

# Create the GUI
root = tk.Tk()
root.title("Predicting of Bicycles count")
root.geometry("850x500")

canvas = tk.Canvas(root, width=500, height=600,bg="black")
canvas.pack()

# set the background image
bg_image = tk.PhotoImage(file=r'''C:\Users\prana\Downloads\public bicycle.png''')
bg_image = bg_image.zoom(2)
canvas.create_image(320, 0, anchor=tk.NW, image=bg_image)

# set the image size
canvas.image = bg_image
canvas.place(relwidth=20, relheight=5)





# Create the input widgets
season_label = tk.Label(root, text="Season")
season_label.grid(row=0, column=0, padx=15, pady=15)
season_input = tk.Entry(root)
season_input.grid(row=0, column=1, padx=5, pady=5)

holiday_label = tk.Label(root, text="Holiday")
holiday_label.grid(row=1, column=0, padx=15, pady=15)
holiday_input = tk.Entry(root)
holiday_input.grid(row=1, column=1, padx=5, pady=5)

workingday_label = tk.Label(root, text="Workingday")
workingday_label.grid(row=2, column=0, padx=15, pady=15)
workingday_input = tk.Entry(root)
workingday_input.grid(row=2, column=1, padx=5, pady=5)

weather_label = tk.Label(root, text="Weather")
weather_label.grid(row=3, column=0, padx=15, pady=15)
weather_input = tk.Entry(root)
weather_input.grid(row=3, column=1, padx=5, pady=5)

temp_label = tk.Label(root, text="Temperature")
temp_label.grid(row=4, column=0, padx=15, pady=15)
temp_input = tk.Entry(root)
temp_input.grid(row=4, column=1, padx=5, pady=5)

atemp_label = tk.Label(root, text="ATemperature")
atemp_label.grid(row=5, column=0, padx=15, pady=15)
atemp_input = tk.Entry(root)
atemp_input.grid(row=5, column=1, padx=5, pady=5)

humidity_label = tk.Label(root, text="Humidity")
humidity_label.grid(row=6, column=0, padx=15, pady=15)
humidity_input = tk.Entry(root)
humidity_input.grid(row=6, column=1, padx=5, pady=5)

windspeed_label = tk.Label(root, text="Windspeed")
windspeed_label.grid(row=7, column=0, padx=15, pady=15)
windspeed_input = tk.Entry(root)
windspeed_input.grid(row=7, column=1, padx=5, pady=5)

year_label = tk.Label(root, text="Year")
year_label.grid(row=8, column=0, padx=15, pady=15)
year_input = tk.Entry(root)
year_input.grid(row=8, column=1, padx=5, pady=5)

month_label = tk.Label(root, text="Month")
month_label.grid(row=9, column=0, padx=10, pady=10)
month_input = tk.Entry(root)
month_input.grid(row=9, column=1, padx=5, pady=5)

day_label = tk.Label(root, text="Day")
day_label.grid(row=10, column=0, padx=10, pady=10)
day_input = tk.Entry(root)
day_input.grid(row=10, column=1, padx=5, pady=5)

dayofweek_label = tk.Label(root, text="Day of Week")
dayofweek_label.grid(row=11, column=0, padx=10, pady=10)
dayofweek_input = tk.Entry(root)
dayofweek_input.grid(row=11, column=1, padx=5, pady=5)

hour_label = tk.Label(root, text="Hour")
hour_label.grid(row=12, column=0, padx=10, pady=10)
hour_input = tk.Entry(root)
hour_input.grid(row=12, column=1, padx=5, pady=5)

#Create the output label
count_output_label = tk.Label(root, text="Count")
count_output_label.grid(row=13, column=0, padx=10, pady=10)
count_output = tk.Label(root, text="")
count_output.grid(row=13, column=1, padx=10, pady=10)

#Create the submit button
submit_button = tk.Button(root, text="Predict Count", command=predict_count)
submit_button.grid(row=14, column=0, columnspan=2, padx=5, pady=5)

root.mainloop() # run the GUI loop