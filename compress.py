# Made By Ali Hany | Arrow-Dev <3
# Created in 2/3/2024 | Last Update 2/3/2024
# Visit Us https://arrow-dev.rf.gd


# Compress Photos Pillow [Project]
# import needed library's

import random
import os
import sys

from PIL import Image

if len(sys.argv) < 1 :
    print("-> Paramters are Less Than 1")
    sys.exit(-1)

args = sys.argv[1:]

def get_image_size(image_path):
    return os.path.getsize(image_path)

# Now Compress Image Part
def compress(image, path="compressed.jpg"):
   # Now Save Image
    try:
       image.save(path, compress_level=9)
    except Exception as error:
        print(f"-> Error {error}")
        sys.exit(-1)

def main():
    image_path = args[0].strip()
    try:
        image = Image.open(image_path)
    except Exception as error:
        print(f"-> Error {error}")
    else:
        _, image_extention = os.path.splitext(image_path)
        new_path = f"image{random.randint(0,100)}{image_extention}"
        compress(image, path=new_path)
        old_size = get_image_size(image_path)
        new_size = get_image_size(new_path)
        ratio = (1 - new_size / old_size) * 100

        print(f"-> Compression successful {ratio:.2f}% Ratio Compression.")



if __name__ == "__main__":
    main() 
