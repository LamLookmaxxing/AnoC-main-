import os

folder_path = 'home/static/home'  # Thay thế bằng đường dẫn tới thư mục của bạn

for root, dirs, files in os.walk(folder_path):
    for file_name in files:
        print(os.path.join(root, file_name))