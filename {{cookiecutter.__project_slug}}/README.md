# {{cookiecutter.__project_slug}}

{{cookiecutter.description}}

## Technology choices

* django 4.2
* htmx
* bootstrap 5
* postgres db

## Tools

* docker & docker compose
* justfile


## just commands

The following commands are provided to assist with development. With `just`
installed, simply run these commands from the project root command line:

* `just rebuild`-- rebuild the docker image
* `just shell` -- gain a bash shell into the web container
* `just cleandb` -- flush the postgres database to start fresh
* `just test` -- run unit tests
* `just init` -- setup initial project space


## Run the server (local development)

This project comes with a dockerfile and docker compose setup for local development.
Use the following docker compose commands:

* first time use: `just init` -- to setup the project space before running any
    docker commands
* `docker compose up` -- start up the docker containers, including the web server
    and database.
* visit `http://localhost:8000` in a web browser
