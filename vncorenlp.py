from vncorenlp import VnCoreNLP

# Đường dẫn đến file jar của VnCoreNLP
vncorenlp_path = "VnCoreNLP-master/VnCoreNLP-master/VnCoreNLP-1.1.1.jar"
annotator = VnCoreNLP(vncorenlp_path)
def tokenize_vietnamese(text):
    # Tokenize văn bản tiếng Việt
    tokens = annotator.tokenize(text)
    return tokens

# Sử dụng tokenizer của VnCoreNLP cho tiếng Việt
text = "Xin chào, đây là một ví dụ về tokenize tiếng Việt."
tokens = tokenize_vietnamese(text)
print(tokens)
