INCHES_TO_CM = 2.54
CM_TO_METERS = 0.01
FEET_TO_INCHES = 12

# Enter your code here

def convert_height_to_meters(feet,inches):
    height_in_inches = (feet*FEET_TO_INCHES) + inches
    height_in_cm = height_in_inches * INCHES_TO_CM
    height_in_meters = height_in_cm * CM_TO_METERS
    print(str(feet) + " feet, " + str(inches) + " inches = " + str(height_in_meters) + " meters")
    
convert_height_to_meters(5,11)

convert_height_to_meters(6,0)

convert_height_to_meters(5,5)
