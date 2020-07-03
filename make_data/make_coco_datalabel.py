from __future__ import print_function
import os, sys
import json
from pycocotools.coco import COCO


def convert(size, box):
    dw = 1. / (size[0])
    dh = 1. / (size[1])
    x = box[0] + box[2] / 2.0
    y = box[1] + box[3] / 2.0
    w = box[2]
    h = box[3]

    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return (x, y, w, h)


datasetname = 'val'
year = '2017'
json_file = '/train/trainset/1/mscoco{}/annotations/instances_{}{}.json'.format(year, datasetname, year)  # # Object Instance 类型的标注

data = json.load(open(json_file, 'r'))

ana_txt_save_path = "/home/Yolo/yolov/data/coco{}/labels/{}{}".format(year,datasetname,year)  # 保存的路径
if not os.path.exists(ana_txt_save_path):
    os.makedirs(ana_txt_save_path)

coco = COCO(json_file)
json_category_id_to_contiguous_id = {
        v: i + 1 for i, v in enumerate(coco.getCatIds())
    }

for i, img in enumerate(data['images']):
    # print(img["file_name"])
    filename = img["file_name"]
    img_width = img["width"]
    img_height = img["height"]
    # print(img["height"])
    # print(img["width"])
    img_id = img["id"]
    ana_txt_name = filename.split(".")[0] + ".txt"  # 对应的txt名字，与jpg一致
    if i %1000==0:
        print(i)
    f_txt = open(os.path.join(ana_txt_save_path, ana_txt_name), 'w')

    annIds = coco.getAnnIds(imgIds=img_id)
    anns = coco.loadAnns(annIds)
    if len(anns)>0:
        for ann in anns:
            box = convert((img_width, img_height), ann["bbox"])
            f_txt.write("%s %s %s %s %s\n" % (json_category_id_to_contiguous_id[ann["category_id"]]-1, box[0], box[1], box[2], box[3]))

    else:
        print(ana_txt_name)
    f_txt.close()


