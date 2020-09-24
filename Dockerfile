ARG AIDO_REGISTRY
FROM ${AIDO_REGISTRY}/duckietown/aido-base-python3:daffy

ARG PIP_INDEX_URL
ENV PIP_INDEX_URL=${PIP_INDEX_URL}
RUN echo PIP_INDEX_URL=${PIP_INDEX_URL}

WORKDIR /project

COPY requirements.* ./
RUN pip install -U pip>=20.2
RUN pip install --use-feature=2020-resolver -r requirements.resolved && rm -rf /root/.cache

COPY . .

ENTRYPOINT ["python3", "solution.py"]
