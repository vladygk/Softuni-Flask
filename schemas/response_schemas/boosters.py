from marshmallow import fields, Schema
from marshmallow.validate import Length


class BoosterResponseSchema(Schema):
    title = fields.String(required=True, validate=Length(min=2, max=60))
