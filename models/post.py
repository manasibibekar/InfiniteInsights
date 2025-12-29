from extensions import db

class Post(db.Model):
    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)

    author_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    )

    author = db.relationship(
        "User",
        back_populates="posts"
    )

    def __repr__(self):
        return f"<Post id={self.id} title={self.title}>"
