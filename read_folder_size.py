import os

def get_folder_size(folder_path):
  """
  특정 폴더의 크기를 바이트 단위로 계산합니다.

  Args:
    folder_path: 크기를 계산할 폴더의 경로입니다.

  Returns:
    폴더의 총 크기 (바이트)입니다. 폴더가 존재하지 않으면 0을 반환합니다.
  """

  total_size = 0
  if os.path.exists(folder_path):
    for dirpath, dirnames, filenames in os.walk(folder_path):
      for f in filenames:
        fp = os.path.join(dirpath, f)
        total_size += os.path.getsize(fp)

  return total_size

# 사용 예시
folder_path = "C:/Users/SBA/opencvDojang/data"  # 확인하려는 폴더 경로로 변경
folder_size_bytes = get_folder_size(folder_path)

if folder_size_bytes == 0:
  print(f"'{folder_path}' 경로가 존재하지 않습니다.")
else:
  # 바이트를 KB, MB, GB로 변환하여 출력
  folder_size_kb = folder_size_bytes / 1024
  folder_size_mb = folder_size_kb / 1024
  folder_size_gb = folder_size_mb / 1024
  
  print(f"'{folder_path}' 폴더의 크기:")
  print(f"- {folder_size_bytes} 바이트")
  print(f"- {folder_size_kb:.2f} KB")
  print(f"- {folder_size_mb:.2f} MB")
  print(f"- {folder_size_gb:.2f} GB")