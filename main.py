import requests
from bs4 import BeautifulSoup
import json

def get_latest_updates():
    # URL ví dụ (giả lập)
    data = [
        {"brand": "Samsung", "device": "Galaxy S24 Ultra", "version": "One UI 8", "status": "Stable"},
        {"brand": "Apple", "device": "iPhone 15 Pro", "version": "iOS 19", "status": "Stable"}
    ]

    # Lưu vào file JSON
    with open('updates.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print("Đã tạo file updates.json thành công!")

if __name__ == "__main__":
    get_latest_updates()
