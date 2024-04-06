# wes-django-template

This is my cookiecutter template for stamping out a new django project that
uses the following:

## Tools

* docker & docker compose
* just


## Web application

The web application uses the following technologies:

* django 4.2
* htmx
* bootstrap 5


# Install this template

To create a project using this template do the following:

Install cookiecutter using pipx

```sh
pipx install cookiecutter
```

Run cookiecutter on the template

```sh
pipx run cookiecutter gh:wrhansen/wes-django-template.git
```

Answer the prompts, and then a new project will be created based on your inputs.

# Cookiecutter project template

* project_name -- the name of the project. This name will be cleaned and used
    for they underlying python project that gets created.
* description -- a short description for this project, goes into the generate
    README
