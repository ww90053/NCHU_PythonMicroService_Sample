FROM python:3

# 程式路徑,請維持
WORKDIR /usr/src/app

# 這邊需勞煩實驗室自行視情況調整之
# COPY requirements.txt ./
# RUN pip install --no-cache-dir -r requirements.txt

#將本資料夾完全複製
COPY . .
# 預設呼叫保持清醒的程式,請維持
CMD [ "python", "./keepawake.py" ]
# 預設執行一次單元測試程式碼
RUN python UnitTest.py