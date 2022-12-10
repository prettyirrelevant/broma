# Broma
Basically a fun project where I implement certain technologies and learn too.

## Feature
- Video Call
- Real-Time Chat
- Real-Time Tic Tac Toe

## Demo
A demo of the project can be found [here](https://bromaa.fly.dev).

## Development (Docker)
- For easy replication of this project on your local machine, use the Docker configuration.
- Populate the content of `.env.example` and rename to `.env`
- Run `docker-compose up -d --build`
- Visit `http://localhost:8000`

## Drawbacks
- During a game, if the client disconnects, the state of the game is not restored upon reconnection.

## Roadmap
- [ ] Write testss.
- [ ] Implement cron job to delete conversations after 24 hours.
- [x] Implement chat feature.
- [ ] Store the state of a tictactoe game after every move.
