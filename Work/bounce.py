# bounce.py
#
# Exercise 1.5

height = 100 # Meters
bounce_count = 1

while bounce_count <= 10:
    height *=  0.6
    print(bounce_count, round(height, 4))
    bounce_count += 1
