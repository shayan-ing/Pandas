import chardet
import pandas as pd
# Detect the encoding of the file
with open("E:\\DADS\\PYthon\\Datasets-main\\company.csv", 'rb') as f:
    result = chardet.detect(f.read())
    file_encoding = result['encoding']

print(f"Detected file encoding: {file_encoding}")

# Now, read the CSV file with the detected encoding
data = pd.read_csv("E:\\DADS\\PYthon\\Datasets-main\\company.csv", encoding=file_encoding)
print(data)