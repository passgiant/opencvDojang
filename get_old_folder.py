# 날짜_시간 형태로 폴더를 생성하고 
# 가장 오래된 폴더 정렬해서 찾기, 지우기

import os
from datetime import datetime

# 폴더를 생성
# 현재 폴더 아래에 test 폴더를 생성
# test 폴더 아래에 날짜_시간 폴더를 생성

basePath = 'test'

# 폴더 만드는 함수
os.makedirs(basePath, exist_ok=True)

# 현재 시간 가져오기
now = datetime.now()

# 폴더명을 '20240904_11'
# folder_name = now.strftime('%Y%m%d_%H')
for hour in range(24):
    folder_name = now.strftime('%Y%m%d_')
    folder_name += str(hour)
    folder_name = os.path.join(basePath, folder_name)
    os.makedirs(folder_name, exist_ok=True)