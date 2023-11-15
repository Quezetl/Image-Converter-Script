from PIL import Image
import os
from pillow_heif import register_heif_opener

register_heif_opener()

if input("would you like to convert photos: ").lower() != "yes":
    exit()

prompt = input("would you like to create a new directory for the images?\n1) Yes\n2) No\nAnswer: ")

if prompt == str(1) or prompt.lower() == "yes" or prompt.lower() == "y":
    newFolder = input("Enter new folder name: ")
    os.mkdir(newFolder)
    newFolder = newFolder + "/"
else:
    newFolder = ""

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

for filename in os.listdir("."):
    if filename.endswith(oExt):
        prefix = filename.split(oExt)[0]
        name = prefix + nExt
        newName = newFolder + name
        im = Image.open(filename)
        exifInfo = im.info['exif']
        img = im.convert("RGB")
        img.save(name, formatType, exif=exifInfo)
        os.renames(name, newName)
