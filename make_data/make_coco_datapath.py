# -*- coding: utf-8 -*-
import os

if __name__ == '__main__':
    datasetname = 'val'
    year = '2014'
    data_dir = '/home/Yolo/yolov/data' # the yolo code data path

    path1 = "/train/trainset/1/mscoco{}/{}{}".format(year, datasetname, year) #图片的文件夹
    namepath = data_dir+"/coco{}/images/{}{}".format(year, datasetname, year)
    txtpath = data_dir+"/coco{}/".format(year) + "{}.txt".format(datasetname) #放入的txt文件
    allfile1 = os.listdir(path1)
    with open(txtpath, 'a+') as fp:
        for name in allfile1:
            newpath = os.path.join(namepath, name)
            fp.write("".join(newpath) + "\n")

