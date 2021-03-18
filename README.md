# Lab: Django REST Framework & Docker
## Overview
Use Django REST Framework to create an API, then “containerize” it with Docker.

The process of querying and converting tabular database values into JSON or another format is called _serialization_. When you're creating an API, the correct serialization of data is the major challenge. The Django REST Framework will solve this in my application by providing:
1. A web-browsable API
2. Authentication polcies include packages for OAuth1 and OAuth2
3. Serialization supports both ORM and non-ORM data sources
4. [Extensive documentation](https://www.django-rest-framework.org/)

## Feature Tasks and Requirements
- [x] Rebuild a custom version of Blog API demo project from scratch.
  - [x] Replace Blog and Post with your own application and model.
  - [x] Your model must have at least as many fields as demo’s model.
  - [x] Your model must have one field that is a foreign key to user.
  - [x] NOTE: You are not required to build any templates for this lab.
## Features - Docker
  - [x] NOTE Refer to the class demo for built out Dockerfile and docker-compose.yml examples.
  - [x] Update Dockerfile and docker-compose.yml if needed.

## Implementation Notes
- [x] You’ll need to run a command to convert pyproject.toml dependencies to requirements.txt
poetry export -f requirements.txt -o requirements.txt

If you get an allowed host error examine the bug details and update code as needed.
When Docker installed and docker files are ready to go then run…
`$ docker-compose up`
- To shut docker down enter ctrl+c, then run:
`$ docker-compose down`
You’ll learn a better way soon
### User Acceptance Tests
- [x] Modify provided unit tests in demo to work for your project.
  -  `$ python manage.py test` passes