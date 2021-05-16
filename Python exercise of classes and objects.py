""""As an exercise, create and print a Point object, and then use id to print the object's unique identifier,
Translate the hexadecimal form into decimal and confirm that they match """


class point:
    pass


# creating new instance
blank = point()

# creating attribute for object blank
blank.x = 3.0
blank.y = 4.0

# retrieving the id value of object blank of class point
id(blank)
print(id(blank))

# translate to decimal form by converting to float
decimal_converter = float(id(blank))
print(decimal_converter)

# printing the value of object blank
print(blank.x)
print(blank.y)
print(blank)
