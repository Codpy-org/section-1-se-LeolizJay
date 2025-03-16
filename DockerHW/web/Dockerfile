FROM python:3.11-slim
workdir /app
copy . .
RUN pip install -r requirements.txt
expose 5000
CMD ["python", "main.py"]