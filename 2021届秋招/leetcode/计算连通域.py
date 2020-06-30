import cv2
from glob import glob
import numpy as np
from PIL import Image

# root = "/media/aries/新加卷/uestc项目/54所遥感项目/彭清/seg_img/data_all_xa/9.4标注/标注/"
root="/media/aries/0F20176E0F20176E/data_all/遥感数据/54所项目数据_6.19/成都数据/labels/"
# root="/home/aries/图片/111111.png"

extension = "*.png"
name = glob(root + extension)
print(name)
res = [0] * 8
#
palette=[0,0,0,  ##背景
         200,0,0,##建筑
         0,0,200,##水体
         0,100,0,##草地
         0,250,0,##森林
         150,250,0,##田地
         255,255,255,   ##道路
         0,150,250]##裸地

for file_name in name:
    # img = cv2.imread(file_name)
    # print(img.shape)
    img=Image.open(file_name)
    img=np.array(img)
    # img = np.squeeze(img[:, :, 0])
    print(img.shape)
    # cv2.imshow("test",img)
    # cv2.waitKey(0)
    temp = [0] * 8
    for thr in [0.5,1.5,2.5,3.5,4.5,5.5,6.5,7.5]:
        ret, th1 = cv2.threshold(img, thr, 0, cv2.THRESH_TOZERO_INV)
        #大于阈值的设定为0 小于阈值的不变

        ret, th1 = cv2.threshold(th1, thr-1,0, cv2.THRESH_TOZERO)
        #小于阈值的设定为0,大于阈值的不变
        ret, th1 = cv2.threshold(th1, thr-1, 255, cv2.THRESH_BINARY)
        # print(ret,th1)
        # kernel = np.ones((5, 5), np.uint8)
        # opening = cv2.morphologyEx(th1, cv2.MORPH_OPEN, kernel)
        img_show=Image.fromarray(th1*10)
        Image._show(img_show)
        # cv2.imshow('th1', th1)
        # cv2.waitKey(0)
        #
        # cv2.imshow('opening', opening)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()

        # opening = np.array(opening, np.uint8)
        contours, hierarchy = cv2.findContours(th1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        temp[int(thr-1.5)] += len(contours)
    res = [res[i] + temp[i] for i in range(8)]
print(res)
#[0, 163220, 127248, 102529, 68443, 7901, 3343, 0]

# root1="/home/aries/图片/1.png"
# img=cv2.imread(root1)
# print(img.shape)
# # cv2.imshow("test",img)
# gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# cv2.imshow("gray",gray_img)
# cv2.waitKey(0)
# ret,th1=cv2.threshold(gray_img,120,255,cv2.THRESH_BINARY)
# cv2.imshow('th1',th1)
# cv2.waitKey(0)
# print(ret,th1)
#
#
# kernel = np.ones((5,5),np.uint8)
# opening = cv2.morphologyEx(th1, cv2.MORPH_OPEN, kernel)
# cv2.imshow('opening',opening)
# opening = np.array(opening,np.uint8)
# contours, hierarchy = cv2.findContours(opening,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
# print(len(contours))
