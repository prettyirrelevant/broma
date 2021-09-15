# Broma
Basically a fun project where I implement certain technologies and learn too.

## Development (Docker)
- For easy replication of this project on your local machine, use the Docker configuration.
- Populate the content of `.env.example` and rename to `.env`
- Run `docker-compose up -d --build`

## Drawbacks
- During a game, if the client disconnects, the state of the game is not restored upon reconnection.

## Roadmap
- [ ] Write testss.
- [ ] Implement chat feature.
- [ ] Store the state of a tictactoe game after every move.