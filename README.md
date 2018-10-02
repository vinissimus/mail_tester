# Mail Tester

## Description:
Server based on aiohttp deployed on a docker container.
It serves to send an email rendered in html.

## Requirements
  1. Python 3.6
  2. Latest pip version
  3. Latest docker version

## Deployment
### Build the docker image
  - "$ docker build -t <tagname> ."

### Run the container
  - "$ ./run {user} {password}"

## How to use it
  1. Go to localhost:8080
  2. Type the recipient's email, subject and content
  3. Send!
