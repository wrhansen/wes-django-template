# For more information, please refer to https://aka.ms/vscode-docker-python
# Stage 1: builder image to install dependencies into virtualenvironment
FROM python:3.11-slim as builder

RUN pip install -U pip
ENV PATH /venv/bin:${PATH}

COPY requirements.txt ./app/requirements.txt

RUN python3 -m venv /venv
RUN . /venv/bin/activate; pip install --no-compile -r /app/requirements.txt

# Stage 2: Actual image
FROM python:3.11-slim

RUN mkdir /app
COPY . /app
COPY --from=builder /venv/ /venv/
COPY --from=builder /app/ /app/

EXPOSE 80

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH /app
ENV PATH /venv/bin:${PATH}
WORKDIR /app

# Creates a non-root user with an explicit UID and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser

# # During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
# CMD ["gunicorn", "config.wsgi", "--bind", "0.0.0.0:80"]
