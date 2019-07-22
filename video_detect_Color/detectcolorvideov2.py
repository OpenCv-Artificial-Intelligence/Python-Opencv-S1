import numpy as np
import imutils
import cv2

#otherwise, grab a reference to the video file
camera = cv2.VideoCapture(0)

# define the lower and upper boundaries of the colors in the HSV color space
lower = {'white':(0,37,189),
         'black':(59,44,0),
         'gay':(96,21,105),
         'red':(0, 119, 17),
         'green':(49, 23, 72),
         'blue':(50, 130, 140),
         'yellow':(0, 159, 136),
         'orange':(0, 100, 112),
         'brown':(0,0,54),
         'pink':(0,96,241),
         'purple':(120,0,12)}

upper = {'white':(124,154,255),
         'black':(179,187,61),
         'gay':(141,70,168),
         'red':(7,241,152),
         'green':(97,245,255),
         'blue':(150,200,230),
         'yellow':(179,238,253),
         'orange':(12,255,255),
         'brown':(51,89,146),
         'pink':(179,154,255),
         'purple':(156,169,213)}


# define standard colors for circle around the object
colors = {'white':(255,255,255),
          'black':(0,0,0),
          'gay':(128,128,128),
          'red':(255,0,0),
          'green':(0,255,0),
          'blue':(0,0,255),
          'yellow':(255, 255, 0),
          'orange':(255,165,0),
          'brown':(128,0,0),
          'pink':(240,128,128),
          'purple':(128,0,128)}
 

# keep looping
while True:
    # grab the current frame
    (grabbed, frame) = camera.read()

    # resize the frame, blur it, and convert it to the HSV color space
    frame = imutils.resize(frame, width=400)
    blurred = cv2.GaussianBlur(frame, (11, 11), 0)
    
    # Threshold the HSV image to get only blue colors
    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)

    #for each color in dictionary check object in frame
    for key, value in upper.items(): #loop

        # blobs left in the mask
        kernel = np.ones((9,9),np.uint8)
        mask = cv2.inRange(hsv, lower[key], upper[key]) #map
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
        mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
               
        # find contours in the mask and initialize the current
        # (x, y) center of the ball
        cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[-2]
        center = None
       
        # only proceed if at least one contour was found
        if len(cnts) > 0:
            # find the largest contour in the mask, then use
            # it to compute the minimum enclosing circle and
            # centroid
            c = max(cnts, key=cv2.contourArea)
            ((x, y), radius) = cv2.minEnclosingCircle(c)
            M = cv2.moments(c)
            center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"])) #center 
       
            # only proceed if the radius meets a minimum size. Correct this value for your obect's size
            if radius > 0.1:
                # draw the circle and centroid on the frame,
                # then update the list of tracked points
                #cv2.circle(frame, (int(x), int(y)), int(radius), colors[key], 3)
                cv2.putText(frame,key + " color", (int(x-radius),int(y-radius)), cv2.FONT_HERSHEY_SIMPLEX, 0.6,colors[key],2)
 
     
            # show the frame to our screen
            cv2.imshow("Output", frame)
   
    key = cv2.waitKey(5) & 0xFF
    if key == 27:
        break
 
# cleanup the camera and close any open windows
camera.release()
cv2.destroyAllWindows()
