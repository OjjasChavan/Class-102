import cv2 
import dropbox
import time 
import random

start_time = time.time()
def take_snapshot():
    number = random.randint(1, 100)
    VideoCaptureObject = cv2.VideoCapture(0)
    result = True
    
    while(result):
        ret, frame = VideoCaptureObject.read()
        image_name = 'img' + str(number) + '.jpg'
        cv2.imwrite(image_name, frame)
        start_time = time.time()
        result = False

    return image_name
    print("Snapshot taken!")
    VideoCaptureObject.release()
    cv2.destroyAllWindows()

def upload_file(image_name):
    access_token = "https://www.dropbox.com/scl/fo/xwfciidvvy3840wb1l75w/h?dl=0&rlkey=bii4lwq0p1glpifult3kxzzky"
    dbx = dropbox.Dropbox("access_token")
    file = image_name
    file_from = file
    file_to = "/" + (image_name)
    dex = dropbox.Dropbox(access_token)

    with open(file_from, 'rb') as f:
        dbx.files_upload(f.read(), file_to, mode=dropbox.files.WriteMode.overwrite)
        print("File uploaded!")


def main():
    while(True):
        if ((time.time() - start_time) >= 300):
            name = take_snapshot()
            upload_file(name)
        
main()