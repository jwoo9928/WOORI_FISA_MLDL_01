import os
import shutil
import pandas as pd

# CSV 파일 로드
csv_file = 'archive/train.csv'  # train.csv 파일 경로
df = pd.read_csv(csv_file)

# 이미지가 있는 폴더 경로 (원본 이미지 경로)
image_folder = 'archive/'  # 이미지 폴더 경로

output_folder_1 = '1/'
output_folder_0 = '0/'
os.makedirs(output_folder_1, exist_ok=True)
os.makedirs(output_folder_0, exist_ok=True)

# 200개씩 반복하여 처리
chunk_size = 200
for start in range(0, len(df), chunk_size):
    end = start + chunk_size
    chunk_df = df.iloc[start:end]  # 200개씩 잘라서 처리

    # 이미지 파일을 1, 0 폴더로 이동
    for _, row in chunk_df.iterrows():
        image_file = row['file_name']  # CSV에서 파일명 가져오기
        label = row['label']  # 레이블 가져오기

        # 이미지 파일의 전체 경로 생성
        image_path = os.path.join(image_folder, image_file)

        # 레이블에 따라 폴더로 이동
        if label == 1:
            destination_folder = output_folder_1
        elif label == 0:
            destination_folder = output_folder_0

        # 대상 폴더가 없다면 생성
        destination = os.path.join(destination_folder, image_file)
        os.makedirs(os.path.dirname(destination), exist_ok=True)  # 폴더가 없으면 생성

        # 이미지 이동
        if os.path.exists(image_path):
            shutil.move(image_path, destination)
            print(f"Moved {image_file} to {destination}")
        else:
            print(f"Image {image_file} not found!")

print("Image sorting complete.")
