import face_recognition
import os
import cv2


KNOWN_FACES_DIR = "known face"
UNKNOWN_FACES_DIR = "unknown face"
TOLERANCE = 0.6
FRAME_THICKNESS = 3
FONT_THICKNESS = 2
MODEL = "hog" 

print("Loading known faces...")

known_faces = []
known_names = []


for filename in os.listdir(KNOWN_FACES_DIR):
    if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
        image_path = os.path.join(KNOWN_FACES_DIR, filename)
        image = face_recognition.load_image_file(image_path)
        encodings = face_recognition.face_encodings(image)

        if encodings:
            known_faces.append(encodings[0])
            name = os.path.splitext(filename)[0]  
            known_names.append(name)
        else:
            print(f"[WARNING] No face found in {filename}, skipping...")

print("Processing unknown faces...")

for filename in os.listdir(UNKNOWN_FACES_DIR):
    if not filename.lower().endswith(('.jpg', '.jpeg', '.png')):
        continue

    print(f"Processing {filename}")
    image_path = os.path.join(UNKNOWN_FACES_DIR, filename)
    image = face_recognition.load_image_file(image_path)
    locations = face_recognition.face_locations(image, model=MODEL)
    encodings = face_recognition.face_encodings(image, locations)

    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    for face_encoding, face_location in zip(encodings, locations):
        results = face_recognition.compare_faces(known_faces, face_encoding, TOLERANCE)
        match = None

        if True in results:
            match = known_names[results.index(True)]
            print(f"Match found: {match}")

            
            top_left = (face_location[3], face_location[0])
            bottom_right = (face_location[1], face_location[2])
            color = [0, 255, 0]
            cv2.rectangle(image, top_left, bottom_right, color, FRAME_THICKNESS)

            
            label_top_left = (face_location[3], face_location[2])
            label_bottom_right = (face_location[1], face_location[2] + 22)
            cv2.rectangle(image, label_top_left, label_bottom_right, color, cv2.FILLED)
            cv2.putText(image, match, (face_location[3] + 10, face_location[2] + 15),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (200, 200, 200), FONT_THICKNESS)

    cv2.imshow(filename, image)
    cv2.waitKey(5000)
    cv2.destroyWindow(filename)
