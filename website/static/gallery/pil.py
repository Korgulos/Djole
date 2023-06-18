from PIL import Image


def getImageName(file_location):
    filename = file_location.split('\\')[-1]
    location = file_location.split("\\")[0:-1]
    filename = filename.split('.')
    name = filename[0]
    filename = '.'.join(filename)
    path = '\\'.join(location) + '\\' + filename
    if path[0:1] == '\\':
        path = path[1:]
    return [path, name]


link = getImageName('Radojka i Tine.tif')

#print(link)

img = Image.open(r'{}'.format(link[0]))

#baseWidth = 1080
new_width = 1080
new_height  = int(new_width * img.height / img.width)
img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)

rgb_im = img.convert("RGB")

rgb_im.save("{}.jpg".format(link[1]))

new_height = 150
new_width  = int(new_height * img.width / img.height)
img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)


# converting to jpg
rgb_im = img.convert("RGB")
  
# exporting the image
rgb_im.save("{}150.jpg".format(link[1]))
