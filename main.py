import os
#import time
import sys
# 實驗室自行實作之程式檔引用,請參考demo.py,視實際情況替換之
import demo

# 以下範例示範如何將程式
# 限制: 輸入輸出的檔案路徑必須一致


# 相對路徑輸入輸出資料夾
DATA_PATH = './input'
PROCESSED_DIR = './output'


def Main():
    # 抓取輸入參數GUID,
    # 此GUID是在呼叫此程式之前隨機產生,用於資料夾命名
    # 目的是讓每次呼叫,可以讓不同次的輸入輸出依照資料夾放好
    # EX:
    # GUID=abcd-1234-0000-0001
    # 則輸入檔案路徑則為:
    # './input/abcd-0000-0000-0001/'

    # 先檢查有沒有輸入?
    if (len(sys.argv) < 2):
        print(f'please intput argument for a guid')
        print(f'error')
        return False

    GUID = sys.argv[1]
    print(sys.argv[1])

    # 拼接 輸入檔路徑資料夾, EX: './input/abcd-0000-0000-0001/'
    inputFileDir = os.path.join(DATA_PATH, GUID)
    # 如果 輸入檔路徑資料夾不存在,後面不處理了
    if (not os.path.isdir(inputFileDir)):
        print(f'{inputFileDir} not exist')
        print(f'error')
        return False
    # 拼接 輸出檔路徑資料夾, EX: './output/abcd-0000-0000-0001/'
    outFileDir = os.path.join(PROCESSED_DIR, GUID)
    # 建立 輸出檔路徑資料夾
    if (not os.path.isdir(outFileDir)):
        os.mkdir(outFileDir)
    else:
        # 如果 輸出檔路徑資料夾內有東西,後面不處理了
        print(f'{outFileDir} is exist')
        print(f'error')
        return False

    # ========================================================================
    # 呼叫範例用的函數,這邊需勞煩實驗室自行實作之
    result = demo.exec(inputFileDir, outFileDir)
    # ========================================================================
    if (result):
        # 輸出結束資訊
        print(f'finish')
        return True
    else:
        print(f'error')
        return False



# 如果是主程式
if __name__ == '__main__':
    Main()
