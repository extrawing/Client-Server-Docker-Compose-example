# Same thing than the 'server' Dockerfile.
FROM python:latest

RUN apt-get update && apt-get install -y \
    tcpdump \
    net-tools

# Same thing than the 'server' Dockerfile.
# We import 'client.py' in '/client/' folder.
ADD client.py /client/

# I would like to introduce something new, the 'WORKDIR' command.
# This command changes the base directory of your image.
# Here we define '/client/' as base directory.
WORKDIR /client/
