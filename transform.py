import cv2
import os
import numpy as np
from tqdm import tqdm

img_path = 'Data'
trans_path = 'AugData'
img_list = os.listdir(img_path)


for img_name in tqdm(img_list):
    img = cv2.imread(os.path.join(img_path, img_name))
    cv2.imwrite(os.path.join(trans_path, img_name)[:-7] + '_0_gt.bmp', img)

    img1 = np.array(img)[::-1]
    cv2.imwrite(os.path.join(trans_path, img_name)[:-7] + '_1_gt.bmp', img1)

    img2 = np.array(img)[:, ::-1]
    cv2.imwrite(os.path.join(trans_path, img_name)[:-7] + '_2_gt.bmp', img2)

    img3 = np.array(img1)[:, ::-1]
    cv2.imwrite(os.path.join(trans_path, img_name)[:-7] + '_3_gt.bmp', img3)

    img4 = np.array(np.rot90(img))
    cv2.imwrite(os.path.join(trans_path, img_name)[:-7] + '_4_gt.bmp', img4)

    img5 = np.array(img4)[::-1]
    cv2.imwrite(os.path.join(trans_path, img_name)[:-7] + '_5_gt.bmp', img5)

    img6 = np.array(img4)[:, ::-1]
    cv2.imwrite(os.path.join(trans_path, img_name)[:-7] + '_6_gt.bmp', img6)

    img7 = np.array(img5)[:, ::-1]
    cv2.imwrite(os.path.join(trans_path, img_name)[:-7] + '_7_gt.bmp', img7)
