FROM duckietown/aido3-base-python3:daffy

WORKDIR /project

COPY requirements.txt .

RUN pip install -r requirements.txt && rm -rf /root/.cache

COPY . .

ENTRYPOINT ["python3", "solution.py"]
