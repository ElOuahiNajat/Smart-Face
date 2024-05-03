import cv2
import numpy as np
import database
import face_recognition
import datetime

# Function to recognize faces in a frame
def recognize_faces_in_frame(known_face_encodings, img):
    rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    face_locations = face_recognition.face_locations(rgb_img)
    if len(face_locations) == 0:
        return False, None, None

    face_encodings = face_recognition.face_encodings(rgb_img, face_locations)
    match_index = None
    face_loc = None

    for i, face_encoding in enumerate(face_encodings):
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        if True in matches:
            match_index = matches.index(True)
            face_loc = face_locations[i]
            break

    if match_index is not None:
        return True, match_index, face_loc
    else:
        return False, None, None

# Function to find face encodings
def findEncodings(images):
    encodeList = []
    for img in images:
        if img is not None:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            encode = face_recognition.face_encodings(img)[0]
            encodeList.append(encode)
    return encodeList


# Database configuration
host = 'localhost'
database_name = 'face_smart'
user = 'root'
password = ''
table_name = 'employee'

connection = database.connect_to_database(host, database_name, user, password)

images, ids = database.fetch_images_from_database(connection, table_name)

encode_list_known = findEncodings(images)

print('Encoding Complete.')

start_time = None
end_time = None
total_time = datetime.timedelta(0)

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

while True:
    ret, img = cap.read()

    if not ret:
        print("Failed to capture frame")
        break

    # Check if the captured frame is empty
    if img is None:
        print("Empty frame captured")
        continue  # Skip processing this frame

    is_face_detected, match_index, face_loc = recognize_faces_in_frame(encode_list_known, img)

    if is_face_detected:
        if start_time is None:
            start_time = datetime.datetime.now()

        if match_index is not None:
            person_id, person_name = ids[match_index]
            y1, x2, y2, x1 = face_loc
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(img, person_name, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    else:
        if start_time is not None:
            end_time = datetime.datetime.now()

    cv2.imshow('Smart Face', img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        end_time = datetime.datetime.now()
        break

if start_time is not None and end_time is not None:
    total_time += end_time - start_time

print(f'Total Time: {total_time}')

cap.release()
cv2.destroyAllWindows()

if connection.is_connected():
    connection.close()
    print("MySQL connection closed")
