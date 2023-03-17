
This project is a template to quickly setup prototypes of python apps / jobs interacting with PostgreSQL Dbs

it uses : 

- *alembic* to manage migrations
- *sqlalchemy* as orm



NB. When starting a new project, if no migrations exists, ensure that the folder alembic/versions exists.
If not, alembic revision will fail (and the error message is not very clear about the folder missing)



## set up database

    make setup

## autogenerate migrations from models

    poetry run alembic revision --autogenerate

## check migration generation (dry-run) and potential issues

    poetry run alembic check

## run migrations to db

    poetry run alembic upgrade head

## downgrade db migrations fully

    poetry run alembic downgrade base


