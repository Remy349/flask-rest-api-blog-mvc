from marshmallow import Schema, fields


class PlainCommentSchema(Schema):
    id = fields.Int(dump_only=True)
    content = fields.Str(required=True)
    create_at = fields.DateTime(dump_only=True)


class PlainPostSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    content = fields.Str(required=True)
    create_at = fields.DateTime(dump_only=True)


class CommentSchema(PlainCommentSchema):
    post_id = fields.Int(required=True, load_only=True)
    post = fields.Nested(PlainPostSchema(), dump_only=True)


class PostSchema(PlainPostSchema):
    comments = fields.List(fields.Nested(PlainCommentSchema()), dump_only=True)


class PostUpdateSchema(Schema):
    title = fields.Str()
    content = fields.Str()
