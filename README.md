![](https://reposart.s3.eu-west-2.amazonaws.com/minusz/monolith.jpg)
*Art from ["Witcher Concept Art of Blaviken, Cintra and Tor Lara"](https://redanianintelligence.com/2019/12/31/new-witcher-concept-art-of-blaviken-cintra-and-tor-lara/)*

# The Monolith
TBD..

## Development:

### Setup db:
1. Go into cointainer `docker-compose run monolith /bin/bash`
2. `export PYTHONPATH=.`
3. Migrate users app first `./manage.py makemigrations users` & `./manage.py migrate users`
4. Run rest of the migrations `./manage.py migrate`

### Build
`docker-compose build`

### Run
`docker-compose up`

### or just
`docker-compose up --build`

Go to [http://localhost:8000/](http://localhost:8000/)
