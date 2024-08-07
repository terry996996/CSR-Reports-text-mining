# CSR-Reports-text-mining
學術用途專案，以文字探勘相關技術針對國內現有(截至2023年)各家企業所出版公告的CSR報告書文本執行一系列分析與詞彙議題研究，捕捉產業特性在報告書當中具體存在的價值與軌跡。

核心技術包括:斷詞處理、詞頻分析、文字雲、詞頻反詞頻(TF-IDF)等

論文摘要:

  企業社會責任(Corporate Social Responsibility，CSR)已是當今公司治理的一項顯學，隨 著其概念主張蓬勃演進，相關範疇主題成了國內外文獻熱切探討標的，而關於企業如何落實 具體行動及傳達想法主張上欲供對外利害關係人了解的面向，出版年度CSR報告書為當今 主流作法，故報告書文本實為蘊含相當豐富且重要的訊息價值，對此本論文使用文字探勘 (Text Mining)方法，針對國內企業出版公告之現有報告書文本，透過資料處理階段定位出的 不同樣本型態文檔為基準，對其中文字內容潛藏之訊號索引進行特徵萃取與捕捉。

  同時，面對整體國家CSR推廣，各產業導入CSR過程中有哪些主力投注焦點和特色，從CSR報告書裡的資訊揭露狀態和特定議題著墨情形亦可得出深刻體察，因此本論文即以詞頻分析與文字雲、詞頻與反詞頻(TF-IDF)演算技術這些經典關鍵詞研究方法，配合社會科學上更為嚴謹的變異數分析、多重比較及追蹤資料迴歸實證，進一步對報告書文檔內產業特性展現面貌及在議題設定與資訊揭露成效影響中發揮的作用價值執行完整掌握，從而由內外部角度綜合觀點探討國內不同產業CSR推動風格和報告書文化，旨在從產業面現狀分析，對未來國家CSR值得延續的潛力面向及須正視的重大挑戰環節做深入剖析釐清，希望具體形成政策規劃適切建議，敦請各界共同重視國內CSR發展相關議題與消息。

  而在本論文研究結果中發現國內企業界普遍在CSR推廣上增加環境主軸的熱切投入和關注，是可以有效促進各界對該公司的良好印象和CSR理念上之認可，長期下來提升企業市場競爭力；另外，亦體察到整體國家的CSR推動可能存有過度偏重單一領域的現象，導致報告書撰寫內容存在過於侷限疑慮，進而影響資訊傳遞之品質效果，此類問題也正是當今迫在眉睫須積極面對解決的環節；同時本論文整體的研究重點也證實到產業特性在CSR報告書資訊揭露及趨勢發展上扮演著舉足輕重地位，唯有有效體認產業特性的精髓，才能針對國內不同產業CSR做適性化策略引導及現狀通盤識讀，促使國內未來於各領域CSR面向做均衡的全面性推展之外，同時亦根據產業性質元素，在不同產業的CSR行動指引上做多元化發展，如此來穩健地建構多彩的CSR生態圈，並與國際有效接軌，使國內CSR文化更加成熟且熱絡，體現出最大的企業社會責任意義與精神真諦。

論文連結: https://ndltd.ncl.edu.tw/cgi-bin/gs32/gsweb.cgi/login?o=dnclcdr&s=id=%22112NTPU0303010%22.&searchmode=basic


# 文字檔轉換
原始報告書pdf文檔進行自動化讀檔作業，轉換成逐分txt檔，並經由DOS命令合併成論文中不同型態的階段樣本。

# 斷詞
處理上使用jieba套件，引用Fxsjy於Github開源的內建前綴詞典檔案(dict.txt.big) https://github.com/fxsjy/jieba/blob/master/extra_dict/dict.txt.big
，結合本論文新增之CSR常見詞彙作斷詞依據，針對存在詞典內字詞以字典樹方式完成分割，不在詞典內字詞則以隱藏式馬可夫模型(HMM)處理。

停用語的移除作業上以Goto456於Github開源的中文停用語表 https://github.com/goto456/stopwords/blob/master/cn_stopwords.txt
，結合人工判讀增修後的文檔完成移除操作，強化斷詞精確性。

註:詳細規則請參考本作者text mining專案內"情緒分析.py"裡的應用作法。
# 詞頻統計與文字雲
從中初步捕捉熱門議題，並未國家與產業的CSR關切焦點。
使用python內的word cloud套件進行階段性產製結果調整以及Word Art網站開源的線上編修工具進行製作。

# TF-IDF
進階詞彙訊息提取技術，量化關鍵議題的重視程度特徵。

# 統計分析
以ANOVA和多重比較、追蹤資料迴歸進行內部報告書撰寫特徵與議題設定角度及外部財務績效影響成效上產業特性的具體意涵和價值。
