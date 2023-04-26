from resources.auth import RegisterResource, LoginResource
from resources.cards import CardsResource, CardResource

routes = ((RegisterResource, "/register"),
          (LoginResource, "/login"),
          (CardResource, "/cards/<int:id_>"),
          (CardsResource, "/cards"),
          )
