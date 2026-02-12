import requests
import json
import xml.etree.ElementTree as ET

def get_real_updates():
    # Sử dụng RSS Feed của GSMArena để lấy tin mới nhất về Phần mềm/OS
    RSS_URL = "https://www.gsmarena.com/rss-news-software.php3"
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    try:
        response = requests.get(RSS_URL, headers=headers)
        # Parse XML từ RSS Feed
        root = ET.fromstring(response.content)
        
        updates_list = []
        
        # Duyệt qua 12 tin tức mới nhất
        for item in root.findall('./channel/item')[:12]: 
            title = item.find('title').text
            link = item.find('link').text
            pub_date = item.find('pubDate').text
            
            # Phân loại hãng dựa trên từ khóa trong tiêu đề
            brand = "Công nghệ"
            title_lower = title.lower()
            
            if any(x in title_lower for x in ["ios", "iphone", "apple", "ipad"]):
                brand = "Apple"
            elif any(x in title_lower for x in ["samsung", "one ui", "galaxy"]):
                brand = "Samsung"
            elif any(x in title_lower for x in ["xiaomi", "hyperos", "redmi"]):
                brand = "Xiaomi"
            elif any(x in title_lower for x in ["android", "google", "pixel"]):
                brand = "Google"
            elif "oppo" in title_lower:
                brand = "Oppo"

            updates_list.append({
                "brand": brand,
                "title": title,
                "date": pub_date,
                "link": link
            })
            
        return updates_list
    except Exception as e:
        print(f"Lỗi: {e}")
        return []

def save_to_json(data):
    if data:
        with open('updates.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print(f"Thành công! Đã lưu {len(data)} tin vào updates.json")

if __name__ == "__main__":
    data = get_real_updates()
    save_to_json(data)
