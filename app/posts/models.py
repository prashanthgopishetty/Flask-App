

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(50), unique=True, nullable=False)
    content = db.Column(db.String(500), unique=True, nullable=False)

    def __repr__(self):
        return f" Post ==> {self.subject}"
