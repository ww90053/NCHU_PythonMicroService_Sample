import os
import time
import shutil

#以下範例示範如何將程式

#示範用函數
#inputFileDirPath:輸入檔案資料夾,EX: '/usr/src/app/input/abcd-0000-0000-0001/'
#outFileDirPath:輸出檔案資料夾,EX: '/usr/src/app/output/abcd-0000-0000-0001/'
def exec(inputFileDirPath,outFileDirPath):
    #注意!資料夾內可能會有多個輸入輸出檔案,是代表每次處理的需要多個參數
    #輸入檔有3個,是代表輸入需要三個參數(.txt檔)或檔案

    #輸入檔資料夾內的檔案命名如下    
    # 檔名路徑格式: {輸入檔案資料夾}/input{編號}.{副檔名}
    # EX:
    #   /usr/src/app/input/abcd-0000-0000-0001/input1.txt
    #   /usr/src/app/input/abcd-0000-0000-0001/input2.png
    #   /usr/src/app/input/abcd-0000-0000-0001/input3.txt
    
    #讀取輸入檔案資料夾,這邊只示範抓到檔名並print出來
    #具體要如何使用這些輸入檔案,需勞煩自行實作
    #取得來源目錄下的所有檔案名稱 ,EX: ['input1.txt', 'input2.png', 'input3.txt']
	ndir_files = os.listdir(inputFileDirPath)
	
	for fileName in ndir_files:
		print(f'處理檔案中:{fileName}')
	
	
	
	#這邊關鍵在於要將檔案放置到輸出資料夾,並依照檔案命名
	# 檔名路徑格式: {輸出檔案資料夾}/output{編號}.{副檔名}
	# EX:
	#   /usr/src/app/output/abcd-0000-0000-0001/output1.png
	#   /usr/src/app/output/abcd-0000-0000-0001/output2.png
	#   /usr/src/app/output/abcd-0000-0000-0001/output3.png
	#   /usr/src/app/output/abcd-0000-0000-0001/output4.png	
	shutil.copyfile('./sampleFile/output1.png', os.path.join(outFileDirPath, 'output1.png'))
	shutil.copyfile('./sampleFile/output2.png', os.path.join(outFileDirPath, 'output2.png'))
	shutil.copyfile('./sampleFile/output3.png', os.path.join(outFileDirPath, 'output3.png'))
	shutil.copyfile('./sampleFile/output4.png', os.path.join(outFileDirPath, 'output4.png'))
	

	#執行成功,回傳True
	return True
    
	#如果執行失敗則回傳False,錯誤訊息用print的方式呈現
	#print(f'這邊輸入錯誤訊息')
	#return False
