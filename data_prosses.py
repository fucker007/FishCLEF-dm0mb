# _*_ coding: utf-8 _*_
import os
import cv2
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element
from xml.etree.ElementTree import SubElement
from xml.etree.ElementTree import ElementTree

def prettyXml(element, indent, newline, level = 0):
    if element:
        if element.text == None or element.text.isspace():
            element.text = newline + indent * (level + 1)
        else:
            element.text = newline + indent * (level + 1) + element.text.strip() + newline + indent * (level + 1)
    temp = list(element) 
    for subelement in temp:
        if temp.index(subelement) < (len(temp) - 1):
            subelement.tail = newline + indent * (level + 1)
        else: 
            subelement.tail = newline + indent * level
        prettyXml(subelement, indent, newline, level = level + 1)

def save_info(file_name, frame_id, save_id, img_info):
    all_list = img_info['all_list']
    cap = cv2.VideoCapture(file_name)
    cap.set(cv2.CAP_PROP_POS_FRAMES, int(frame_id))
    is_right, frame = cap.read()
    if is_right:
        cv2.imwrite(os.path.join("VOCdevkit/VOC2015/JPEGImages/",save_id+".png"), frame)
        write_xml("VOCdevkit/VOC2015/Annotations/"+save_id+".xml", img_info)
    

def write_xml(file_path, info_img):
    annotation = Element('annotation')
    size = SubElement(annotation, 'size')
    width = SubElement(size, 'width')
    width.text = str(info_img['width'])
    height  = SubElement(size, 'height')
    height.text = str(info_img['height'])
    for box in info_img['all_list']:
        box_xml = SubElement(annotation, 'object')
        name_xml = SubElement(box_xml, 'name')
        name_xml.text = box['fish_species']
        bndbox = SubElement(box_xml, 'bndbox')
        xmin = SubElement(bndbox, 'xmin')
        xmin.text = str(box['x'])
        ymin = SubElement(bndbox, 'ymin')
        ymin.text = str(box['y'])
        xmax = SubElement(bndbox, 'xmax')
        xmax.text = str(box['x'] + box['w'])
        ymax = SubElement(bndbox, 'ymax')
        ymax.text =  str(box['y'] + box['h'])
    tree = ElementTree(annotation )
    root = tree.getroot()
    prettyXml(root, '\t', '\n')
    # write out xml data
    tree.write(file_path, encoding = 'utf-8')

def get_frame_and_bbox(set_, name, id_):
    video_path = os.path.join(os.path.join(set_, "videos"),id_+".flv") 
    xml_path = os.path.join(os.path.join(set_, "gt"),id_+".xml") 
    in_file = open(xml_path)
    tree = ET.parse(in_file)
    root =  tree.getroot()
    print(tree)
    save_id = 1
    for item in root.iter('video'):
        frames = item.findall("frame")
        for frame in frames:
            frame_id = frame.get('id')
            print("frmae id:", frame_id)
            objs = frame.findall('object')
            all_list=[]
            for obj in objs:
                bbox = dict(
                    fish_species = obj.get(name),
                    x = int(obj.get("x")),
                    y = int(obj.get("y")),
                    w = int(obj.get("w")),
                    h = int(obj.get("h")),
                )
                all_list.append(bbox)
                print("fish_species: %s -> x -> %s y ->%s w ->%s h -> %s" % (bbox['fish_species'], bbox['x'] ,bbox['y'], bbox['w'],bbox['h']))
            img_info = dict(
                    width = 640, 
                    height = 480, 
                    depth = 3,
                    all_list =  all_list
                    )
            save_info(video_path, frame_id, id_+'_'+str(frame_id)+'_'+str(save_id), img_info)
            save_id += 1


def read_xml(): 
    sets = [("test_set", "species_name")]
    os.makedirs("VOCdevkit/VOC2015/JPEGImages/")
    os.makedirs("VOCdevkit/VOC2015/Annotations/")
    for set_, name in sets:
        for xml in os.listdir(os.path.join(set_, "gt")):
            id_, _ = xml.split(".")
            print(id_)
            get_frame_and_bbox(set_, name, id_)

if __name__ == "__main__":
    read_xml()



