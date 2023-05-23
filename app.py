"""
The application constructs Minuk's personal website using Flask.
The website is hosted on EC2 and can be accessed through www.minukma.com
It contains Minuk's resume, blogs, and projects.
"""
import os
import re
import json
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, abort, flash
# use sqlalchemy to connect to database
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user
from database import db, migrate
from models import BlogPost, Admin, Post, Image, Reply, Friend
from werkzeug.security import check_password_hash
from werkzeug.utils import secure_filename

# Import the ResearchHighlight model
from models import ResearchHighlight

def convert_links(description):
    # converts the links in the research highlights to html links.
    pattern = r'\[\[(.*?)\]\]\((.*?)\)'
    replacement = r'<a href="\2">\1</a>'
    return re.sub(pattern, replacement, description)

# create the application object
app = Flask(__name__)
app.secret_key = app.secret_key = os.environ.get('FLASK_SECRET_KEY', 'default-secret-key')

# configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///minuk_database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
migrate.init_app(app, db)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

app.config['MAX_CONTENT_LENGTH'] = 100 * 1024 * 1024  # limit request size
app.jinja_env.filters['convert_links'] = convert_links

def research_highlights_to_json(research_highlights):
    # convert the research highlights to a list of dictionaries
    return json.dumps([highlight.to_dict() for highlight in research_highlights])

@app.route('/')
def home():
    research_highlights = ResearchHighlight.query.all()
    return render_template(
        'index.html', 
        research_highlights_json=research_highlights_to_json(research_highlights)
    )

@app.route('/blogs')
def blogs():
    # to construct the blog_nav bar
    blog_posts = BlogPost.query.order_by(BlogPost.date.desc()).all()

    # Fetch the BlogPost with the given id
    latest_blog = BlogPost.query.order_by(BlogPost.date.desc()).first()

    return render_template(
        f'blog_post.html', 
        blog=latest_blog,
        blog_posts=blog_posts
    )

@app.route('/resume')
def resume():
    return render_template('resume.html')

@app.route('/blogs/<int:blog_id>')
def post(blog_id):
    # Fetch the BlogPost with the given id
    blog_post = BlogPost.query.get(blog_id)

    if not blog_post:
        # Return a 404 error if the blog post does not exist
        abort(404)

    # to construct the blog_nav bar
    blog_posts = BlogPost.query.order_by(BlogPost.date.desc()).all()
    return render_template(
        'blog_post.html', 
        blog=blog_post,
        blog_posts=blog_posts
    )


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        password = request.form.get('password')
        admin = Admin.query.get(1)  # Assuming you only have one admin
        if admin and admin.check_password(password):
            login_user(admin)
            action = request.form.get('action')
            post_id = request.form.get('post_id')
            if action == 'new_post':
                return redirect(url_for('new_post'))
            elif action == 'revise_post':
                return redirect(url_for('revise_post', post_id=post_id))
            elif action == 'delete_post':
                return redirect(url_for('delete_post', post_id=post_id))
    flash('Are you really Minuk? You previously submitted an incorrect password!')
    return redirect(url_for('blogs'))


@login_manager.user_loader
def load_user(user_id):
    return Admin.query.get(int(user_id))


@app.route('/new_post')
@login_required
def new_post():
    return render_template('new_post.html')


@app.route('/create_post', methods=['POST'])
@login_required
def create_post():
    # Get the title from the form data
    title = request.form.get('title')

    # Create a new BlogPost instance
    blog_post = BlogPost(title=title, date=datetime.now())
    db.session.add(blog_post)
    db.session.commit()  # Commit the session to get an id for blog_post

    # Get the content and image from the form data
    contents = request.form.getlist('content[]')
    images = request.files.getlist('image[]')

    for content, image in zip(contents, images):
        # Create a new Post instance
        post = Post(content=content, blogpost_id=blog_post.id)
        db.session.add(post)
        db.session.commit()  # Commit the session to get an id for post

        # Check if the image was provided
        if image:
            filename = secure_filename(image.filename)
            image_path = os.path.join('static/images', filename).replace("\\", "/")  # fix windows error
            image.save(image_path)

            image_path_db = "/" + image_path
            # Create a new Image instance
            img = Image(src=image_path_db, alt=content, post_id=post.id)
            db.session.add(img)

    db.session.commit()

    # Redirect to the newly created post
    return redirect(url_for('post', blog_id=blog_post.id))


@app.route('/delete_post/<int:post_id>', methods=['GET'])
@login_required
def delete_post(post_id):
    post_to_delete = BlogPost.query.get_or_404(post_id)
    db.session.delete(post_to_delete)
    db.session.commit()
    flash('The post was successfully deleted!')
    return redirect(url_for('blogs'))


@app.route('/revise_post/<int:post_id>')
@login_required
def revise_post(post_id):
    blog_post = BlogPost.query.get_or_404(post_id)
    return render_template('edit_post.html', blog_post=blog_post)


@app.route('/update_post/<int:post_id>', methods=['POST'])
@login_required
def update_post(post_id):
    # Get the existing blog post
    blog_post = BlogPost.query.get_or_404(post_id)
    
    # Now, update the blog_post with the new data from the form submission
    blog_post.title = request.form.get('title')
    blog_post.date = datetime.now()

    # Get the content and image from the form data
    contents = request.form.getlist('content[]')
    images = request.files.getlist('image[]')

    # Here's where things get tricky: we need to match the new content and images with the existing posts and images.
    # This code assumes that the ordering of the content and images matches the ordering of the existing posts.
    for i, post in enumerate(blog_post.posts):
        # Update the content of the post
        post.content = contents[i]
        
        # Check if a new image was provided
        if images[i]:
            filename = secure_filename(images[i].filename)
            image_path = os.path.join('static/images', filename).replace("\\", "/")  # fix windows error
            images[i].save(image_path)

            image_path_db = "/" + image_path
            # Assume that each post has exactly one image
            post.images[0].src = image_path_db
            post.images[0].alt = contents[i]

    db.session.commit()

    flash('The post was successfully updated!')
    return redirect(url_for('post', blog_id=blog_post.id))


@app.route('/add_reply/<int:blog_id>', methods=['POST'])
def add_reply(blog_id):
    # Get the blog post
    blog_post = BlogPost.query.get_or_404(blog_id)
    
    # Create a new Reply
    reply = Reply(guest=request.form.get('guest'), content=request.form.get('reply'), blogpost_id=blog_id)

    # Add the reply to the session and commit
    db.session.add(reply)
    db.session.commit()

    # Redirect back to the blog post
    return redirect(url_for('post', blog_id=blog_id))


@app.route('/connections')
def connections():
    friends = Friend.query.all()

    friends = Friend.query.order_by(Friend.name).all()
    return render_template('connections.html', friends=friends)


@app.route('/add_friend', methods=['POST'])
def add_friend():
    # Get the data from the POST request
    name = request.form.get('name')
    photo = request.files.get('photo')
    description = request.form.get('description')

    # Check if the photo was provided
    if photo:
        filename = secure_filename(photo.filename)
        photo_path = os.path.join('static/images', filename)
        photo.save(photo_path)
    else:
        photo_path = None

    # Create a new Friend instance
    friend = Friend(name=name, profile_photo=photo_path, description=description)

    # Add the friend to the session
    db.session.add(friend)
    db.session.commit()

    flash('New friend added successfully!', 'success')

    # Redirect to the connections page or any other appropriate page
    return redirect(url_for('connections'))


if __name__ == '__main__':
    app.run(debug=True)
