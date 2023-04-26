from resources.auth import RegisterResource, LoginResource
from resources.boosters import BoostersResource, BoostersResourceFiltered
from resources.cards import CardsResource, CardResource
from resources.decks import DecksResource, DeckResource

routes = ((RegisterResource, "/register"),
          (LoginResource, "/login"),
          (CardResource, "/cards/<int:id_>"),
          (CardsResource, "/cards"),
          (DeckResource, "/decks/<int:id_>"),
          (DecksResource, "/decks"),
          (BoostersResourceFiltered, "/boosters/<string:deck_name>"),
          (BoostersResource, "/boosters")
          )
