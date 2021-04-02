ARG AIDO_REGISTRY=docker.io
ARG ARCH=amd64
ARG MAJOR=daffy
ARG BASE_TAG=${MAJOR}-${ARCH}
FROM ${AIDO_REGISTRY}/duckietown/dt-commons:${BASE_TAG}

ARG PIP_INDEX_URL
ENV PIP_INDEX_URL=${PIP_INDEX_URL}
RUN echo PIP_INDEX_URL=${PIP_INDEX_URL}

WORKDIR /code


RUN pip3 install -U "pip>=20.2"
COPY requirements.* ./
RUN cat requirements.* > .requirements.txt
RUN  pip3 install --use-feature=2020-resolver -r .requirements.txt


COPY . .

RUN PYTHONPATH=. python3 -c "from solution import *"

CMD ["python3", "solution.py"]
