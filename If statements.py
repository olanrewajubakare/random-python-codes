points = 174  # use this as input for your submission
prize = None 
# establish the default prize value to None
if points <= 50:
    prize = "wooden rabbit"
elif 151 <= points <=180:
    prize = "wafer-thin mint!"
elif points >=181:
    prize = "penguin"


# use the points value to assign prizes to the correct prize names
if prize:
    result = "Congratulations! You won a {}!".format(prize)
else:
    result = "Oh dear, no prize this time."

# use the truth value of prize to assign result to the correct prize


print(result)
