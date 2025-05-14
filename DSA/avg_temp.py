'''

The goal of this project is to create a program that:

    1. Accepts daily high temperatures for a given number of days.
    2. Calculates the average temperature.
    3. Finds and returns the number of days with temperatures above the average.

'''

num_days = int(input("For how many days you want to calculate average temperature:\n"))

temperature = []

for i in range(1, num_days+1):
    temp = float(input(f"Enter temperature for day {i}:\n"))
    temperature.append(temp)

print(temperature)

avg_temp = sum(temperature)/int(num_days)

no_of_days_above_avg = 0

for temp in temperature:
    if temp > avg_temp:
        no_of_days_above_avg += 1

print(f"The avg temperature for the input number of days: {avg_temp} degree")
print(f"Among {num_days} days the temperature above {avg_temp} is: {no_of_days_above_avg}")