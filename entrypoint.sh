#!/bin/bash
set -e
Cyan='\e[36m'
Red='\e[31m'

/wait-for-postgres.sh

# activate our virtual environment here
. /opt/pysetup/.venv/bin/activate

printf $Red"*******************************\n"
printf $Red"*******************************\n"
printf $Red"Starting Production Enviroment\n"
printf $Red"*******************************\n"
printf $Red"*******************************\n"

if [ "$1" = "runserver" ]; then
	# This is just to make `docker-compose up` work first time
	# Real production should run these manually
	python manage.py migrate --no-input

	daphne -b 0.0.0.0 -p 8000 broma_config.asgi:application
elif [ "$1" = 'manage' ]; then
	python manage.py "${@:2}"
else
	exec "$@"
fi

exit