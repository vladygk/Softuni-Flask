import factory

from db import db
from models import User, RoleType, Card


class BaseFactory(factory.Factory):
    @classmethod
    def create(cls, **kwargs):
        object_ = super().create(**kwargs)
        db.session.add(object_)
        db.session.commit()
        return object_


class UserFactory(BaseFactory):
    class Meta:
        model = User

    id = factory.Sequence(lambda n: n)
    username = factory.Faker("first_name")
    email = factory.Faker("email")
    password = factory.Faker("password")
    role = RoleType.user


def get_user_id():
    return UserFactory().id


class CardFactory(BaseFactory):
    class Meta:
        model = Card

    id = factory.Sequence(lambda n: n)
    title = "fake title"
    description = "fake descr"
    photo_url = "fake url"
    attribute = "fake attr"
    owner_id = 0
