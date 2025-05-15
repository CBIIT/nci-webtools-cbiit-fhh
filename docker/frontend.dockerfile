FROM public.ecr.aws/amazonlinux/amazonlinux:2023

RUN dnf -y update \
    && dnf -y install \
    python3\
    python3-pip \
    npm \
    && dnf clean all

RUN mkdir -p /app/

WORKDIR /app/

COPY requirements.txt /app/

RUN pip3 install -r requirements.txt

COPY . /app/

CMD ["flask", "run", "--host=0.0.0.0", "--port=80"]