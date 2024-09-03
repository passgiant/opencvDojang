import os

# 루트 폴더 경로 설정
folder_path = "C:/Users/SBA/opencvDojang/ex1"  # 원하는 폴더 경로로 변경

# os.walk를 사용하여 폴더 구조 순회
for dirpath, dirnames, filenames in os.walk(folder_path):
    # 현재 폴더 정보 출력
    print(f"현재 폴더: {dirpath}")

    # 현재 폴더의 하위 폴더 목록 출력
    print("하위 폴더:", dirnames)

    # 현재 폴더의 파일 목록 출력
    print("파일:", filenames)
    print("-" * 30) 