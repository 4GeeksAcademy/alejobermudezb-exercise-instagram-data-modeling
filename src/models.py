import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Text, Boolean
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)  
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    phone = Column(Integer)
    birthday = Column(String(10), nullable=False)
    posts = relationship("Post", backref="user")
    messages = relationship("Message")

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    date = Column(String(250))
    location = Column(String(250))
    like = Column(String(250), nullable=False)
    description = Column(String(250))
    user = relationship("User")
    pictures = relationship("Picture")
    comments = relationship("Comment")

class Message(Base):
    __tablename__ = 'message'
    id = Column(Integer, primary_key=True)
    text = Column(Text, nullable=False)
    reaction = Column(String(5))
    date = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
   
class Followers(Base):
    __tablename__ = 'followers'
    id = Column(Integer, primary_key=True)
    followers_id = Column(Integer,ForeignKey("user.id"))
    following_id = Column(Integer,ForeignKey("user.id"))
    user_1 = relationship("User")
    


class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    text = Column(Text, nullable=False)
    like = Column(Boolean)
    date = Column(String(250), nullable=False)
    post_id = Column(Integer, ForeignKey('post.id'))
    user_id = Column(Integer, ForeignKey('user.id'))


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
