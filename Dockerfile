# syntax=docker/dockerfile:1
FROM python:3.10-bullseye
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

ARG USERNAME=guido
ARG USER_ID=1000
ARG GROUP_ID=1000
RUN groupadd --gid ${GROUP_ID} ${USERNAME}
RUN useradd --uid ${USER_ID} --gid ${GROUP_ID} -s /bin/bash -m ${USERNAME}
USER ${USERNAME}
ENV PATH=$PATH:$HOME/.local/bin

WORKDIR /workspaces/budget/
COPY core /workspaces/budget/core/
COPY main /workspaces/budget/main/
COPY manage.py requirements.txt /workspaces/budget/
RUN python -m pip install --upgrade pip && python -m pip install -r requirements.txt
