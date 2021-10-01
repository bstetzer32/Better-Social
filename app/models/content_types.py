from .db import db

class ContentType(db.Model):
    __tablename__ = 'content_types'

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(50), nullable=False)


    def to_dict(self):
        return {
            "id": self.id,
            "type": self.type
        }