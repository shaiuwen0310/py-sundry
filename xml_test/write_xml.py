import xml.etree.ElementTree as gfg
import os
import numpy as np
import cv2

image_path = os.path.dirname(__file__) + "/gen_xml/Selection_038.png"
image_coordinate_path = os.path.dirname(__file__) + "/gen_xml/test.txt"

image = cv2.imread(image_path)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
image_h, image_w, image_d = np.shape(image)

################## gen XML ##################
root = gfg.Element("annotation")
gfg.SubElement(root, "filename").text = image_path

m1 = gfg.Element("size")
gfg.SubElement(m1, "width").text = str(image_w)
gfg.SubElement(m1, "height").text = str(image_h)
gfg.SubElement(m1, "depth").text = str(image_d)
root.append(m1)

gfg.SubElement(root, "segmented").text = "0"
################## gen XML ##################

################## gen XML ##################
with open(image_coordinate_path) as f:
    for line in f:
        label_index = int(line.split(" ")[0])
        xmin, ymin, xmax, ymax = int(line.split(" ")[1]), int(line.split(" ")[2]), int(line.split(" ")[3]), int(line.split(" ")[4])

        classes = ['green', 'yellow', 'blue', 'red', 'white', 'orange', 'black', 'gray', 'pink', 'light_blue']
        real_color = classes[label_index]

        ################## gen XML ##################
        m2 = gfg.Element("object")
        gfg.SubElement(m2, "name").text = str(real_color)
        gfg.SubElement(m2, "pose").text = "Unspecified"
        gfg.SubElement(m2, "truncated").text = "0"
        gfg.SubElement(m2, "difficult").text = "0"
        root.append(m2)

        m3 = gfg.Element("bndbox")
        # 擴大 1 pixel
        gfg.SubElement(m3, "xmin").text = str(xmin-1)
        gfg.SubElement(m3, "ymin").text = str(ymin-1)
        gfg.SubElement(m3, "xmax").text = str(xmax+1)
        gfg.SubElement(m3, "ymax").text = str(ymax+1)
        m2.append(m3)
        ################## gen XML ##################

tree = gfg.ElementTree(root)

xml_name = os.path.dirname(__file__) + "/gen_xml/Selection_038.xml"
with open(xml_name, "wb") as files:
    tree.write(files)

