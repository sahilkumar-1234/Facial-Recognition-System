# # import cv2
# # import numpy as np 
# # import face_recognition
# # import os
# # from datetime import datetime

# # path = "C:/Users/sahil/OneDrive/Documents/chindiprojects python/Facial Recog attendance sys/Images"
# # images = []
# # names=[]

# # for file in os,listdir(path):
# #     img = cv2.imread(f'{path}/{file}')
# #     images.append(img)
# #     names.append(os.path.splittext(file)[0])
    
# # def encode_faces(images):
# #     encoded= []
# #     for img in images:
# #         img_rgb = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
# #         encodes= face_recognition.face_encodings(img_rgb)
# #         if encodes:
# #             encoded.append(encodes[0])
# #     return encoded

# # known_encodings = encode_faces(images)

# # def mark_attendance(name):
# #     with open('Attendance.csv','a+') as f:# a+ these allows appending and the reading of the file if file doesnt exists it will create it
# #         f.seek(0)# file pointer ko 0 se start karati hai taki poori file read kaar sake
# #         data= f.readlines()# these will read the every file line in the list form
# #         recorded = [line.split(',')][0]
         
# #         for line in data:
# #                 # harr lin me se naam ko extract karna
# #             if name not in recorded:
                
# #                 now = datetime.now()# gets the curetn date and the time
# #                 time = now.strftime('%H:%M:%S')#formatting the time and the date
# #                 date = now.strftime('%d-%m-%Y')
# #                 f.write(f'{name},{date},{time}\n')#add the attendance  in the attendance file
 
# # cap= cv2.VideoCapture(0,cv2.CAP_DSHOW)

# # while True:
# #     success, frame= cap.read()
# #     rgb_small = cv2.cvtcolor(small,cv2.COLOR_BGR2RGB)
    
# #     faces_loc = face_recognition.face_locations(rgb_small)
# #     encodings = face_recognition.face_encodings(rgb_small,face_loc)
    
# #     for encode , face_loc in zip(encodings,faces_loc):
# #         matches = face_recognition.compare_faces(known_encodings,encode)
# #         distances = face_recognition.face_distance(known_encodings,encode)
        
# #         match_index = np.argmin(distances)
        
# #         if matches[match_index]:
# #             name = names[match_index]
            
# #             y1,x2,y2,x1 = face_loc
# #             y1,x2,y2,x1 = y1*4,x2*4,y2*4,x1*4
# #             cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),2)
# #             cv2.putText(frame, name, (x1,y1-10),cv2.FONT_HERSHEY_SIMPLEX,(0,255,0),2)
# #             mark_attendance(name)
            
# #     cv2.imshow('Face Recognition Attendance',frame)
    
# #     if cv2.waitkey(1)==27:
# #         break
    
# # cap.release()
# # cv2.destroyAllWindows()

#_____________________________________________________________________________________________________________________________
#a better version of it

# import cv2
# import numpy as np 
# import face_recognition
# import os
# from datetime import datetime



# path = "C:/Users/sahil/OneDrive/Documents/chindiprojects python/Facial Recog attendance sys/Images"
# images = []
# names = []

# for file in os.listdir(path):
#     img = cv2.imread(f'{path}/{file}')
#     images.append(img)
#     names.append(os.path.splitext(file)[0])

# def encode_faces(images):
#     encoded = []
#     for img in images:
#         img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#         encodes = face_recognition.face_encodings(img_rgb)
#         if encodes:
#             encoded.append(encodes[0])
#     return encoded

# known_encodings = encode_faces(images)

# def mark_attendance(name):
#     with open('Attendance.csv', 'a+') as f:
#         f.seek(0)
#         data = f.readlines()
#         recorded = [line.split(',')[0] for line in data]
#         if name not in recorded:
#             now = datetime.now()
#             time = now.strftime('%H:%M:%S')
#             date = now.strftime('%d-%m-%Y')
#             f.write(f'{name},{date},{time}\n')

# cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# while True:
#     success, frame = cap.read()
#     small = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
#     rgb_small = cv2.cvtColor(small, cv2.COLOR_BGR2RGB)

#     faces_loc = face_recognition.face_locations(rgb_small)
#     encodings = face_recognition.face_encodings(rgb_small, faces_loc)

#     for encode, face_loc in zip(encodings, faces_loc):
#         matches = face_recognition.compare_faces(known_encodings, encode)
#         distances = face_recognition.face_distance(known_encodings, encode)
#         match_index = np.argmin(distances)

#         if matches[match_index]:
#             name = names[match_index]
#             y1, x2, y2, x1 = face_loc
#             y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4
#             cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
#             cv2.putText(frame, name, (x1, y1-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
#             mark_attendance(name)

#     cv2.imshow('Face Recognition Attendance', frame)
#     if cv2.waitKey(1) == 27:
#         break

# cap.release()
# cv2.destroyAllWindows()


#________________________________________________________________________________________________________________
#tried a different version with fixing the laggy issues...

import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime
import time
print("Video Panel is Loading....")
# Load known faces
path = "C:/Users/sahil/OneDrive/Documents/chindiprojects python/Facial Recog attendance sys/Images"
images = []
names = []

for file in os.listdir(path):
    img = cv2.imread(f'{path}/{file}')
    if img is None:
        continue
    images.append(img)
    names.append(os.path.splitext(file)[0])

def encode_faces(images):
    encoded = []
    for img in images:
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encodes = face_recognition.face_encodings(img_rgb)
        if encodes:
            encoded.append(encodes[0])
    return encoded

known_encodings = encode_faces(images)

def mark_attendance(name):
    with open('Attendance.csv', 'a+') as f:
        f.seek(0)
        data = f.readlines()
        recorded = [line.split(',')[0] for line in data]
        if name not in recorded:
            now = datetime.now()
            time_str = now.strftime('%H:%M:%S')
            date_str = now.strftime('%d-%m-%Y')
            f.write(f'{name},{date_str},{time_str}\n')

# Start webcam

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# Variables to control frame processing
frame_count = 0
process_every_n_frames = 3  # Process every 3rd frame to reduce lag

while True:
    success, frame = cap.read()
    if not success:
        break

    # Resize frame for faster processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

    if frame_count % process_every_n_frames == 0:
        # Only process this frame
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for encode_face, face_loc in zip(face_encodings, face_locations):
            matches = face_recognition.compare_faces(known_encodings, encode_face)
            distances = face_recognition.face_distance(known_encodings, encode_face)

            name = "Unknown"
            if matches:
                best_match_index = np.argmin(distances)
                if matches[best_match_index]:
                    name = names[best_match_index]
                    mark_attendance(name)

            face_names.append((name, face_loc))

    # Draw rectangles and labels
    for name, (top, right, bottom, left) in face_names:
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    cv2.imshow('Face Recognition Attendance', frame)
    frame_count += 1

    # Exit on ESC key
    if cv2.waitKey(1) & 0xFF == 27:
        break
cap.release()
cv2.destroyAllWindows()

