# Write a program that prompts the user for a distance in miles and convert it to kilometers

miles = input('Enter a distance in miles: ')
miles_float = float(miles)
# kilometers_value = miles_value * 1.609344
kilometers = miles_float * 1.609344
print('That value in kilometers is', kilometers)
