import cv2

# Reading the Image
img = cv2.imread(r"C:\Users\praghadeesh.siva\Downloads\Learning\OpenCV\Assets\Images\people1.jpg")

# Displaying the Image
cv2.imshow('Example - Show image in window',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Resizing the image
img = cv2.resize(img, (800, 600))
img.shape
cv2.imshow('Example - Show image in window',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Making the image Gray Scale to work on only One Channel, instead of Three Channel in RGB
image_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Example - Show image in window',image_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Detecting Faces
face_detector = cv2.CascadeClassifier(r"C:\Users\praghadeesh.siva\Downloads\Learning\OpenCV\Assets\Cascades\haarcascade_frontalface_default.xml")
detection = face_detector.detectMultiScale(image_gray)

for (x, y, w, h) in detection:
    cv2.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), 2)
cv2.imshow('Example - Show image in window',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Playing with Scale Factor
new_face_detector = cv2.CascadeClassifier(r"C:\Users\praghadeesh.siva\Downloads\Learning\OpenCV\Assets\Cascades\haarcascade_frontalface_default.xml")
image_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
detection = new_face_detector.detectMultiScale(image_gray, scaleFactor=1.5)
for (x, y, w, h) in detection:
    cv2.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), 2)
cv2.imshow('Example - Show image in window',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# New Image
img = cv2.imread(r"C:\Users\praghadeesh.siva\Downloads\Learning\OpenCV\Assets\Images\people2.jpg")
img = cv2.resize(img, (800, 600))
image_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
detection = new_face_detector.detectMultiScale(image_gray, scaleFactor=1.2, minNeighbors=6, minSize=(10,10), maxSize=(100,100))
for (x, y, w, h) in detection:
    cv2.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), 2)
cv2.imshow('Example - Show image in window',img)
cv2.waitKey(0)
cv2.destroyAllWindows()