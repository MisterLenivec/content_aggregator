# Content Aggregator Backend

### For asynchronous periodic content updates:

#### Run redis on docker:
```
docker run -d -p 6379:6379 redis
```

#### Run django server:
```
python manage.py runserver
```

#### Run the Celery worker server:
```
celery -A backend worker -l info
```

#### Run the periodic task scheduler:
```
celery -A backend beat -l info
```

#### Run Flower:
```
flower -A backend --port=5555
```

#### View Flower http://127.0.0.1:5555/

#### Or create docker build

#### Don't forget about settings

