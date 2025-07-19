# Importations  
import streamlit as st
import cv2
import cvzone
import mediapipe as mp


# Load the Model
cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

modelFile = "D:\ASL\PROJETs\ML\Object_Detetction\Project3-HaramBlur\gender_net.caffemodel"
configFile = "D:\ASL\PROJETs\ML\Object_Detetction\Project3-HaramBlur\gender_deploy.prototxt"
net = cv2.dnn.readNet(modelFile, configFile)
genderList = ['Male', 'Female']
colors ={'pink':(255,0,255),'green' :(0,255,0) }

# Define the  predict Function 
def predict_gender(image):

    mp_face_detection = mp.solutions.face_detection
    mp_drawing = mp.solutions.drawing_utils
    with mp_face_detection.FaceDetection(model_selection=0, min_detection_confidence=0.5) as face_detection:
  
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = face_detection.process(image_rgb)

        if results.detections:
            for detection in results.detections:
                bbox = detection.location_data.relative_bounding_box
                h, w, _ = image.shape
                x = int(bbox.xmin * w)
                y = int(bbox.ymin * h)
                width = int(bbox.width * w)
                height = int(bbox.height * h)

                face = image[y:y+height, x:x+width]
                # Detect if the face is a women or a Men 
                blob = cv2.dnn.blobFromImage(face,1,(227,227),(78.4263377603, 87.7689143744, 114.895847746))
                net.setInput(blob)
                genderPreds = net.forward()
                gender = genderList[genderPreds[0].argmax()]

                if gender == 'Female':
                    image[y:y+height, x:x+width] = cv2.GaussianBlur(face, (99, 99), 30)
                    cv2.rectangle(image, (x, y), (x+width, y+height), color=colors["pink"], thickness=2)
                    cvzone.putTextRect(image,f'Gender: {gender}',(x,y-20),2,2,colorR=colors['pink'])
                else :  
                    cvzone.cornerRect(image,(x,y,width,height),colorR=colors['green'])
                    cvzone.putTextRect(image,f'Gender: {gender}',(x,y-20),2,2,colorR=colors['green'])
        
    return image

st.title("Haram Blur ❤️")

# Affciher le Meesage
if "first_run" not in st.session_state:
    st.session_state.first_run =True 
if st.session_state.first_run:
    st.toast("Welcome to Haram Real_Time Blur ❤️", icon="🙈")
    st.session_state.first_run = False

# You can access the value at any point with:
name = st.text_input("Your name", key="namee")
if name :
    st.success(f"Hello **{name}** , This applcation is For u Muslim To Lower Your GAZE ❤️")


st.divider()

# Initialiser l’état de la webcam
if "cam_active" not in st.session_state:
    st.session_state.cam_active = False

if 'cap' not in st.session_state:
    st.session_state.cap = None

# Afficher le bouton de lancement de la webcam 
with st.container():
    left_column, middle_column ,right_column = st.columns([2,3,2])
    # You can use a column just like st.sidebar:
    with left_column: 
        if  st.button('🎥Lancer la webcam',type='primary') :
            st.session_state.cam_active = True
            st.session_state.cap = cv2.VideoCapture(0)
            st.toast("Webcam lancée ✅")


    with right_column:
        if st.button('🛑Stop la webcam') :
            if st.session_state.cap is not None:
                st.session_state.cap.release()
                st.session_state.cap = None
                st.toast("Webcam fermée ❌")
            st.session_state.cam_active = False


st.divider()

# Placeholder pour l'image de la webcam

FRAME_WINDOW = st.empty()

# Add a placeholder
while st.session_state.cam_active and st.session_state.cap is not None:
    
    ret, frame = st.session_state.cap.read()
    if ret:
        result_frame = predict_gender(frame)
        FRAME_WINDOW.image(result_frame, channels='BGR')
else :
    FRAME_WINDOW.empty()
    

