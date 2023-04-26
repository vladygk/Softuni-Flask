#Yugioh API#
## SoftUni Flask project ## 
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/3c/Flask_logo.svg/1280px-Flask_logo.svg.png" width= "100px"/>

##Main Functionality##
- CRUD operations for the Card resource
- Private and Public part of the API
- Persisting data in a DB

## Endpoints provided ##

###Authentication###
- POST  `/register` public
- POST `/login` public

###Cards###
- GET `/cards` private
- GET `/cards/id` private
- PUT `/cards/id` private
- DELETE `/cards/id` private

###Decks###
- GET `/decks` public
- GET `/decks/id` public

###Boosters###
- GET `/boosters` public
- GET `/boosters/deck_name` public

##Future functionality##
- Add mobile app UI
