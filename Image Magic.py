# Image Magic
# Load an image and manipulate the pixels

from PIL import Image

# Load the image (pumpkin)
image = Image.open('./halloween-unsplash.jpg')
output_image =image.open('./halloween-unsplash.jpg')

# Grab pixel information

a_pixel = image.getpixel((0, 0))  # grab pixel (0, 0) top-left


print(a_pixel)

# Iterate over EVERY PIXEL
# Get Dimensions (size) of the image
image.width = image.width
image.height = image.height

# Modify the image to it from colour to gray scale
# ( r, g, b ) --> ( ?, ?, ?, )
# take the r b g, add them up then divide by 3
# replace r, g, b with AVERAGE value

# Top to bottom
for y in range(image.height):
    # Left to right
    for x in range(image.width):
        # grab pixel information for THIS pixel
         pixel = image.getpixel((x, y))

         # grab r, g, b
         red, green, blue = pixel

         # calculate the average
         average =int((red + green + blue) / 3)

         # Create a gray pixel
         gray_pixel =(average, average, average)

        # Put that in the new image
        output_image.putpixel ((x, y), gray_pixel)


    output_image.save('grayscale.jpg')


