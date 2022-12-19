#! /usr/bin/env sh

# printenv

# Let the DB start
sleep 3;
python /app/db/backend_wait.py

# Run migrations
cd /
alembic -x target=main upgrade head

# alembic -x target=test downgrade head
alembic -x target=test upgrade head
