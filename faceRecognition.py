import cv2
import time
import os

def getlistOffiles(dirName):
    ListOfFile = os.listdir(dirName)
    allfiles = list()

    for entry in ListOfFile:
        fullPath = os.path.join(dirName,entry)
        if os.path.isdir(fullPath):
            allfiles = allfiles + getlistOffiles(fullPath)
        else:
            allfiles.append(fullPath)
    return allfiles

def main():
    dirName = 'pictures'
    listOfFiles = getlistOffiles(dirName)

    for i in range(6):
        imagePath = listOfFiles[i]
        print(imagePath)
        cascPath = 'haarcascade_frontalface_default.xml'
        faceCascade = cv2.CascadeClassifier(cascPath)
        image = cv2.imread(imagePath)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        faces = faceCascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5,minSize=(30,30))

        for (x,y,w,h) in faces:
            cv2.rectangle(image, (x,y), (x+w, y+h), (0,255, 0), 2)

        cv2.imshow("Faces found", image)
        cv2.waitKey(4)
        time.sleep(5)
        cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
