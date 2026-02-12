import requests
import json
import xml.etree.ElementTree as ET

def get_real_updates():
    RSS_URL = "https://www.gsmarena.com/rss-news-software.php3"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    try:
        response = requests.get(RSS_URL, headers=headers)
        root = ET.fromstring(response.content)
        updates_list = []
        for item in root.findall('./channel/item')[:15]: 
            title = item.find('title').text
            link = item.find('link').text
            pub_date = item.find('pubDate').text
            t = title.lower()
            brand = "Công nghệ"
            if any(x in t for x in ["ios", "apple", "iphone", "macbook"]): brand = "Apple"
            elif any(x in t for x in ["samsung", "galaxy", "one ui"]): brand = "Samsung"
            elif any(x in t for x in ["xiaomi", "hyperos", "redmi", "poco"]): brand = "Xiaomi"
            elif any(x in t for x in ["android", "pixel", "google"]): brand = "Google"
            elif "oppo" in t: brand = "Oppo"
            elif "vivo" in t: brand = "Vivo"
            updates_list.append({
                "brand": brand,
                "title": title,
                "date": pub_date,
                "link": link
            })
        return updates_list
    except Exception as e:
        print(f"Lỗi cào dữ liệu: {e}")
        return []

def save_to_json(data):
    with open('updates.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print(f"Đã cập nhật {len(data)} tin tức mới nhất!")

if __name__ == "__main__":
    news_data = get_real_updates()
    save_to_json(news_data)
