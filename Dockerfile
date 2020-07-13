ARG AIDO_REGISTRY
FROM ${AIDO_REGISTRY}/duckietown/aido-base-python3:daffy-aido4

WORKDIR /project

COPY requirements.* ./

RUN pip install -r requirements.resolved && rm -rf /root/.cache

COPY . .

ENTRYPOINT ["python3", "solution.py"]
