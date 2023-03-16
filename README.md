
This project is a template to quickly setup prototypes of python apps / jobs interacting with PostgreSQL Dbs

it uses : 

- *alembic* to manage migrations
- *sqlalchemy* as orm


## set up database


    make setup




## run migrations


    poetry run alembic upgrade head

