import json
import os
import requests

from filter_update import filter_data_update

def update_data(tag):
    tg = ["update", "Update", "cap nhat"]
    if any(t in tag for t in tg):
            for filename in os.listdir("fileScrapped"):
                if filename.endswith(".txt"):
                    # Tách tên tag từ tên file
                    tag_from_file = filename[:-4]

                    # URL cần lấy dữ liệu
                    url = 'https://muaban.net/bat-dong-san/' + tag_from_file + '-ha-noi?q=hanoi'

                    # Thông tin xác thực
                    username = 'vanh34'
                    apiKey = 'h3l61yzVHP3BsKh82h4s7a0po'

                    apiEndPoint = "http://api.scraping-bot.io/scrape/raw-html"

                    # Tùy chọn cấu hình
                    options = {
                        "useChrome": False,
                        "premiumProxy": False,
                        "proxyCountry": None,
                        "waitForNetworkRequests": False
                    }

                    # Chuẩn bị payload dưới dạng JSON
                    payload = json.dumps({"url": url, "options": options})

                    # Cài đặt tiêu đề của yêu cầu
                    headers = {
                        'Content-Type': "application/json"
                    }

                    # Gửi yêu cầu POST tới API endpoint
                    response = requests.post(apiEndPoint, data=payload, auth=(username, apiKey), headers=headers)

                    # Gọi hàm filter_data_update để xử lý dữ liệu
                    filter_data_update(tag_from_file)
                    # Thêm tag_from_file vào đây

            # Gọi hàm để chạy một lần đầu tiên và cập nhật dữ liệu từ các file txt hiện có
