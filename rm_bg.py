# Author: Oladapo Okikiola
# first install rembg module
from rembg import remove
from PIL import Image
input_path = 'pic_1.jpg'
output_path = 'removed.png'
input = Image.open(input_path)
output = remove(input)
output.save(output_path)
