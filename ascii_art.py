# ASCII Art
# Project created Fall 2018
# Idea: https://robertheaton.com/2018/06/12/programming-projects-for-advanced-beginners-ascii-art/
from PIL import Image
import numpy as np
import pprint
import sys

# TODO:
# add argparse thing - image file, single brightness number

pp = pprint.PrettyPrinter(indent=4)
ascii_chars = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$" 

#single brightness number
def single_brightness(color_func):
	def single_color_func(r, g, b):
		if color_func == "AVERAGE":
			return int((r + b + g)/3)
		elif color_func == "LIGHTNESS":
			return int((max(r, b, g) +  min(r, b, g))/2)
		elif color_func == "LUMINOSITY":
			return int((max(r, b, g) +  min(r, b, g))/2)
		else:
			return ValueError("Did not select valid color function option")
	return single_color_func


# load image and dimensions
try:
	im = Image.open("beach.png")			# im is a PIL.image
	print("Image loaded successfully!")
except:
	print("Image cannot be opened")
width, height = im.size
print("Original dimensions: " + str(width) + " x " + str(height))

im = im.resize((320, 240))
width = 320
height = 240

#load pixels into matrix
pixels = im.load()
pixel_matrix = []
brightness_matrix = []
min_bright = sys.maxsize
max_bright = sys.maxsize*-1
color_func = single_brightness("AVERAGE")	# Can be AVERAGE, LIGHTNESS or LUMINOSITY

for x in range(width):
	brightness_row = []
	for y in range(height):
		r, g, b, total = pixels[x, y]
		rgb = (r, g, b)
		brightness = color_func(r, g, b)
		if brightness < min_bright:
			min_bright = brightness
		if brightness > max_bright:
			max_bright = brightness
		brightness_row.append(brightness)
	brightness_matrix.append(brightness_row)

scaled_min = 0
scaled_max = len(ascii_chars)-1

for i in range(len(brightness_matrix)):
	row = []
	for j in range(len(brightness_matrix[0])):
		val = brightness_matrix[j][i]
		new_value = int(( (val - min_bright) / (max_bright - min_bright) ) * (scaled_max - scaled_min) + scaled_min)
		row.append(ascii_chars[new_value])
	str_row = "".join(row)
	print(str_row)
