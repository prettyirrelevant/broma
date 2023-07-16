# Broma
Basically a fun project where I implement certain technologies and learn too.

## Feature
- Video Call
- Real-Time Chat
- Real-Time Tic Tac Toe

## Development
- Clone the repository
- Create a virtual environment and install all dependencies.
- Populate the content of `.env.example` and rename to `.env`
- Run `python manage.py migrate` to update the database tables' schemas.
- Run `python manage.py runserver`
- Visit `http://localhost:8000`

## Drawbacks
- During a game, if the client disconnects, the state of the game is not restored upon reconnection.

## Roadmap
- [ ] Write testss.
- [ ] Implement cron job to delete conversations after 24 hours.
- [x] Implement chat feature.
- [ ] Store the state of a tictactoe game after every move.
