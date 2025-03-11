FROM python:3.12.5

#Creates a directory named /app inside the container for the application code.
RUN mkdir /app
#Sets the working directory to /app. All subsequent commands will execute relative to this directory.
WORKDIR /app

# Creates a subdirectory named src inside /app to store the source code.
RUN mkdir src 
COPY src src

RUN pip install poetry
RUN poetry config virtualenvs.create false

#Copies the Poetry dependency configuration
COPY poetry.lock pyproject.toml /app/  
#Installs all the Python dependencies listed in the pyproject.toml file without creating a virtual environment 
RUN poetry install -n --no-root

ENV PYTHONPATH="/app/src"
WORKDIR /app/src

EXPOSE 8050
EXPOSE 8080
# ENTRYPOINT ["python3", "./api/main.py"]
