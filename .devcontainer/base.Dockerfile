ARG IMG
FROM $IMG

# Install poetry
RUN curl -sSL https://install.python-poetry.org | python3 -
