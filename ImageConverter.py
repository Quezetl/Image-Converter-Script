from PIL import Image
import os
from pillow_heif import register_heif_opener

register_heif_opener()

# Check if user wants new directory
prompt = input("would you like to create a new directory for the images?\n1) Yes\n2) No\nAnswer: ")

# Either create new directory or don't based on previous input
if prompt == str(1) or prompt.lower() == "yes" or prompt.lower() == "y":
    newFolder = input("Enter new folder name: ")
    os.mkdir(newFolder)
    newFolder = newFolder + "/"
else:
    newFolder = ""

# Loop for checking conversion type, if invalid input it will prompt again for valid input
while (True):
    type = int(input("What conversion would you like to make?\n"
                     "1).HEIC ->  .JPG\n"
                     "2).PNG  ->  .JPG\n"
                     "3).HEIC ->  .PNG\n"
                     "4).JPG  ->  .PNG\n... "))
    match type:
        case 1:
            break
        case 2:
            break
        case 3:
            break
        case 4:
            break
        case _:
            continue

# Stores new and old extension type to be used later
match type:
    case 1:
        oExt = ".HEIC"
        nExt = ".jpg"
        formatType = 'JPEG'
    case 2:
        oExt = ".PNG"
        nExt = ".jpg"
        formatType = 'JPEG'
    case 3:
        oExt = ".HEIC"
        nExt = ".PNG"
        formatType = 'PNG'
    case 4:
        oExt = ".HEIC"
        nExt = ".PNG"
        formatType = 'PNG'
    case _:
        print("Something went wrong\n")

# main loop for converting from old file type to new file type
for filename in os.listdir("."):
    try:
        if filename.endswith(oExt):
            prefix = filename.split(oExt)[0]
            name = prefix + nExt
            newName = newFolder + name
            im = Image.open(filename)
            exifInfo = im.info['exif']
            img = im.convert("RGB")
            img.save(name, formatType, exif=exifInfo)
            os.renames(name, newName)
    except Exception as e:
        print(f"Error converting {filename}: {e}")
