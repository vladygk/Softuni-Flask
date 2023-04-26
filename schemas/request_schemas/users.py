from marshmallow import fields, Schema


class UserRegisterRequestSchema(Schema):
    username = fields.String(required=True)
    email = fields.String(required=True)
    password = fields.String(required=True)


class UserLoginRequestSchema(Schema):
    email = fields.String(required=True)
    password = fields.String(required=True)
