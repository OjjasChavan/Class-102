# import cv2

# def take_snapshot():
#     VideoCaptureObject = cv2.VideoCapture(0)
#     result = True
    
#     while(result):
#         ret, frame = VideoCaptureObject.read()
#         cv2.imwrite("ojjas.jpg", frame)
#         result = False

#     VideoCaptureObject.release()
#     cv2.destroyAllWindows()

# take_snapshot()

import cv2

def take_pic():
    image = cv2.VideoCapture(0)
    result = True

    while(result):
        ret, frame = image.read()
        cv2.imwrite("ojjas.jpg", frame)
        result = False

    image.release()
    cv2.destroyAllWindows()

take_pic()