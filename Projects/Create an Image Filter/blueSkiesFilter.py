# Constants for the image
IMAGE_URL = str(input("Enter a valid image URL: "))
IMAGE_WIDTH = 280
IMAGE_HEIGHT = 200
blueUpFactor = int(input("How much more blue do you want this image | Enter a value between 1 and 255"))
maxPixelValue = 255

image = Image(IMAGE_URL)
image.set_position(70, 70)
image.set_size(IMAGE_WIDTH, IMAGE_HEIGHT)
add(image)


# Filter to brighten an image
def blueFilter(pixel):
    blue = blueColour(pixel[2])
    return blue

def blueColour(colorValue):
    return min(colorValue + blueUpFactor, maxPixelValue)

def changePicture():
    for x in range(image.get_width()):
        for y in range(image.get_height()):
            pixel = image.get_pixel(x,y)
            newColor = blueFilter(pixel)
            image.set_blue(x, y, newColor)
            

# Give the image time to load
print("Creating Blue Skies....")
print("Might take a minute....")
timer.set_timeout(changePicture, 1000)
