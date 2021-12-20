import cv2

cam = cv2.VideoCapture(0)
camera_height = 480
camera_width = 640

#x = 480
#y = 640
up_sign = cv2.imread("up.jpg")
up_sign = cv2.resize(up_sign, (40, 40))
up_sign = cv2.inRange(up_sign, (90,90,150), (255,255,255))

left_sign = cv2.imread("left.jpg")
left_sign = cv2.resize(left_sign, (40, 40))
left_sign = cv2.inRange(left_sign, (90,90,150), (255,255,255))

right_sign = cv2.imread("right.jpg")
right_sign = cv2.resize(right_sign, (40, 40))
right_sign = cv2.inRange(right_sign, (90,90,150), (255,255,255))

man_sign = cv2.imread("man.jpg")
man_sign = cv2.resize(man_sign, (40, 40))
man_sign = cv2.inRange(man_sign, (90,90,150), (255,255,255))

stop_sign = cv2.imread("stop.jpg")
stop_sign = cv2.resize(stop_sign, (40, 40))
stop_sign = cv2.inRange(stop_sign, (90,90,150), (255,255,255))

wait_sign = cv2.imread("wait.jpg")
wait_sign = cv2.resize(wait_sign, (40, 40))
wait_sign = cv2.inRange(wait_sign, (90,90,150), (255,255,255))

cancel_sign = cv2.imread("cancel.jpg")
cancel_sign = cv2.resize(cancel_sign, (40, 40))
cancel_sign = cv2.inRange(cancel_sign, (90,90,150), (255,255,255))


while True:
    ret, frame = cam.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    hsv = cv2.blur(hsv, (5,5))

    mask = cv2.inRange(hsv, (80,80,80), (255,255,255))

    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=4)

    contours1, hierarchy1 = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    if contours1:
        image_copy = frame.copy()
        c = max(contours1, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(c)

        sign_from_image = frame[y:y + h, x:x + w]
        sign_from_image = cv2.resize(sign_from_image, (40,40))
        sign_from_image = cv2.inRange(sign_from_image, (90,90,150), (255,255,255))


        cv2.imshow("sign", sign_from_image)
        #cv2.imshow("right", right_sign)
        #cv2.imshow("man", man_sign)
        #cv2.imshow("sign", left_sign)


        counter_up = 0
        counter_right = 0
        counter_left = 0
        counter_man = 0
        counter_stop = 0
        counter_wait = 0
        counter_cancel = 0

        for i in range(40):
            for j in range(40):
                if right_sign[i][j] == sign_from_image[i][j]:
                    counter_right += 1
                if man_sign[i][j] == sign_from_image[i][j]:
                    counter_man += 1
                if left_sign[i][j] == sign_from_image[i][j]:
                    counter_left += 1
                if up_sign[i][j] == sign_from_image[i][j]:
                    counter_up += 1
                if stop_sign[i][j] == sign_from_image[i][j]:
                    counter_stop += 1
                if wait_sign[i][j] == sign_from_image[i][j]:
                    counter_wait += 1
                if cancel_sign[i][j] == sign_from_image[i][j]:
                    counter_cancel += 1


        if counter_right > 1200 and counter_right < 1250:
            print('Знак поворот направо')
        elif counter_left > 1390 and counter_left < 1430:
            print('Знак поворот налево')
        elif counter_up > 1100 and counter_up < 1150:
            print('Знак движение прямо')
        elif counter_stop > 1150 and counter_stop < 1170:
            print('Знак стоп')
        elif counter_wait > 1200 and counter_wait < 1300:
            print('Знак уступи дорогу')
        elif counter_cancel > 1220 and counter_cancel < 1240:
            print('Знак въезд запрещен')
        elif counter_man > 920 and counter_man < 1000:
            print('Знак пешеходного перехода')


    cv2.imshow("Frame", image_copy)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
cam.release()