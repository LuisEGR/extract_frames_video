import os
import cv2
import glob

def buscarVideos():
    return glob.glob("./*.mp4")
    
print(buscarVideos())

for vidName in buscarVideos():
    vidcap = cv2.VideoCapture(vidName)
    print("Procesando: ", vidName, " - ", vidcap.get(7), " frames")
    success,image = vidcap.read()
    count = 0
    success = True
    dirname = vidName.replace('.mp4', '_frames/')
    directory = os.path.dirname(dirname)
    if not os.path.exists(directory):
        os.makedirs(directory)

    while success:
      cv2.imwrite(dirname + "frame%d.jpg" % count, image)     # save frame as JPEG file
      success,image = vidcap.read()
      #print(count, ' - Read a new frame: ', success)
      count += 1
    print("--> Done")
