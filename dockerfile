# 使用官方 Python 基礎映像
FROM python:3.9-slim

WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "main.py"]