# This Dockerfile is from https://github.com/thedirtyfew/dash-docker-mwe
FROM python:3.8-slim-buster

RUN echo '<h1>Hello, Docker!</h1>'
# Create a working directory.
RUN mkdir wd
WORKDIR wd

# Install Python dependencies.
COPY requirements.txt .
RUN pip3 install -r requirements.txt

# Copy the rest of the codebase into the image
COPY . ./

# Finally, run gunicorn.
CMD [ "gunicorn", "--workers=5", "--threads=1", "-b 0.0.0.0:8000", "src.local_run.app:server"]