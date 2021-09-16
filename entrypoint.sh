#!/bin/bash
set -e
Cyan='\e[36m'
Red='\e[31m'

/wait-for-postgres.sh

# activate our virtual environment here
. /opt/pysetup/.venv/bin/activate

printf $Red"*******************************\n"
printf $Cyan"*******************************\n"
printf $Red"Starting Production Enviroment\n"
printf $Cyan"*******************************\n"
printf $Red"*******************************\n"

if [ "$1" = "runserver" ]; then
	python manage.py migrate --no-input

	daphne -b 0.0.0.0 -p 8000 broma_config.asgi:application
else
	exec "$@"
fi

exit