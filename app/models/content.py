from .db import db

class Content(db.Model):
    __tablename__ = 'contents'

    id = db.Column(db.Integer, primary_key=True)
    content_type = db.Column(db.Integer, db.ForeignKey("contents.id"), nullable=False)

    def to_dict(self):

        return {
            "id": self.id,
            "content_type": self.content_type
        }