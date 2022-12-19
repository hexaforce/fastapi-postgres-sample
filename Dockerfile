FROM python:slim as requirements-stage
COPY ./pyproject.toml /tmp/
WORKDIR /tmp
RUN pip install poetry
RUN poetry export -f requirements.txt --output requirements.txt --without-hashes

FROM hexaforce/fastapi-docker
COPY --from=requirements-stage /tmp/requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt
COPY ./app /app
COPY ./alembic.ini /

# In production, comment out the following:
CMD ["/start-reload.sh"]
# Default /start.sh is applied.
