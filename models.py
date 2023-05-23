"""
This is the models file for the Research Highlight section of the website.
"""
from database import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime


class ResearchHighlight(db.Model):
    """
    This is the Research Highlight class.

    Attributes:
        id (int): The id of the research highlight.
        image (str): The image of the research highlight.
        alt (str): The alt text of the image.
        link (str): The link of the research highlight.
        title (str): The title of the research highlight.
        description (str): The description of the research highlight.
    """
    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.String(256))
    alt = db.Column(db.String(256))
    link = db.Column(db.String(512))
    title = db.Column(db.String(256))
    description = db.Column(db.Text)

    # to dictionary for JSON serialization
    def to_dict(self):
        """
        This function converts the Research Highlight object to a dictionary.

        Returns:
            dict: The Research Highlight object in dictionary form.
        """
        return {
            'id': self.id,
            'image': self.image,
            'alt': self.alt,
            'link': self.link,
            'title': self.title,
            'description': self.description
        }
    
class BlogPost(db.Model):
    """
    This is the Blog Post class.
    It can have multiple posts.

    Attributes:
        id (int): The id of the blog post.
        title (str): The title of the blog post.
        date (date): The date of the blog post.
        posts (list): The list of posts in the blog post.
    """
    __tablename__ = 'blogpost'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256))
    date = db.Column(db.Date)
    posts = db.relationship('Post', backref='blogpost', lazy=True, cascade="all, delete-orphan")
    replies = db.relationship('Reply', backref='blogpost', lazy=True, cascade="all, delete-orphan")


class Post(db.Model):
    """
    This is the Post class.
    It can have multiple images.

    Attributes:
        id (int): The id of the post.
        content (str): The content of the post.
        blogpost_id (int): The id of the blog post that the post belongs to.
        images (list): The list of images in the post.
    """
    __tablename__ = 'post'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    blogpost_id = db.Column(db.Integer, db.ForeignKey('blogpost.id'), nullable=False)
    images = db.relationship('Image', backref='post', lazy=True, cascade="all, delete-orphan")


class Image(db.Model):
    """
    This is the Image class.

    Attributes:
        id (int): The id of the image.
        src (str): The source of the image.
        alt (str): The alt text of the image.
        post_id (int): The id of the post that the image belongs to.
    """
    __tablename__ = 'image'
    id = db.Column(db.Integer, primary_key=True)
    src = db.Column(db.String(256))
    alt = db.Column(db.String(256))
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)


class Admin(UserMixin, db.Model):
    __tablename__ = 'admin'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Reply(db.Model):
    """
    This is the Reply class.

    Attributes:
        id (int): The id of the reply.
        content (str): The content of the reply.
        date_posted (date): The date of the reply.
        blogpost_id (int): The id of the blog post that the reply belongs to.
    """
    __tablename__ = 'reply'
    id = db.Column(db.Integer, primary_key=True)
    guest = db.Column(db.String(64), nullable=True)
    content = db.Column(db.String(200), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    blogpost_id = db.Column(db.Integer, db.ForeignKey('blogpost.id'), nullable=False)


class Friend(db.Model):
    """
    This is the Friend class.
    It represents a research collaborator or blog neighbor.

    Attributes:
        id (int): The id of the friend.
        name (str): The name of the friend.
        profile_photo (str): The path to the profile photo of the friend.
        description (str): A short description of the friend.
    """
    __tablename__ = 'friend'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    profile_photo = db.Column(db.String(256), nullable=False)
    description = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"Friend(id={self.id}, name={self.name})"
