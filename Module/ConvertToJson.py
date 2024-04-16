import json

# Đọc dữ liệu từ file text
with open('../Test/scraped_data.txt', 'r', encoding='utf-8') as f:
    data = f.read().split('\n\n')  # Split by empty lines

# Chuyển dữ liệu sang dạng list, mỗi item trong list là một đoạn văn đã scrap
data = [item.replace('\n', ' ') for item in data]

# Chuyển đổi dữ liệu sang kiểu dictionary
data_dict = {"data": data}

# Ghi dictionary xuống file JSON
with open('../Test/scraped_data.json', 'w', encoding='utf-8') as json_file:
    json.dump(data_dict, json_file, ensure_ascii=False, indent=4)