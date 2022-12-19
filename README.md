# fastapi-postgres-sample

```
make up

export `cat postgres/local.env`

export POSTGRES_SERVER=localhost

alembic -x target=main revision --autogenerate

sqlacodegen postgresql://postgres:password@localhost/example > app/db/model.py

```


http://localhost/v1/docs


```
docker-compose exec api pytest ./app/tests
```