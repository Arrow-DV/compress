# Made By Ali Hany | Arrow-Dev <3
# Created in 2/3/2024 | Last Update 2/3/2024
# Visit Us https://arrow-dev.rf.gd


# Compress Photos Pillow [Project]
# import needed library's
from PIL import Image
from sys import argv as arg
import os
import random
# Check If Len Arg > 1
if len(arg) < 1 :
    print("-> Paramters is Less Than 1")
    exit()

# Getting Input
image = None
oldimg_size = os.path.getsize(arg[1])
try:
    image = Image.open(arg[1].strip())
    
except Exception as error:
    print(f"-> Error {error} ")
    exit()
# Now Compress Image Part
def compress(image):
   global arg
   # Get Image Extenstion
   img_exten = os.path.basename(arg[1]).split(".")[-1]
   # Now Save Image Time
   try:
       new_path = f"image{random.randint(0,100)}.{img_exten}"
       image.save(new_path,compress_level=9)
       newimg_size = os.path.getsize(os.path.abspath(new_path))
       ratio = (1-newimg_size / oldimg_size )* 100
       print(f"-> Compression successful {ratio:.2f}% Ratio Compression.")
   except Exception as error:
       print(f"-> Error {error}")
compress(image) 