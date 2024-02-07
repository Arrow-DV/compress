# Made By Ali Hany | Arrow-Dev <3
# Created in 2/3/2024 | Last Update 2/7/2024
# Visit Us https://arrow-dev.rf.gd/bio
# Compress Photos Pillow [Project]
# Compress Videos MoviePy[Project]


# -------- Special Thanks -----------
# For Ziad Mustafa | For Improving The Code


# import needed library's
import random
import os
import sys
from PIL import Image
from moviepy.editor import VideoFileClip
from moviepy.audio.fx.all import audio_fadein, audio_fadeout


# Check If Given Args Less Than 1 Means He Run The File Without Args
if len(sys.argv) < 1 :
    print("-> Paramters are Less Than 1")
    sys.exit(-1)

# Inputs
args = sys.argv[1:] # it will start after python file name

# Functions

# Get Image Size To Show It After Finish
def getsize(file_path):
    """Get Video-Image Old Size
       And Show Compress Ratio
    """
    return os.path.getsize(file_path)

# Now Compress Image Part
def compress_image(image, path="compressed.jpg"):
    """This Function Compress The Image"""
    # Now Save Image
    try:
       image.save(path, compress_level=9)
    except Exception as error:
        print(f"-> Error {error}")
        sys.exit(-1)
# Image Extenstion Check
def check_ext(file : str):
    """Check If Given File 
       Is Image Or Video
       File : Image Path
    """
    _type_ = ""
    image_extensions = ['jpg', 'jpeg', 'png', 'gif', 'bmp', 'tiff', 'tif', 'svg', 'webp', 'ico', 'jp2', 'j2k', 'raw', 'cr2', 'nef', 'psd', 'ai', 'eps', 'pdf', 'dds', 'tga', 'exr', 'hdr', 'pgm', 'ppm']
    video_extensions = ['mp4', 'mkv', 'avi', 'mov', 'wmv', 'flv', 'webm', 'm4v', '3gp', 'mpeg', 'mpg', 'm2v', 'ogv', 'vob', 'qt', 'divx', 'asf', 'rm', 'rmvb', 'ts', 'm2ts']
    file_extension = file.split(".")[-1].lower().strip()
    for ext in image_extensions:
        if( file_extension== ext):
                _type_ = "image"
      
    for ext in video_extensions:
        if(file_extension == ext):
            _type_ = "video"
       
    return _type_,file_extension

# Compress Video Function
def compress_video(input_path: str, output_path: str, bitrate='500k'):

    # Load the video clip
    video_clip = VideoFileClip(input_path)
    # Set the output bitrate indirectly by setting audio bitrate
    audio_clip = video_clip.audio
    new_audio_clip = audio_clip.fx(audio_fadein, 0.5).fx(audio_fadeout, 0.5)
    video_clip = video_clip.set_audio(new_audio_clip)

    # Write the compressed video to the output file
    video_clip.write_videofile(output_path, codec='libx264', audio_codec='aac', verbose=False,bitrate=bitrate)
    # Close the video clip
    video_clip.close()
    old_size = getsize(input_path)
    new_size = getsize(output_path)
    ratio = (1 - new_size / old_size) * 100
    getsize(output_path)
    print(f"-> The video has been compressed successfully\n-> Ratio Of Compression {ratio:.2f}%".title())


def image_progress():

    image_path = args[0].strip()
    try:
        image = Image.open(image_path)
    except Exception as error:
        print(f"-> Error {error}")
        exit()
    else:
        _, image_extention = os.path.splitext(image_path)
        new_path = f"image{random.randint(0,100)}{image_extention}"
        compress_image(image, path=new_path)
        old_size = getsize(image_path)
        new_size = getsize(new_path)
        ratio = (1 - new_size / old_size) * 100

        print(f"-> Compression successful {ratio:.2f}% Ratio Compression.".title())
        print(f"-> Image Saved Successfully At {new_path} ")
        return new_path
def init():

    if check_ext(args[0])[0] == "image":
        try:
            image_progress()
        except KeyboardInterrupt:
            print("-> Exited Successfully")
            
        except FileNotFoundError:
            print("-> File wasn't Found!")
        except Exception as error:
            print(f"-> Error {error}")

    elif check_ext(args[0])[0] == "video":
        output_path = f"video{random.randint(0,1000)}.{check_ext(args[0])[1]}"
        # We Will Use Video Compress Functions
        try:
            compress_video(args[0],f"video{random.randint(0,1000)}.{check_ext(args[0])[1]}")
        except KeyboardInterrupt:
            print("-> Exited Successfully")
            try:
                os.remove(output_path)
            except:
                pass
        except FileNotFoundError:
            print("-> File wasn't Found!")
        except Exception as error:
            print(f"-> Error {error}")
            exit()
    else:
        print("-> Unknown File Type")
        

if __name__ == "__main__":
    init()
