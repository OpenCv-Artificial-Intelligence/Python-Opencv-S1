#cv version 3.4.2
import sys
import cv2
import cv2 as cv
import numpy as np

def main(argv):
    default_file =  "pic/13.jpg"
    filename = argv[0] if len(argv) > 0 else default_file
    # Loads an image
    src = cv.imread(filename, cv.IMREAD_COLOR)
    src_0 = cv.imread(filename,0)
    #cv.imshow("ss", src)

    # Check if image is loaded fine
    if src is None:
        print ('Error opening image!')
        print ('Usage: hough_circle.py [image_name -- default ' + default_file + '] \n')
        return -1
    
    gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
    
    gray = cv.medianBlur(gray, 5)

    
    rows = gray.shape[0]
    circles = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, 1,200)
    
    if circles is not None:
        circles = np.uint16(np.around(circles))
        for i in circles[0, :]:
            center = (i[0], i[1])
            i[2]=i[2]+4
            # circle center
            cv.circle(src, center, 1, (0, 255, 0), 5)
            # circle outline
            radius = i[2]
            cv.circle(src, center, radius, (0, 255, 0), 5)
           
    
    cv.imshow("detected circles", src)
    cv.waitKey(0)
    
    return 0
if __name__ == "__main__":
    main(sys.argv[1:])
