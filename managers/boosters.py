from models import Booster, Deck


class BoosterManager:
    # returns all boosters in db
    @staticmethod
    def get_all():
        return Booster.query.filter_by().all()

    # returns booster for specific deck title
    @staticmethod
    def get_filtered(deck_name):
        deck_id = Deck.query.filter_by(title=deck_name).first().id

        boosters = Booster.query.filter_by(id=deck_id).all()

        return boosters
