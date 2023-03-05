FROM python:3.10
WORKDIR /prediction
COPY requirements.txt /prediction
EXPOSE 5000
RUN pip install virtualenv
ENV PATH="/flaskenv/bin:$PATH"
RUN pip install -r ./requirements.txt
COPY . /prediction
CMD ["python", "app.py"]