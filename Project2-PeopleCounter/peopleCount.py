import cv2 
import cvzone
import math
from ultralytics import YOLO
from sort import *


def main():
    
    all_classes = []
    with open("D:\ASL\PROJETs\ML\Object_Detetction\YOLO Basics\80Classes.txt","r") as f:
        all_classes = f.read().splitlines()


    cap = cv2.VideoCapture("D:/ASL/PROJETs/ML/Object_Detetction/videos/people.mp4") # Open The Video = '0'
    #time.sleep(5)

    cap.set(cv2.CAP_PROP_FRAME_WIDTH,1280) # Width is equal to 1280 pixels 
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT,720)

    #create instance of SORT
    tracker = Sort(max_age=10 ,min_hits=4,iou_threshold=0.5) 

    model =YOLO("D:\ASL\PROJETs\ML\Object_Detetction\Yolo-Weights\yolov8s.pt")

    mask = cv2.imread("D:\ASL\PROJETs\ML\Object_Detetction\Project2-PeopleCounter\mask_people.png")
    limitsDown =[(400,297),(673,297)]
    limitsUp =[(150,225),(365,225)]


    totalCountDown = []
    totalCountUp = []
    while True:

        success,frame = cap.read()
        if success:
            img_region = cv2.bitwise_and(frame,mask)
            results =model.predict(img_region, stream=True)

            # carLabel =cv2.imread("graphics.png",cv2.IMREAD_UNCHANGED)
            # frame =cvzone.overlayPNG(frame,carLabel,(0,0))

            detections = np.empty((0,5))
            cv2.line(frame,limitsDown[0],limitsDown[1],(255,255,255),2)
            cv2.line(frame,limitsUp[0],limitsUp[1],(255,255,255),2)

            centers = []
            for r in results :
                boxes = r.boxes # Len Boxes = Number Of Objects
                for box in boxes:
                    x1,y1,x2,y2 = box.xyxy[0]
                    x1,y1,x2,y2 = int(x1),int(y1),int(x2),int(y2)
                    w, h = x2-x1, y2-y1
                    
                    # Frame Info :classe , conf 
                    cls = int(box.cls[0])
                    class_detected = all_classes[cls]
                    conf = math.ceil(box.conf[0]*100)/100 
                    
                    # Display only the Permitted classes
                    if class_detected == "person" and conf >0.5 :
                        
                        # Track the Object Detected Only    
                        currentArray = np.array([x1,y1,x2,y2,conf])
                        detections = np.vstack((detections, currentArray))
                        
                        # # Display the Bounding Box
                        #cvzone.putTextRect(frame,f"{class_detected} {conf} ",(x1,y1+30),colorR=(0,255,0),colorB=(0,0,0),scale=0.8,thickness=1,offset=5)
                        cvzone.cornerRect(frame,(x1,y1,w,h),colorR=(255,255,255),rt=1,l=10)
                        cx ,cy = x1+w//2,y1+h//2
                        cv2.circle(frame,(cx,cy),5,(0,255,0),cv2.FILLED)
                        #centers.append([cx,cy])
                        
            resultsTrackers = tracker.update(detections)
            
            for i,results in enumerate(resultsTrackers):
                
                x1,y1,x2,y2,id = results
                x1,y1,x2,y2,id = int(x1),int(y1),int(x2),int(y2),int(id)
                cx ,cy = x1+w//2,y1+h//2
                #cvzone.cornerRect(frame,(x1,y1,w,h),colorR=(255,0,0),rt=1,l=10)
                cvzone.putTextRect(frame,str(id),(x1,y1),colorR=(255,0,0),colorB=(255,255,255),scale=1,thickness=2,offset=5) 
                #cv2.circle(frame,(cx,cy),5,(0,255,0),cv2.FILLED)
                if limitsDown[0][1] -5<= cy <limitsDown[0][1]  and limitsDown[0][0] <= cx <= limitsDown[1][0]:
                    if id not in totalCountDown:
                        totalCountDown.append(id)
                        cv2.line(frame,limitsDown[0],limitsDown[1],(0,0,255),10)

                if limitsUp[0][1] -5<= cy <limitsUp[0][1]+15  and limitsUp[0][0] <= cx <= limitsUp[1][0]:
                    print(f'Up Set Ids : {len(totalCountUp)} ')
                    if  totalCountUp.count(id) == 0:
                        totalCountUp.append(id)
                        cv2.line(frame,limitsUp[0],limitsUp[1],(0,255,0),10)
                    
            
            cvzone.putTextRect(frame,f"Down : {len(totalCountDown)}",(980,80),colorR=(0,0,255),colorB=(0,0,0),scale=4,thickness=3,offset=10)
            cvzone.putTextRect(frame,f"Up :{len(totalCountUp)}",(980,160),colorR=(0,255,0),colorB=(0,0,0),scale=4,thickness=3,offset=10)
            

            cv2.imshow("frame",frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                cv2.destroyAllWindows()
                cap.release()
                break
        else : 
            cv2.destroyAllWindows()
            cap.release()
            break

if __name__ == "__main__":
    main()
