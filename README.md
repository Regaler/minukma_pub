# [Minuk's Personal Website](https://www.minukma.com/)

This is a Flask-powered personal website hosted on an Amazon EC2 instance. It uses SQLite3 as a database to store data, including blog posts and replies from users. It was primarily designed to serve as a platform to showcase my research work and connect with my peers and the general audience.

## Technologies Used

- Flask
- SQLite3
- HTML/CSS
- Vue.js
- AWS EC2
- Nginx
- Certbot (for HTTPS encryption)

## Features

- **Home (MINUK MA):** The landing page of the website, displaying profile information, email, and research highlights. The highlights are converted from a markdown-like syntax into HTML.
- **Resume:** A dedicated section to download my resume in PDF format.
- **Blogs:** A unique feature that allows admin to add, revise, and delete blog posts. Each blog post can contain text and images. Users can also leave replies on the blog posts.
- **Connections:** A section dedicated to introducing my work colleagues or collaborators as a researcher and blog neighbors who may be interesting to keep in touch with.

## Admin Login

The website features secure login functionality for the administrator. This allows the administrator to create new blog posts, revise existing ones, and delete any post if required.

## Repository Structure

- `migrations`: Contains files related to database migrations.
- `static`: Contains static files like CSS, JavaScript, and images.
- `templates`: Contains the HTML templates for the website.
- `.gitignore`: Specifies files that should not be tracked by Git.
- `app.py`: The main Flask application file.
- `database.py`: Contains database configurations.
- `models.py`: Defines the database models for SQLAlchemy.
- `requirements.txt`: Lists all the Python dependencies for the project.
- `seed_admin.py`, `seed_blogs.py`, `seed_research_highlights.py`: Python scripts to seed the initial data into the database.
- `tmp_db_query.py`: A temporary file possibly used for running ad-hoc queries on the database.

## Deployment

The website is hosted on an Amazon EC2 instance with Nginx serving the application. If you want to deploy a similar setup, please follow these general steps:

1. Set up an EC2 instance in your AWS account. You can follow [this guide](https://docs.aws.amazon.com/efs/latest/ug/gs-step-one-create-ec2-resources.html) for the same.

2. Once you have SSH access to your EC2 instance, clone this repository to your EC2 instance.

3. Install the necessary dependencies using `pip install -r requirements.txt`.

4. Set up Nginx by following [this guide](https://www.digitalocean.com/community/tutorials/how-to-install-nginx-on-ubuntu-20-04). Configure Nginx to serve your application.

5. Apply the migrations to your SQLite3 database using Flask-Migrate.

6. Secure your application by setting up HTTPS using Certbot. Follow [this guide](https://www.digitalocean.com/community/tutorials/how-to-secure-nginx-with-let-s-encrypt-on-ubuntu-20-04) for more details.

## Disclaimer

The website is currently set up for personal use and as such, does not support user registration or multiple admins. If you would like to adapt the codebase for a different use case, significant modifications may be required.

## License

All Rights Reserved to Minuk Ma. 

## Acknowledgments

I would like to express my gratitude to my colleagues and collaborators for their continuous support and inspiration.

For any further queries, please feel free to reach out to me.

