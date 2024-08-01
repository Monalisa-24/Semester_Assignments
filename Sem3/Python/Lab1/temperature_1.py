print("\nCalcius to Ferhenheit\n")

temp1 = float(input("Take a temperature in Celcius : "))
ferhenheit = (9/5*temp1)+32
print(f"{temp1} degree in Celcius = {ferhenheit} degree in Ferhenheit")


print("\nFerhenheit to Calcius\n")

temp2 = float(input("Take a temperature in Ferhenheit : "))
celcius = ((temp2 - 32)*5)/9
print(f"{temp2} degree in Ferhenheit = {celcius} degree in Celcius")