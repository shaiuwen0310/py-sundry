import cv2
import numpy as np

# 讀圖片
img = cv2.imread("7w.jpg", cv2.IMREAD_COLOR)
img_h, img_w, _ = img.shape

# 讀yolo檔案，並且換算坐標
f = open("7w.txt", "r")
for x in f:
    l = x.split(' ')
    
    # l[0] 為類別代號，本腳本中不使用

    # 框的中心點X方向 / 影象寬
    box2_x1_ratio = float(l[1])
    # 框的中心點Y方向 / 影象高
    box2_y1_ratio = float(l[2])
    # 框寬 / 影象寬
    box2_width_ratio = float(l[3])
    # 框高 / 影象高
    box2_height_ratio = float(l[4])

    # 框的中心點X方向
    x_center = int(box2_x1_ratio * img_w)
    # 框的中心點Y方向
    y_center = int(box2_y1_ratio * img_h)
    # 框寬
    w = int(box2_width_ratio * img_w)
    # 框高
    h = int(box2_height_ratio * img_h)

    # 左上角座標
    x_left_up = int((x_center - (0.5 * w)))
    y_left_up = int(y_center - (0.5 * h))

    # 右下角座標
    x_right_bottom = int(x_center + (0.5 * w))
    y_right_bottom = int(y_center + (0.5 * h))

    cv2.rectangle(img, (x_left_up, y_left_up), (x_right_bottom, y_right_bottom), (255, 255, 0), 2)

cv2.imshow('myimg', img)
cv2.waitKey(0)
cv2.destroyAllWindows()