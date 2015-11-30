#!/usr/bin/python

import sys
import dicom
import pylab

from os import listdir
from os.path import isfile, join

#print 'Number of arguments:', len(sys.argv), 'arguments.'
#print 'Argument List:', str(sys.argv)

#print ('Number of arguments:', len(sys.argv), 'arguments.')
#print ('Argument List:', str(sys.argv))

mypath=sys.argv[1]
file_Index=int(sys.argv[2])


onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))] 
file_name=onlyfiles[file_Index]

 	
ds=dicom.read_file(join(mypath,file_name))
pylab.imshow(ds.pixel_array, cmap=pylab.cm.bone)


#str_Dir=sys.argv[1];
#fileIndex=int(sys.argv[2])

print("The directory to the picture is : %s" %mypath)
print("The file_index is  : %d" %file_Index)
print(ds)
pylab.savefig('result.jpg')

htmlPage="""
<!DOCTYPE html>
<html>
<head>
  <title>Hi there</title>
</head>
<body>
<img src="result.jpg" >

<pre> %s </pre>
</body>
</html>

""" % (ds)

text_file = open("Index.html", "w")

text_file.write("%s " % htmlPage)

text_file.close()

#print ("Hello, Python!")
