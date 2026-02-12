import requests
from bs4 import BeautifulSoup
import json
import xml.etree.ElementTree as ET

def get_real_updates():
    # Sử dụng RSS Feed của GSMArena để lấy tin mới nhất về Software/OS
    RSS_URL = "https://www.gsmarena.com/rss-news-software.php3"
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    try:
        response = requests.get(RSS_URL, headers=headers)
        # Parse XML từ RSS
        root = ET.fromstring(response.content)
        
        updates_list = []
        
        # Duyệt qua các tin tức mới nhất (item)
        for item in root.findall('./channel/item')[:10]: # Lấy 10 tin mới nhất
            title = item.find('title').text
            link = item.find('link').text
            pub_date = item.find('pubDate').text
            
            # Phân loại đơn giản dựa trên tiêu đề tin tức
            brand = "Tech News"
            if "iOS" in title or "iPhone" in title:
                brand = "Apple"
            elif "Samsung" in title or "One UI" in title:
                brand = "Samsung"
            elif "Xiaomi" in title or "HyperOS" in title:
                brand = "Xiaomi"
            elif "Android" in title:
                brand = "Google"

            updates_list.append({
                "brand": brand,
                "device": title, # Tiêu đề bài báo thường chứa tên thiết bị
                "version": "Check link for details",
                "date": pub_date,
                "link": link,
                "status": "Latest Update"
            })
            
        return updates_list
    except Exception as e:
        print(f"Lỗi khi cào dữ liệu: {e}")
        return []

def save_to_json(data):
    if data:
        with open('updates.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print(f"Đã cập nhật {len(data)} tin tức mới nhất vào updates.json")
    else:
        print("Không có dữ liệu mới để lưu.")

if __name__ == "__main__":
    news_data = get_real_updates()
    save_to_json(news_data)
