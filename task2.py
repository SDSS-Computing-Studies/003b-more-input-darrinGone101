#!python3
"""
A population can be modeled by the following:
future population = (current population)*(1+r)^(time in years) 
Have the user enter the current population, the rate of growth as a decimal and the number of DAYS.
Calculate the expected future population

Enter the population: 25000000
Enter the rate of growth in percent: 2.1
Enter the number of days: 12
There will be 25017087 people after 12 days
"""
population = float( input("Enter The  Population: "))
rgrowth = float( input("Enter The Rate of Growth: "))
time = int( input("Enter The Number of Days: "))
fpop = population*(1+ (rgrowth/100))**(time / 365)
fpop = round(fpop)
print(f"There will be {fpop} people after {time} days")