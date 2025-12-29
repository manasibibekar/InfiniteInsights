from models.post import Post
from extensions import db

def create_post(title, content, user):
    post = Post(title=title, content=content, author=user)
    db.session.add(post)
    db.session.commit()
    return post


def get_all_posts():
    return Post.query.all()


def get_post(post_id):
    return Post.query.get_or_404(post_id)


def update_post(post, title, content):
    post.title = title
    post.content = content
    db.session.commit()
    return post


def delete_post(post):
    db.session.delete(post)
    db.session.commit()
