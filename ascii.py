import cv2
import numpy as np
import imageio.v2
from scipy.ndimage import gaussian_filter
#import scipy.ndimage
#import gaussian filter
from PIL import Image, ImageDraw, ImageOps, ImageFont

# Characters used for Mapping to Pixels
Character = {
    "standard": "@%#*+=-:. ",
    "complex": "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
}


def get_data(mode):
    font = ImageFont.truetype("fonts/DejaVuSansMono-Bold.ttf", size=20)
    scale = 2
    char_list = Character[mode]
    return char_list, font, scale


# Making Background Black or White
bg = "white"
# bg = "black"
if bg == "white":
   # bg_code=255                             # for grayscale image
    bg_code = (255,255,255)               # for rgb there will be 3 inputs instead of 1 as in grayscale image
elif bg == "black":
   # bg_code=0
    bg_code = (0,0,0)

# Getting the character List, Font and Scaling characters for square Pixels
char_list, font, scale = get_data("complex")
num_chars = len(char_list)
num_cols = 300

# Reading Input Image
image = cv2.imread("./data/input_image.jpg")

# Converting Color Image to Grayscale
#image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)             # this code is needed when we want grayscale iamge

# Extracting height and width from Image
height, width, _ = image.shape               # for rgb as n*m*3

# Defining height and width of each cell==pixel
cell_w = width / num_cols
cell_h = scale * cell_w
num_rows = int(height / cell_h)

# Calculating Height and Width of the output Image
char_width, char_height = font.getsize("A")
out_width = char_width * num_cols
out_height = scale * char_height * num_rows

# Making a new Image using PIL
out_image = Image.new("RGB", (out_width, out_height), bg_code)     # here 'L' for grayscale and 'RGB' for rgb image
draw = ImageDraw.Draw(out_image)

# Mapping the Characters
# for grayscale image
"""for i in range(num_rows):
    min_h = min(int((i + 1) * cell_h), height)
    row_pix = int(i * cell_h)

    # lst = [i for i in range(5)] => We can make strings/lists/tuples in this way => lst = [0, 1, 2, 3, 4]
    # lst[first:last] gives us a sublist from the first index to the last index excluding the last index => lst[1:4]==[1, 2, 3]
    line = "".join([char_list[
        min(int(
            np.mean(image[row_pix:min_h, int(j*cell_w)
                    :min(int((j + 1) * cell_w), width)]) / 255 * num_chars
        ), num_chars - 1)]
        for j in range(num_cols)]) + "\n"

    # Draw string at a given position (x,y)
    draw.text((0, i * char_height), line, fill=255-bg_code, font=font)
"""
# for RGB image

for i in range(num_rows):
        for j in range(num_cols):
              partial_image = image[int(i * cell_h):min(int((i + 1) * cell_h), height),
                              int(j * cell_w): min(int((j + 1) * cell_w), width), :]
              partial_avg_color = np.sum(np.sum(partial_image, axis=0), axis=0) / (cell_h * cell_w)
              partial_avg_color = tuple(partial_avg_color.astype(np.int32).tolist())
              c = char_list[min(int(np.mean(partial_image) * num_chars / 255), num_chars - 1)]
              draw.text((j * char_width, i * char_height), c, fill=partial_avg_color, font=font)
              
# Inverting Image and removing excess borders
if bg == "white":
    cropped_image = ImageOps.invert(out_image).getbbox()
elif bg == "black":
    cropped_image = out_image.getbbox()

# Saving the new Image
out_image = out_image.crop(cropped_image)
out_image.save("./data/rgb_output_white.jpg")
# take image input

image = "./data/rgb_output_white.jpg"



# function to convert image into sketch
def rgb2gray(rgb):
	# 2 dimensional array to convert image to sketch
	return np.dot(rgb[..., :3], [0.2989, 0.5870, .1140])


def dodge(front, back):

	# if image is greater than 255 (which is not possible) it will convert it to 255
	f_sketch = front*255/(255-back)
    
	f_sketch[f_sketch > 255] = 255
	f_sketch[back == 255] = 255

	# to convert any suitable existing column to categorical type we will use aspect function
	# and uint8 is for 8-bit signed integer
	return f_sketch.astype('uint8')


out_put = imageio.v2.imread(image)
gray_image = rgb2gray(out_put)

i = 255-gray_image


# to convert into a blur image
blur_image =gaussian_filter(i, sigma=13)              #Use a Gaussian function to blur the image.


# calling the function
returned = dodge(blur_image, gray_image)


cv2.imwrite('./data/sketch_bg_white.png', returned)
