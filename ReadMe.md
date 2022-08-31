
# 國立中興大學農業大數據平台-Python程式微服務範例
## 概念說明
- 此範例主要是讓python程式可在本平台作為可被呼叫的微服務
- 原理主要是透過K8S呼叫容器內的python程式
	- 具體指令為：python main.py {GUID}
	- {GUID}在這邊可以當作一組隨機變數，傳遞給微服務程式之後可用來區分不同次呼叫的輸入輸出資料夾
	- 例如：python main.py abcd-0000-0000-0007
- 外部呼叫微服務程式的步驟具體如下
	- 傳遞需要辨識的檔案到input資料夾（輸入輸出檔案與資料夾需要一些命名上的限制）
	- 呼叫並傳遞GUID給微服務程式
	- 等待最後微服務程式print finish，訊息代表執行結束
		- 如果出錯則print error代表錯誤
	- 到輸出資料夾抓取產出的檔案

## 範例檔案與資料夾說明

### main.py
	主程式,基本照抄即可,只有以下兩段需要替換成自己實作的部分
	#實驗室自行實作之程式檔引用,請參考demo.py,視實際情況替換之
	#呼叫範例用的函數,這邊需勞煩實驗室自行實作之
	
### demo.py
	demo用的範例,裡面只是產生測試用的範例檔案
	這邊需勞煩實驗室自行實作之

### unittest.py
	單元測試用的程式,基本照抄即可,
	跟主程式一樣,也會引用demo.py,
	差別在於此程式的輸入資料夾固定在/unittest_input/
	以便程式封裝成容器化之後,測試是否仍可正常執行

### keepawake.py
	保持服務清醒,讓K8S不會立刻結束執行任務,類似讓它變成服務的效果

### Dockerfile
	Docker封裝的設定檔
	這邊需勞煩實驗室自行視情況調整之

### /input/
	輸入用的資料夾,裡面會再用guid區分不同批的辨識
### /output/
	輸出用的資料夾,裡面會再用guid區分不同批的辨識
### /unittest_input/
	單元測試用的輸入資料夾
### /unittest_output/
	單元測試用的輸出資料夾

## 程式規範說明
### 程式路徑限制
- 上述程式與資料夾配置路徑請放在/usr/src/app/ 之下,以便容器化佈署之後方便呼叫
- 主程式務必命名為 main.py

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


### Container封裝說明
	因為自動化佈署需要,ReposityName與TagName需要命名在匯出檔案上
	且dockerhub帳號的部分需要固定使用iscom70598966
#### 封裝指令
	格式 sudo docker build . -t iscom70598966/{ReposityName}:{TagName}
	範例 sudo docker build . -t iscom70598966/allentest:v1
#### 匯出封裝檔案
	格式 sudo docker save -o iscom70598966_{ReposityName}_{TagName} iscom70598966/{ReposityName}:{TagName}
	範例 sudo docker save -o iscom70598966_allentest_v1 iscom70598966/allentest:v1