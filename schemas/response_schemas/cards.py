from marshmallow import fields, Schema


class CardResponseSchema(Schema):
    title = fields.String(required=True)
    description = fields.String(required=True)
    photo_url = fields.String(required=True)
    attribute = fields.String(required=True)




