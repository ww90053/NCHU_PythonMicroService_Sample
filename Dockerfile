FROM python:3

# 請維持以下路徑
WORKDIR /usr/src/app

# COPY requirements.txt ./
# RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./keepawake.py" ]
