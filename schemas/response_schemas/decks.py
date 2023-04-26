from marshmallow import fields, Schema
from marshmallow.validate import Length


class DeckResponseSchema(Schema):
    title = fields.String(required=True, validate=Length(min=2, max=60))
    arch_type = fields.String(required=True, validate=Length(min=5, max=60))
