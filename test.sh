CUDA_VISIBLE_DEVICES=1 python test.py --weights weights/yolov3-spp-ultralytics.pt --batch-size 32 --save-json \
--data data/coco2017.data --cfg cfg/yolov3-spp.cfg --img-size 608 --iou-thres 0.6