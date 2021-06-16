import cv2
import numpy as np

image_path="圖片.png"
image_store_path="圖片_複製.png"

# image = cv2.imread(image_path)
image = cv2.imdecode(np.fromfile(image_path, dtype=np.uint8), -1)
image_copy = image.copy()

# cv2.imwrite(image_store_path, image_copy)
cv2.imencode('.png', image_copy)[1].tofile(image_store_path)
