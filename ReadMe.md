
# 國立中興大學農業大數據平台-Python程式微服務範例
## 概念說明
- 因為介接上的需要,一些輸入和輸出的檔案需要放置在指令路徑
- 微服務程式會接收一組由外部程式隨機產生的GUID,用來區分不同次呼叫的輸入輸出資料夾
- 讀取到輸入檔案,並且產出執行結果檔案後,請放置到對應GUID的輸出資料夾
- 最後print finish訊息代表執行結束
- 如果出錯則print error代表錯誤
## 程式限制規範說明
### 程式路徑限制
- 主程式務必命名為 main.py
- 程式配置路徑請放在/usr/src/app/ 之下,以便容器化佈署之後方便抓取

### 輸入與輸出的檔案皆需要依照指定路徑放置
#### 輸入資料夾命名
    /usr/src/app/input/{GUID}/
#### 輸出資料夾命名
    /usr/src/app/output/{GUID}/

    EX: 
    GUID=abcd-1234-0000-0001
    則輸入檔案路徑則為:
    /usr/src/app/input/abcd-0000-0000-0001/
    則輸出檔案路徑則為:
    /usr/src/app/output/abcd-0000-0000-0001/

#### 輸入檔案命名
	/{輸入檔案資料夾}/input{編號}.{副檔名}
	注意!資料夾內可能會有多個輸入輸出檔案,是代表每次處理的需要多個參數
    假設輸入檔有3個檔案,是代表每次辨識需要輸入三個檔案
    EX:
	輸入範例
    /usr/src/app/input/abcd-0000-0000-0001/input1.txt
    /usr/src/app/input/abcd-0000-0000-0001/input2.png
    /usr/src/app/input/abcd-0000-0000-0001/input3.txt
#### 輸出檔案命名	
	/{輸出檔案資料夾}/output{編號}.{副檔名}
	輸出範例
	/usr/src/app/output/abcd-0000-0000-0001/output1.txt
	/usr/src/app/output/abcd-0000-0000-0001/output2.txt
	/usr/src/app/output/abcd-0000-0000-0001/output3.txt
	/usr/src/app/output/abcd-0000-0000-0001/output4.txt


## 範例檔案與資料夾說明

### main.py
	主程式,基本照抄即可,只有以下兩段需要替換成自己實作的部分
	#實驗室自行實作之程式檔引用,請參考demo.py,視實際情況替換之
	#呼叫範例用的函數,這邊需勞煩實驗室自行實作之
	
### demo.py
	demo用的範例,裡面只是產生測試用的範例檔案

### input
	輸入用的範例資料夾,僅供開發端使用,實際佈署之後會放在別的資料夾
### output
	輸出用的資料夾,僅供開發端使用,實際佈署之後會放在別的資料夾