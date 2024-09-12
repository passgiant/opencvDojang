# 1. 배경 : 흰색 책상, 우드 테이블
# 2. 데이터 증식 조건 
#    2.0 스마트폰으로 사진 촬영후 이미지 크기를 줄여주자. (이미지 크기 224x224)
#        대상물 촬영을 어떻게 해야할지 확인
#    2.1 rotate : 회전(10~30도)범위 안에서 어느 정도 각도를 넣어야 인식이 잘되는가?
#    2.2 hflip, vflip : 도움이 되는가? 넣을 것인가?
#    2.3 resize, crop : 가능하면 적용해 보자.
#    2.4 파일명을 다르게 저장 cf) jelly_wood.jpg, jelly_white.jpg
#        jelly_wood_rot_15.jpg, jelly_wood_hflip.jpg,jelly_wood_resize.jpg 
#    2.5 클래스 별로 폴더를 생성
#    2.6 데이터를 어떻게 넣느냐에 따라 어떻게 동작되는지 1~2줄로 요약

# 구성 순서 
# 1. 촬영한다.
# 2. 이미지를 컴퓨터로 복사, resize한다.
# 3. 육안으로 확인, 이렇게 사용해도 되는가?
# 4. 함수들을 만든다. resize, rotate, hflip, vflip, crop, 
#    원본파일명을 읽어서 파일명을 생성하는 기능은 모든 함수에 있어야 한다.(함수)
# 5. 단일 함수들 검증
# 6. 함수를 활용해서 기능 구현
# 7. 테스트(경우의수)
# 8. 데이터셋을 teachable machine사이트에 올려서 테스트
# 9. 인식이 잘 안되는 케이스를 분석하고 케이스 추가 1~8에서 구현된 기능을 이용

# resize할 때 interpolation도 적용하기

# 문제점1: 클래스로 만들면 더 좋을 것 같음?
# 문제점2: 경로 변수들이 많음
# 문제점3: 함수 실행시키는 것도 많음

import cv2, sys
import numpy as np
import os
from glob import glob
import shutil

dataPath = os.path.join(os.getcwd(), 'dataAug')

data_b = os.path.join(dataPath, 'bottle')
data_b_Org = os.path.join(data_b, 'org')
data_b_Res = os.path.join(data_b, 'res')
fileNames_b_org = glob(os.path.join(data_b_Org, '*.jpg'))
fileNames_b_res = glob(os.path.join(data_b_Res, '*.jpg'))

data_sb = os.path.join(dataPath, 'sub_battery')
data_sb_Org = os.path.join(data_sb, 'org')
data_sb_Res = os.path.join(data_sb, 'res')
fileNames_sb_org = glob(os.path.join(data_sb_Org, '*.jpg'))
fileNames_sb_res = glob(os.path.join(data_sb_Res, '*.jpg'))

data_t = os.path.join(dataPath, 'timer')
data_t_Org = os.path.join(data_t, 'org')
data_t_Res = os.path.join(data_t, 'res')
fileNames_t_org = glob(os.path.join(data_t_Org, '*.jpg'))
fileNames_t_res = glob(os.path.join(data_t_Res, '*.jpg'))

def fs(fileNames, func_name, aug_type, initial=None):
    if initial == 'b':
        dataPath = data_b
    elif initial == 'sb':
        dataPath = data_sb
    elif initial == 't':
        dataPath = data_t
    dataPath_sub = os.path.join(dataPath, aug_type)
    os.makedirs(dataPath_sub, exist_ok=True)
    for fileName in fileNames:
        f_name = os.path.basename(fileName)
        f_name = f_name.split('.')[0]
        img = cv2.imread(fileName)
        if img is None:
            sys.exit('Image load failed')
        if func_name == random_crop:
            for i in range(250):
                img_changed = func_name(img)
                f_name_ch = f'{f_name}_{aug_type}_{i+1}.jpg'
                fileNamed_ch = os.path.join(dataPath_sub, f_name_ch)
                cv2.imwrite(fileNamed_ch, img_changed)
        else:
            img_changed = func_name(img)
            f_name_ch = f'{f_name}_{aug_type}.jpg'
            fileNamed_ch = os.path.join(dataPath_sub, f_name_ch)
            cv2.imwrite(fileNamed_ch, img_changed)
    
def resize(img):
    dsize = (224,224)
    img_resize_IA = cv2.resize(img, dsize, interpolation=cv2.INTER_AREA)
    return img_resize_IA

def rotate_90(img):
    img_rotated = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
    return img_rotated

def rotate_180(img):
    img_rotated = cv2.rotate(img, cv2.ROTATE_180)
    return img_rotated

def rotate_270(img):
    img_rotated = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
    return img_rotated

def hflip(img, num=1):
    img_hflipped = cv2.flip(img, num)
    # cv2.imshow('img_hflipped', img_hflipped)
    # cv2.waitKey()
    # cv2.destroyAllWindows()
    return img_hflipped
    
def vflip(img, num=0):
    img_vflipped = cv2.flip(img, num)
    # cv2.imshow('img_vflipped', img_vflipped)
    # cv2.waitKey()
    # cv2.destroyAllWindows()
    return img_vflipped
    
def hvflip(img, num=-1):
    img_hvflipped = cv2.flip(img, num)
    # cv2.imshow('img_hvflipped', img_hvflipped)
    # cv2.waitKey()
    # cv2.destroyAllWindows()
    return img_hvflipped

def random_crop(img, crop_height=224, crop_width=224):
    max_x = img.shape[0] - crop_width
    max_y = img.shape[1] - crop_height
    
    x = np.random.randint(0, max_x)
    y = np.random.randint(0, max_y)
    
    img_cropped = img[y:y+crop_height, x:x+crop_width]
    return img_cropped

def brightness_up(img):
    img_bright_up = cv2.add(img, 100)
    return img_bright_up

def brightness_down(img):
    img_bright_down = cv2.add(img, -50)
    return img_bright_down
                
def copy_folders_contents(source_folders, destination_folder):
    os.makedirs(destination_folder, exist_ok=True)
    
    for folder in source_folders:
        for root, dirs, files in os.walk(folder):
            for file in files:
                src_path = os.path.join(root, file)
                dst_path = os.path.join(destination_folder, file)
                shutil.copy2(src_path, dst_path)
        
# 이미지 리사이즈 후 저장(했음, 첫 번째는 for문, 두 번째는 함수 버전)
# for fileName in fileNames_org:
#     f_name = os.path.basename(fileName)
#     img = cv2.imread(fileName)
#     if img is None:
#         sys.exit('Image load failed')
#     img_resized = resize(img)
#     f_name_res = f_name + '_res' + '.jpg'
#     fileNamed_res = os.path.join(dataRes, f_name_res)
#     cv2.imwrite(fileNamed_res, img_resized)

# fs(fileNames_b_org, resize, 'res', 'b')
# fs(fileNames_sb_org, resize, 'res', 'sb')
# fs(fileNames_t_org, resize, 'res', 't')

# 이미지 회전 후 저장(했음, 함수 만들어서 사용함)
# fs(fileNames_b_res, rotate_90, 'rot_90', 'b')
# fs(fileNames_sb_res, rotate_90, 'rot_90', 'sb')
# fs(fileNames_t_res, rotate_90, 'rot_90', 't')

# fs(fileNames_b_res, rotate_180, 'rot_180', 'b')
# fs(fileNames_sb_res, rotate_180, 'rot_180', 'sb')
# fs(fileNames_t_res, rotate_180, 'rot_180', 't')

# fs(fileNames_b_res, rotate_270, 'rot_270', 'b')
# fs(fileNames_sb_res, rotate_270, 'rot_270', 'sb')
# fs(fileNames_t_res, rotate_270, 'rot_270', 't')

# 이미지 flip 후 저장(했음, 함수 만들어서 사용함)
# fs(fileNames_res, hflip, 'hflip')
# fs(fileNames_res, vflip, 'vflip')
# fs(fileNames_res, hvflip, 'hvflip')
# fs(fileNames_b_res, hflip, 'hflip', 'b')
# fs(fileNames_sb_res, hflip, 'hflip', 'sb')
# fs(fileNames_t_res, hflip, 'hflip', 't')

# fs(fileNames_b_res, vflip, 'vflip', 'b')
# fs(fileNames_sb_res, vflip, 'vflip', 'sb')
# fs(fileNames_t_res, vflip, 'vflip', 't')

# fs(fileNames_b_res, hvflip, 'hvflip', 'b')
# fs(fileNames_sb_res, hvflip, 'hvflip', 'sb')
# fs(fileNames_t_res, hvflip, 'hvflip', 't')

# 이미지 random crop 후 저장(폴더는 만들어놨는데 안의 내용물은 삭제함, 이유는 배경이 너무 많이 크롭됨, 따로 물체만 resize한 다음에 다시 시도해볼 것)
# fs(fileNames_org, random_crop, 'random_crop')

# 이미지 밝기 조정 후 저장(했음, 함수 만들어서 사용함)
# fs(fileNames_b_res, brightness_up, 'brightness_up', 'b')
# fs(fileNames_sb_res, brightness_up, 'brightness_up', 'sb')
# fs(fileNames_t_res, brightness_up, 'brightness_up', 't')

# fs(fileNames_b_res, brightness_down, 'brightness_down', 'b')
# fs(fileNames_sb_res, brightness_down, 'brightness_down', 'sb')
# fs(fileNames_t_res, brightness_down, 'brightness_down', 't')

source_folders_b = ['C:/Users/SBA/opencvDojang/dataAug/bottle/res', 
                    'C:/Users/SBA/opencvDojang/dataAug/bottle/rot_90', 
                    'C:/Users/SBA/opencvDojang/dataAug/bottle/rot_180', 
                    'C:/Users/SBA/opencvDojang/dataAug/bottle/rot_270', 
                    'C:/Users/SBA/opencvDojang/dataAug/bottle/hflip', 
                    'C:/Users/SBA/opencvDojang/dataAug/bottle/vflip', 
                    'C:/Users/SBA/opencvDojang/dataAug/bottle/hvflip', 
                    'C:/Users/SBA/opencvDojang/dataAug/bottle/brightness_up', 
                    'C:/Users/SBA/opencvDojang/dataAug/bottle/brightness_down']
destination_folder_b = 'C:/Users/SBA/opencvDojang/dataAug/bottle/submit'
source_folders_sb = ['C:/Users/SBA/opencvDojang/dataAug/sub_battery/res', 
                    'C:/Users/SBA/opencvDojang/dataAug/sub_battery/rot_90', 
                    'C:/Users/SBA/opencvDojang/dataAug/sub_battery/rot_180', 
                    'C:/Users/SBA/opencvDojang/dataAug/sub_battery/rot_270', 
                    'C:/Users/SBA/opencvDojang/dataAug/sub_battery/hflip', 
                    'C:/Users/SBA/opencvDojang/dataAug/sub_battery/vflip', 
                    'C:/Users/SBA/opencvDojang/dataAug/sub_battery/hvflip', 
                    'C:/Users/SBA/opencvDojang/dataAug/sub_battery/brightness_up', 
                    'C:/Users/SBA/opencvDojang/dataAug/sub_battery/brightness_down']
destination_folder_sb = 'C:/Users/SBA/opencvDojang/dataAug/sub_battery/submit'
source_folders_t = ['C:/Users/SBA/opencvDojang/dataAug/timer/res', 
                    'C:/Users/SBA/opencvDojang/dataAug/timer/rot_90', 
                    'C:/Users/SBA/opencvDojang/dataAug/timer/rot_180', 
                    'C:/Users/SBA/opencvDojang/dataAug/timer/rot_270', 
                    'C:/Users/SBA/opencvDojang/dataAug/timer/hflip', 
                    'C:/Users/SBA/opencvDojang/dataAug/timer/vflip', 
                    'C:/Users/SBA/opencvDojang/dataAug/timer/hvflip', 
                    'C:/Users/SBA/opencvDojang/dataAug/timer/brightness_up', 
                    'C:/Users/SBA/opencvDojang/dataAug/timer/brightness_down']
destination_folder_t = 'C:/Users/SBA/opencvDojang/dataAug/timer/submit'

# copy_folders_contents(source_folders_b, destination_folder_b)
# copy_folders_contents(source_folders_sb, destination_folder_sb)
# copy_folders_contents(source_folders_t, destination_folder_t)