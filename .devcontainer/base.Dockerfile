ARG IMG
FROM $IMG

# Install CL locale
RUN sed -i "s/# es_CL.UTF-8 UTF-8/es_CL.UTF-8 UTF-8/g" /etc/locale.gen && \
    locale-gen

# Install poetry
RUN curl -sSL https://install.python-poetry.org | python3 -
