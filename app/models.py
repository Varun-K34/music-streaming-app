from datetime import datetime
from app import db

class User(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    is_creator = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"
    
class Song(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    lyrics = db.Column(db.Text, nullable =False)
    duration = db.Column(db.String(10), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    album_id = db.Column(db.Integer, db.ForeignKey('album.id'), nullable=False)

    def __repr__(self):
        return f"Song('{self.name}', '{self.album}')"
    
class Album(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    genre = db.Column(db.String(100), nullable=False)
    artist = db.Column(db.String(100), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    songs = db.relationship('Song', backref='album', lazy=True)

    def __repr__(self):
        return f"Album('{self.name}', '{self.artist}')"
    
class Playlist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    songs = db.relationship('Song', secondary='playlist_songs', backref='playlists', lazy='dynamic')

    def __repr__(self):
        return f"Playlist('{self.name}', '{self.user_id}')"
    

