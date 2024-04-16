import json
from bs4 import BeautifulSoup

# Đọc nội dung của tệp văn bản
with open('Test/response_data.txt', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Phân tích cú pháp HTML
soup = BeautifulSoup(html_content, 'html.parser')

# Lọc các thẻ <a> có class="title"
title_links = soup.find_all('a', class_='title')

# Tạo từ điển để lưu trữ dữ liệu cho text và href
text_dict = {}
href_dict = {}

# Biến đếm để đánh số ID cho mỗi vòng lặp
counter = 1

# Lưu trữ thông tin và thêm vào từ điển
for link in title_links:
    text = link.text
    href = link.get('href')
    # Tạo URL đầy đủ bằng cách thêm https://muaban.net/ vào href
    full_href = f"https://muaban.net{href}"

    # Thêm dữ liệu vào từ điển với ID tương ứng
    text_dict[counter] = text
    href_dict[counter] = full_href

    # Tăng biến đếm lên một sau mỗi vòng lặp
    counter += 1

# Ghi dữ liệu từ điển vào các tệp JSON riêng biệt
# Sử dụng ensure_ascii=False để tránh dấu \ bị thêm vào URL
# Sử dụng indent=4 để định dạng dữ liệu JSON theo cách dễ đọc
with open('text.json', 'w', encoding='utf-8') as text_file:
    json.dump(text_dict, text_file, ensure_ascii=False, indent=4)

with open('href.json', 'w', encoding='utf-8') as href_file:
    json.dump(href_dict, href_file, ensure_ascii=False, indent=4)

print("Dữ liệu đã được lưu vào 'text.json' và 'href.json'")
