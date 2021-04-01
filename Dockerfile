ARG AIDO_REGISTRY=docker.io
ARG ARCH=amd64
ARG MAJOR=daffy
ARG BASE_TAG=${MAJOR}-${ARCH}
FROM ${AIDO_REGISTRY}/duckietown/aido-base-python3:daffy-amd64

ARG PIP_INDEX_URL
ENV PIP_INDEX_URL=${PIP_INDEX_URL}
RUN echo PIP_INDEX_URL=${PIP_INDEX_URL}

WORKDIR /project


RUN pip3 install -U "pip>=20.2"
COPY requirements.* ./
RUN cat requirements.* > .requirements.txt
RUN  pip3 install --use-feature=2020-resolver -r .requirements.txt


COPY . .

RUN PYTHONPATH=. python3 -c "from solution import *"

ENTRYPOINT ["python3", "solution.py"]
