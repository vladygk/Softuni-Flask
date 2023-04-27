from marshmallow import fields, Schema, validates_schema, ValidationError
from marshmallow.validate import Length


class CardCreateRequestSchema(Schema):
    title = fields.String(required=True, validate=Length(min=1, max=60))
    description = fields.String(required=True, validate=Length(min=2, max=200))
    photo_base64 = fields.String(required=True)
    photo_extension = fields.String(required=True)
    attribute = fields.String(required=True, validate=Length(min=2, max=60))

    @validates_schema
    def validates_title(self, data, **kwargs):
        if not data['title'][0].isupper():
            raise ValidationError('Title must start with upper case')


class CardEditRequestSchema(Schema):
    title = fields.String(required=True, validate=Length(min=1, max=60))
    description = fields.String(required=True, validate=Length(min=2, max=200))
    attribute = fields.String(required=True, validate=Length(min=2, max=60))

    @validates_schema
    def validates_title(self, data, **kwargs):
        if not data['title'][0].isupper():
            raise ValidationError('Title must start with upper case')
