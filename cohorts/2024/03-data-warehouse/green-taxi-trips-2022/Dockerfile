FROM mageai/mageai:latest

ARG USER_CODE_PATH=/home/src/${PROJECT_NAME}

# Note: this overwrites the requirements.txt file in your new project on first run.
# You can delete this line for the second run :)
# COPY requirements.txt ${USER_CODE_PATH}/requirements.txt

# RUN pip3 install -r ${USER_CODE_PATH}/requirements.txt

RUN pip3 install poetry

COPY pyproject.toml ${USER_CODE_PATH}/pyproject.toml
COPY poetry.lock ${USER_CODE_PATH}/poetry.lock

RUN poetry install
