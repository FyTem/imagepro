import os
from PIL import Image
from PIL import ImageEnhance

image_path = "D:\code\imagepro\康弘_10.26_2021.jpg"

image = Image.open(image_path)
grey_image = image.convert('L')
fil_image = grey_image.point(lambda i: i*1.8)
out = ImageEnhance.Contrast(fil_image)
out = out.enhance(1.5)

print(image.format, image.size, image.mode)

grey_image.show()
fil_image.show()
out.show()
