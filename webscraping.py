import os
import requests
import json
from FiltersData import filter_data


def scrape_data(tag):
    tz = ["AskName", "greet", "Bye", "Ability", "Instructions", "Update"]
    file_path = f'fileScrapped/{tag}.txt'

    # Kiểm tra nếu tệp dữ liệu đã tồn tại
    if os.path.exists(file_path):
        print(f'Dữ liệu cho tag "{tag}" đã tồn tại.')
        return True

    if tag not in tz:
        # URL cần lấy dữ liệu
        url = 'https://muaban.net/bat-dong-san/' + tag + '-ha-noi?q=hanoi'

        # Thông tin xác thực
        username = 'vanh34'
        apiKey = 'h3l61yzVHP3BsKh82h4s7a0po'





        apiEndPoint = "http://api.scraping-bot.io/scrape/raw-html"

        # Tùy chọn cấu hình
        options = {
            "useChrome": False,  # Đặt thành True nếu muốn sử dụng headless Chrome để render JavaScript.
            "premiumProxy": False,  # Đặt thành True nếu muốn sử dụng proxy cao cấp.
            "proxyCountry": None,  # Chọn proxy theo quốc gia (ví dụ: proxyCountry: "FR").
            "waitForNetworkRequests": False  # Đợi cho hầu hết các yêu cầu mạng Ajax hoàn thành.
        }

        # Chuẩn bị payload dưới dạng JSON
        payload = json.dumps({"url": url, "options": options})

        # Cài đặt tiêu đề của yêu cầu
        headers = {
            'Content-Type': "application/json"
        }

        # Gửi yêu cầu POST tới API endpoint
        response = requests.post(apiEndPoint, data=payload, auth=(username, apiKey), headers=headers)

        # Lưu nội dung của phản hồi vào tệp văn bản
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(response.text)

        # Gọi hàm filter_data để xử lý dữ liệu trong 'response_data.txt'
        filter_data(tag)


# Gọi hàm để chạy

