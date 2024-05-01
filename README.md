# CSR-Reports-text-mining
學術用途專案，以文字探勘相關技術針對國內現有(截至2023年)各家企業所出版公告的CSR報告書文本執行一系列分析與詞彙議題研究，捕捉產業特性在報告書當中具體存在的價值與軌跡。

核心技術包括:斷詞處理、詞頻分析、文字雲、詞頻反詞頻(TF-IDF)等

# 文字檔轉換

# 斷詞
處理上使用jieba套件，引用內建前綴詞典檔案(dict.txt.big，https://github.com/fxsjy/jieba/blob/master/extra_dict/dict.txt.big)，結合本論文新增之CSR常見詞彙作斷詞依據，針對存在詞典內字詞以字典樹方式完成分割，不在詞典內字詞則以隱藏式馬可夫模型(HMM)處理。

停用語的移除作業上以Goto456於Github開源的中文停用語表(https://github.com/goto456/stopwords/blob/master/cn_stopwords.txt)結合人工判讀增修後的文檔完成移除操作，強化斷詞精確性。

# 詞頻統計與文字雲

# TF-IDF

# 統計分析
