# commands
execute following commands from django project base folder
```bash 
./init.sh # init project execution environment
docker-compose up -d # start database

python3 manage.py migrate
python3 manage.py createsuperuser --noinput
```