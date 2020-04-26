import os
from glob import glob

max = '0'
for png in glob(os.path.join(os.getcwd(), 'images/train/*.png')):
  this = png.split('.')[0].split('/')[-1]
  if int(this) > int(max):
    max = this

print(max)

for png in glob(os.path.join(os.getcwd(), 'images/test/*.png')):
  name = png.split('.')[0].split('/')[-1] 
  newname = str(int(name) + int(max))
  os.rename(png, f'images/test/{newname}.png')

max = '0'
for xml in glob(os.path.join(os.getcwd(), 'annotations/train/*.xml')):
  this = xml.split('.')[0].split('/')[-1]
  if int(this) > int(max):
    max = this

print(max)

for xml in glob(os.path.join(os.getcwd(), 'annotations/test/*.xml')):
  name = xml.split('.')[0].split('/')[-1]  
  newname = str(int(name) + int(max))
  os.rename(xml, f'annotations/test/{newname}.xml')