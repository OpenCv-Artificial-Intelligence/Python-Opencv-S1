import numpy as np
import imutils
import cv2

camera = cv2.VideoCapture(0)


# define the list of boundaries
boundaries = [
        ([150,100,0], [180,255,255])
      
]
while True:
    
    _, frame = camera.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
 
    # loop over the boundaries
    for (lower_range, upper_range) in boundaries:
        # create NumPy arrays from the boundaries
        lower_range = np.array(lower_range, dtype = "uint8")
        upper_range = np.array(upper_range, dtype = "uint8")
  
        # find the colors within the specified boundaries and apply
        # the mask
        mask = cv2.inRange(hsv, lower_range, upper_range)
        res = cv2.bitwise_and(frame,frame, mask = mask)

        cv2.imshow("frame", img)
        cv2.imshow("frame", frame)
        cv2.imshow("res",res)
        cv2.imshow('mask', mask)

    key = cv2.waitKey(5) & 0xFF
    if key == 27:
        break
        
cv2.destroyAllWindows()
camera.release()
