import warnings
warnings.filterwarnings('ignore')
import cv2

tracker=cv2.TrackerKCF_create()
tracker_name=str(tracker).split()[0][1:]

cap=cv2.VideoCapture("single_tracking.mp4")
ret,frame=cap.read()
roi=cv2.selectROI(frame,False)

# initialsize tracker
ret=tracker.init(frame,roi)

while True:
    ret,frame=cap.read()
    success,roi=tracker.update(frame)
    
    (x,y,w,h)=tuple(map(int,roi))
    
    if success:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),5)
        
    else:
        cv2.putText(frame,"Fail To Detect",(200,300),cv2.FONT_HERSHEY_SIMPLEX,2,(0,0,255),4)
        
    cv2.putText(frame,tracker_name,(100,400),cv2.FONT_HERSHEY_SIMPLEX,2,(0,0,255),4)
    cv2.imshow(tracker_name,frame)
    
    if cv2.waitKey(50) & 0xff==27:
        break
        
cap.release()
cv2.destroyAllWindows()