# pull official base image
FROM python:3.9.6-slim-buster

# set working directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# trunk-ignore(hadolint/DL3008)
# trunk-ignore(hadolint/DL3009)
# trunk-ignore(hadolint/DL3015)
# trunk-ignore(hadolint/DL3013)
# install system dependencies
RUN apt-get update \
  && apt-get -y install netcat gcc \
  && apt-get clean

# install python dependencies
RUN pip install --no-cache-dir --upgrade pip
COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# add app
COPY . .

# add entrypoint
COPY ./entrypoint.sh .
RUN chmod +x /usr/src/app/entrypoint.sh

# run entrypoint
ENTRYPOINT [ "/usr/src/app/entrypoint.sh" ]