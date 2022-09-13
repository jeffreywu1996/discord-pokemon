# discord-pokemon

## Get started
Need dicsord bot token `.env` and firebase creds file `config/pokedb-cred.prod.json`.

### Run locally
```bash
python3 -m venv venv
source venv/bin/activate

pip3 install -r requirements.txt
python3 poke_bot.py
```

### Build docker
```bash
make build
```
### Run docker
```bash
make run
```

## Deploy
```angular2html
heroku container:push pokemon
heroku container:release pokemon
```