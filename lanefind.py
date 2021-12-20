import cv2 as cv
import numpy as np
import lanes


video = cv.VideoCapture(0)
x = 320
y = 240

while True:
    _, frame = video.read()
    cv.namedWindow("Video", cv.WINDOW_NORMAL)
    cv.resizeWindow("Video", 640, 480)



    try:
        copy_img = np.copy(frame)
        frame = lanes.region_of_interest(frame)
        frame = lanes.canny(frame)
        lines = cv.HoughLinesP(frame, 2, np.pi/180, 100, np.array([()]), minLineLength=50, maxLineGap=5) #кадр, точность в пикселях, радиан, нижний порог, массив, минимальная длина линии(шум), допустимое расстояние)
        average_lines = lanes.average_slope_intercept(frame, lines)

        line_image = lanes.display_lines(copy_img, average_lines)
        combo = cv.addWeighted(copy_img, 0.8, line_image, 0.5, 1)
        cv.imshow("Video", combo)
    except Exception:
        pass


    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cv.destroyAllWindows()
video.release()
