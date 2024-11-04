FROM python:3.9

WORKDIR /python_aprendizado_continuo

COPY requirements.txt /python_aprendizado_continuo

RUN pip install -r /python_aprendizado_continuo/requirements.txt

COPY . /python_aprendizado_continuo

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
