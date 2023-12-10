ARG IMG
FROM $IMG

# Install CL locale
RUN sed -i "s/# es_CL.UTF-8 UTF-8/es_CL.UTF-8 UTF-8/g" /etc/locale.gen && \
    locale-gen

# Setup OMZ configuration
RUN omz update && \
    sed -i 's/^ZSH_THEME=.*/ZSH_THEME=\"bira\"/' /root/.zshrc

# Install poetry
RUN curl -sSL https://install.python-poetry.org | python3 -
