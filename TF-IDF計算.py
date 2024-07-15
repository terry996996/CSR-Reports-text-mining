# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 18:50:46 2024

@author: wangh
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 23:44:33 2024

@author: terry
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 13:05:47 2023

@author: terry
"""

import os
import pandas as pd
from jieba.analyse import extract_tags

# 定義計算 TF-IDF 的函數
def calculate_tfidf(text, target_word):
    data = extract_tags(text, topK=10000000000, withWeight=True)
    tfidf_results = []
    for key, weight in data:
        if key == target_word:
            tfidf_results.append(weight)
    return tfidf_results

# 指定主目錄路徑
main_directory = r'C:\Users\wangh\舊電腦的資料\E new\碩論結果撰寫1'

# 要計算的特定字詞
target_word = "汙染"

# 建立空的 DataFrame
columns = ['檔案名稱', f"特定字詞 '{target_word}' 的 TF-IDF 值"]
df = pd.DataFrame(columns=columns)

# 遍歷主目錄下的所有txt檔案
for file_name in os.listdir(main_directory):
    if file_name.endswith('.txt'):
        txt_file_path = os.path.join(main_directory, file_name)
        
        # 讀取檔案並計算TF-IDF
        with open(txt_file_path, 'r', encoding='utf-8') as file:
            s = file.read()
            tfidf_results = calculate_tfidf(s, target_word)
            if tfidf_results:
                temp_df = pd.DataFrame({'檔案名稱': [file_name], f"特定字詞 '{target_word}' 的 TF-IDF 值": [tfidf_results[0]]})
                df = pd.concat([df, temp_df], ignore_index=True)
                print(df)

output_csv_path = os.path.join(main_directory, 'output汙染2.csv')
df.to_csv(output_csv_path, index=False)
print("DataFrame 已儲存為 CSV 檔案:", output_csv_path)