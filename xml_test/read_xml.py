import xml.etree.ElementTree as ET
import os

# 資料夾路徑 + 子資料夾路徑
xml_name = os.path.dirname(__file__) + "/read_xml/48498-04-19_1618808690219.xml"

tree = ET.parse(xml_name)
root = tree.getroot()

label_name=[]
# 依序歷遍所有<name></name>的數值
for x in root.iter('name'):
    label_name.append(x.text)
print(label_name)
print(label_name.count("blue"))

# 依序歷遍所有<bndbox></bndbox>的數值
# 並由於<bndbox></bndbox>中又有四個元素，可以用index去抓取其中數值
for i, x in enumerate(root.iter('bndbox'), start=0):
    xmin, ymin, xmax, ymax = int(x[0].text), int(x[1].text), int(x[2].text), int(x[3].text)
    print(xmin, ymin, xmax, ymax)
