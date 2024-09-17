import cv2

def count_available_cameras():
    count = 0
    while True:
        print(f"hi {count}")
        # Try to open a camera at index 'count'
        cap = cv2.VideoCapture(count)
        print(cap.isOpened())
        if not cap.isOpened():
            print(f"error found")
            count -= 1
            break
        count += 1
        cap.release()  # Release the camera once detected


    return count

camera_count = count_available_cameras()
print(f"Number of available cameras: {camera_count}")
