import cv2

a=cv2.VideoCapture(0)
while True:
	_, img=a.read()
	cv2.imshow(" my face detection",img)
	if cv2 . waitKey(1) & 0xFF==ord('q'):
		break
a.release()
