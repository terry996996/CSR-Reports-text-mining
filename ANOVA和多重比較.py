# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 23:10:09 2023

@author: terry
"""

import pandas as pd
from statsmodels.stats.multicomp import pairwise_tukeyhsd

df = pd.read_excel("E:/碩論結果專區2/1029/論文取用資料/關鍵字TF-IDF資料預處理結果(排除只有一筆資料的產業組別).xlsx")

# 获取除 '產業別' 列以外的所有列
columns_to_compare = df.columns[3:]

# 指定 Excel 檔案的完整路徑，包括檔案名稱
excel_file_path = "E:/碩論結果專區2/1029/論文取用資料/rejected_results_0.01_columns.xlsx"

# 创建一个 ExcelWriter 对象，用于将每次循环的结果保存到同一文件
excel_writer = pd.ExcelWriter(excel_file_path, engine='xlsxwriter')

# 逐列进行多重比较
for column in columns_to_compare:
    print(f"Performing Tukey's HSD for column: {column}")
    
    # 执行 Tukey's HSD 多重比较
    tukey_result = pairwise_tukeyhsd(endog=df[column],
                                      groups=df['產業別'],
                                      alpha=0.01)

    # 将结果转换为数据框
    tukey_df = pd.DataFrame(data=tukey_result._results_table.data[1:],
                             columns=tukey_result._results_table.data[0])

    # 过滤出 reject 为 True 的部分
    rejected_data = tukey_df[tukey_df['reject']]

    # 打印结果
    print(rejected_data)
    
    # 將拒絕的結果保存到 ExcelWriter 中的新工作表
    rejected_data.to_excel(excel_writer, sheet_name=column, index=False)
    
    print(f"Rejected results saved to sheet: {column}")
    print("\n" + "="*50 + "\n")

# 保存 ExcelWriter 对象中的所有工作表
excel_writer.save()

# 关闭 ExcelWriter 对象
excel_writer.close()

print(f"Excel file saved to: {excel_file_path}")
