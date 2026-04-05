import requests
import os

API_URL = "https://lazy-birds-follow.loca.lt/predict"

TEST_IMAGES = ["test_images/tree.jpeg", "test_images/a.png", "test_images/dua.jpeg"]  

def test_api():
    for image_path in TEST_IMAGES:
        if not os.path.exists(image_path):
            print(f"[-] Không tìm thấy ảnh: {image_path}")
            continue
            
        print(f"[*] Đang suy luận ảnh: {image_path}")
        with open(image_path, "rb") as f:
            files = {"file": (os.path.basename(image_path), f, "image/jpeg")}
            response = requests.post(API_URL, files=files)
            
        if response.status_code == 200:
            print(f"[+] Kết quả: {response.json()}\n")
        else:
            print(f"[-] Lỗi {response.status_code}: {response.text}\n")

if __name__ == "__main__":
    test_api()
