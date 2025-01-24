# ARG PYTHON_VERSION=3.12.1
FROM ubuntu:24.04

ENV TZ=America/Chicago
ENV FLET_FORCE_WEB_SERVER=true
ENV VIRTUAL_ENV=/opt/venv

#RUN apt-get update && apt-get install -y python3 curl libmpv-dev mpv libgtk-3-dev libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev

RUN apt-get update && apt-get install -y python3 python3-pip python3-venv

# Create a virtual environment
RUN python3 -m venv /opt/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

WORKDIR /app

# Copy the frontend source code into the container
COPY . .

# Activate the virtual environment and install dependencies
RUN pip install -r requirements.txt

# Expose the port that the frontend application listens on
EXPOSE 5554

# Start the frontend application TODO may want to change hot reload to not be on when running in prod
CMD ["/bin/bash", "-c", "source $VIRTUAL_ENV/bin/activate && flet run -w -p 5554 main.py"]