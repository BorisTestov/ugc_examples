FROM python:3.11

COPY requirements.txt .
RUN pip install -r requirements.txt
COPY main.py .
ENTRYPOINT ["python3"]
CMD ["main.py"]