FROM python:3.7
WORKDIR /app
COPY . /main.py
RUN pip install -r req.txt
CMD ["python", "main.py"]