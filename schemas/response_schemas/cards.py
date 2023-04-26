from marshmallow import fields, Schema
from marshmallow.validate import Length


class CardResponseSchema(Schema):
    title = fields.String(required=True, validate=Length(min=2, max=60))
    description = fields.String(required=True, validate=Length(min=2, max=60))
    photo_url = fields.String(required=True, validate=Length(min=2, max=60))
    attribute = fields.String(required=True, validate=Length(min=2, max=60))
