FROM python:3.9

ADD PasswordGenerator.py .

CMD ["python", "./PasswordGenerator.py"]