"""
This script seeds the initial data to the BlogPost table.
"""
from app import app, db
from models import BlogPost, Post, Image
from datetime import datetime

blogs_data = []

def seed_blog_1():
    # create a new blog post
    blog_post = BlogPost(title='2023-04-30 | 바나나 팬케이크란 무엇인가', date=datetime.strptime('2023-04-30', '%Y-%m-%d').date())

    # add some posts to the blog post
    post1_content = "오늘은 퇴사한지 3일차 되는 날이었다. 슬슬 잉여 시간이 많아지고 있었다. 이왕 이렇게 된 거 당분간 건강하게 살기로 했다. \
헬스장도 끊었는데 점심을 사 먹지 않고 만들어 먹기로 했다. 집에 바나나가 있어서 바나나 팬케이크를 만들어 먹기로 했다. \
슬슬 반점이 생기는 것이 얼른 먹어야 할 것 같았다. </br></br>\
바나나 팬케이크를 만들기 위해서는 바나나, 계란, 밀가루, 우유, 베이킹 파우더, 설탕, 소금이 필요하다.\
먼저 바나나를 으깬다. 그리고 계란을 풀어서 설탕과 소금을 넣고 섞는다. 그리고 우유를 넣고 섞는다.\
그리고 밀가루와 베이킹 파우더를 넣고 섞는다. 그리고 바나나를 넣고 섞는다. </br></br>\
팬을 달구고 기름을 두른다. 그리고 반죽을 넣고 뒤집어서 굽는다. 그리고 접시에 담아서 먹는다.\
바나나 팬케이크는 바나나를 넣어서 달콤하고 부드러운 맛이 나서 맛있다."
    post1 = Post(content=post1_content, blogpost=blog_post)
    image1 = Image(src='/static/pancake1.jpg', alt='My Photo', post=post1)
    image2 = Image(src='/static/pancake2.jpg', alt='My Photo', post=post1)
    image3 = Image(src='/static/pancake3.jpg', alt='My Photo', post=post1)
    post1.images.extend([image1, image2, image3])
    blog_post.posts.extend([post1])

    # add the blog post to the database
    db.session.add(blog_post)
    db.session.commit()

def seed_blog_2():
    # create a new blog post
    blog_post = BlogPost(title='2023-05-03 | 두산 vs 한화', date=datetime.strptime('2023-05-03', '%Y-%m-%d').date())
    post1_content = "오늘은 두산과 한화의 경기를 보러 갔다. 야구를 잘 모르지만 경기장에 가서 보는 게 재밌을 것 같았다. \
게다가 퇴사해서 시간도 많았다. 난 대전에 오래 살았어서 한화를 응원해야하지만, 전적으로 보고나서 두산을 응원하기로 했다. \
그런데 오늘은 한화가 8:3으로 이겼다. 다음부터 한화를 응원하기로 했다. 한화팬들은 잘 노는 것 같다. "
    post1 = Post(content=post1_content, blogpost=blog_post)
    image1 = Image(src='/static/minuk_baseball.jpg', alt='My Photo', post=post1)
    post1.images.extend([image1])
    blog_post.posts.extend([post1])

    # add the blog post to the database
    db.session.add(blog_post)
    db.session.commit()

def seed_blog_3():
    # create a new blog post
    blog_post = BlogPost(title='2023-05-08 | 모기를 관찰하기', date=datetime.strptime('2023-05-08', '%Y-%m-%d').date())
    post1_content = "오늘은 9시에 일어났다. 화장실에 갔는데 모기가 있어서 얼른 전기모기채로 잡아버렸다. \
모기는 죽었지만 형체가 보존되어 있어서 크게 보고 싶었다."
    post1 = Post(content=post1_content, blogpost=blog_post)
    image1 = Image(src='/static/moth1.jpg', alt='My Photo', post=post1)
    image2 = Image(src='/static/moth2.jpg', alt='My Photo', post=post1)
    image3 = Image(src='/static/moth3.jpg', alt='My Photo', post=post1)
    image4 = Image(src='/static/moth4.jpg', alt='My Photo', post=post1)
    post1.images.extend([image1, image2, image3, image4])

    post2_content = "모기의 흉측한 빨대를 크게 볼 수 있었다. 신기했다. 그 작은 빨대도 균일하게 생긴 것이 아니라 마디로 나누어져 있었다. \
마디로 나눠져 있으니 모기는 빨때를 구부릴 수 있지 않을까?\
또한 모기의 눈이 여러 격자로 이루어져 있는 것도 볼 수 있었다. \
모기의 날개와 빨대에는 잔털이 많았다. 왜 매끈하지 않고 잔털이 나 있을까?\
또한 모기의 머리는 몸통보다 훨씬 작았다. "
    post2 = Post(content=post2_content, blogpost=blog_post)

    post3_content = "길 가다가 주운 나뭇잎도 관찰해보았다. "
    post3 = Post(content=post3_content, blogpost=blog_post)
    image5 = Image(src='/static/leaf1.jpg', alt='My Photo', post=post3)
    image6 = Image(src='/static/leaf2.jpg', alt='My Photo', post=post3)
    image7 = Image(src='/static/leaf3.jpg', alt='My Photo', post=post3)
    image8 = Image(src='/static/leaf4.jpg', alt='My Photo', post=post3)
    image9 = Image(src='/static/leaf5.jpg', alt='My Photo', post=post3)
    post3.images.extend([image5, image6, image7, image8, image9])

    blog_post.posts.extend([post1, post2, post3])

    db.session.add(blog_post)
    db.session.commit()


if __name__ == '__main__':
    with app.app_context():
        seed_blog_1()
        seed_blog_2()
        seed_blog_3()
