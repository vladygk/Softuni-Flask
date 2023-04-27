# Yugioh API #
## SoftUni Flask project ## 
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/3c/Flask_logo.svg/1280px-Flask_logo.svg.png" width= "100px"/>


## How to install ##
1. `pip install -r requirements.txt`
2. `flask run`

## Main Functionality ##
- CRUD operations for the Card resource
- Private and Public part of the API
- Persisting data in a DB
- Saving card photos in *Firebase* storage

## Endpoints provided ##

### Authentication ###
- POST  `/register` **public**: Register user and return token 
- POST `/login` **public**: Login user and return token

### Cards ###
- POST `/cards` **private**: Create new card
- GET `/cards` **private**: Get all cards (depends on the role)
- GET `/cards/id` **private**: Get one card (depends on the role)
- PUT `/cards/id` **private**: Edit one card (depends on the role)
- DELETE `/cards/id` **private**: Delete one card (depends on the role)

### Decks ###
- GET `/decks` **public**: Get all decks
- GET `/decks/id` **public**: Get one deck

### Boosters ###
- GET `/boosters` **public**: Get all boosters
- GET `/boosters/deck_name` **public**: Get one booster

## Future functionality ##
- Add mobile app UI
