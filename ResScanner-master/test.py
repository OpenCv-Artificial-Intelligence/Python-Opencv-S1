import numpy as np
import cv2

# define the list of boundaries
# boundaries = [
# 	((0, 0, 0) 	, (179, 255, 93)),
# 	((0, 90, 10)    , (15, 250, 100)),
# 	((0, 30, 80)    , (10, 255, 200)),
# 	((10, 70, 70)   , (25, 255, 200)),
# 	((30, 170, 100) , (40, 250, 255)),
# 	((35, 20, 110)  , (60, 45, 120)),
# 	((65, 0, 85)    , (115, 30, 147)),
# 	((120, 40, 100) , (140, 250, 220)),
# 	((0, 0, 50)     , (179, 50, 80)),
# 	((0, 0, 90)     , (179, 15, 250))
# ]

boundaries = [
                [(0, 0, 0)      , (179, 255, 93)  , "BLACK"  , 0 , (0,0,0)       ],    
                [(0, 90, 10)    , (15, 250, 100)  , "BROWN"  , 1 , (0,51,102)    ],    
                [(0, 30, 80)    , (10, 255, 200)  , "RED"    , 2 , (0,0,255)     ],
                [(10, 70, 70)   , (25, 255, 200)  , "ORANGE" , 3 , (0,128,255)   ], 
                [(30, 170, 100) , (40, 250, 255)  , "YELLOW" , 4 , (0,255,255)   ],
                [(35, 20, 110)  , (60, 45, 120)   , "GREEN"  , 5 , (0,255,0)     ],  
                [(65, 0, 85)    , (115, 30, 147)  , "BLUE"   , 6 , (255,0,0)     ],  
                [(120, 40, 100) , (140, 250, 220) , "PURPLE" , 7 , (255,0,127)   ], 
                [(0, 0, 50)     , (179, 50, 80)   , "GRAY"   , 8 , (128,128,128) ],      
                [(0, 0, 90)     , (179, 15, 250)  , "WHITE"  , 9 , (255,255,255) ]
];

RED_TOP_LOWER = (160, 30, 80)
RED_TOP_UPPER = (179, 255, 200)

rez = cv2.imread("img/rez.jpg")

# blue_upper = np.array([255, 65, 65])
# blue_lower = np.array([200, 0, 0])

# red_upper = np.array([65, 65, 255])
# red_lower = np.array([0, 0, 200])

# green_upper = np.array([65, 255, 65])
# green_lower = np.array([0, 200, 0])

# white_upper = np.array([255, 255, 255])
# white_lower = np.array([200, 200, 200])

# black_upper = np.array([65, 65, 65])
# black_lower = np.array([0, 0, 0])

upper = red_upper
lower = red_lower

mask = cv2.inRange(rez, lower, upper)
rez, cnts, hierarchy = cv2.findContours(mask.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

c = max(cnts, key=cv2.contourArea)
peri = cv2.arcLength(c, True)
approx = cv2.approxPolyDP(c, 0.05 * peri, True)
cv2.drawContours(rez, [approx], -1, (0, 255, 0), 4)

cv2.imshow("Image",rez)
cv2.waitKey()
cv2.destroyAllWindows()


