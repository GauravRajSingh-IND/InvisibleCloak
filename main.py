# import packages
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


# create a video capture object
cap = cv.VideoCapture(0)
if cap.isOpened() == False:
    print("Error in video capture object.")

# create a named window
winName = "Invisible Cloak"
cv.namedWindow(winName)

# Extra parameters
frameCount = 0
background = None
lw_bd = np.array([150, 150, 150], np.uint8)
up_bd = np.array([210, 255, 255], np.uint8)


while True:

    frameCount +=1
    print(frameCount)

    # read frames one by one from video capture object.
    has_frame, frame = cap.read()

    # Create a background by using 10th frame.
    if frameCount == 10:
        background = frame

    # Convert the frame color to HSV from BGR.
    frame_hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    # Create a mask using inRange Function.
    if frameCount >= 10:
        mask = cv.inRange(frame_hsv, lw_bd, up_bd)
        bg_frame = cv.bitwise_and(background, background, mask = mask)
        fg_frame = cv.bitwise_and(frame, frame, mask = cv.bitwise_not(mask))

        # Final frame.
        frame_result = cv.bitwise_or(bg_frame, fg_frame)

    if not has_frame:
        print("No frame to read.")

    # Display each frame one by one.
    if frameCount <= 10:
        cv.imshow(winName, frame)
    else:
        cv.imshow(winName, frame_result)
    key = cv.waitKey(1)

    # Break the loop if user enter Q or esc key.
    if key == 'Q' or key == 'q' or key == 27:
        break

cap.release()
cv.destroyAllWindows()
    
