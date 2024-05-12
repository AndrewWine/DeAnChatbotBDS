import re
import nltk
import unicodedata
from nltk.corpus import stopwords
from partd import numpy

from main import stemmer


def preprocess_text(text):
    # Loại bỏ dấu câu và dấu nặng
    text = re.sub(r'[^\w\s]', '', text)

    # Chuẩn hóa văn bản
    text = text.lower()

    # Loại bỏ dấu tiếng Việt
    text = unicodedata.normalize('NFD', text).encode('ascii', 'ignore').decode("utf-8")

    # Tách từ
    words = nltk.word_tokenize(text)

    # Loại bỏ từ dừng
    words = [word for word in words if word not in stopwords.words('english')]

    # Stemming
    words = [stemmer.stem(word) for word in words]

    # Kết hợp lại thành câu
    processed_text = ' '.join(words)

    return processed_text




# Nhận dữ liệu nhập vào từ người dùng và tiền xử lý
user_input = input("Nhập vào văn bản cần tiền xử lý: ")
processed_text = preprocess_text(user_input)
print(processed_text)

# Tiếp tục với phần mã của bạn
# Load dữ liệu từ file JSON


# Tiếp tục với phần còn lại của mã của bạn...
