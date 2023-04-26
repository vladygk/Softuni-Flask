from marshmallow import fields, Schema, validates_schema, ValidationError
from marshmallow.validate import Length


class UserRegisterRequestSchema(Schema):
    username = fields.String(required=True, validate=Length(min=2, max=60))
    email = fields.Email(required=True)
    password = fields.String(required=True, validate=Length(min=6, max=60))

    @validates_schema
    def validates_username(self, data, **kwargs):
        if ' ' in data['username']:
            raise ValidationError('Username can\'t contain whitespace')

    @validates_schema
    def validates_password(self, data, **kwargs):
        if data['username'] == data['email']:
            raise ValidationError('Username and email can\'t be the same')


class UserLoginRequestSchema(Schema):
    email = fields.Email(required=True)
    password = fields.String(required=True, validate=Length(min=6, max=60))
