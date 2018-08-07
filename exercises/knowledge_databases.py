from knowledge_model import Base, Knowledge

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///knowledge.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_subject(subject,topic,rating):

    knowledge_object=Knowledge(
        # knowledge_id=knowledge_id,
        subject=subject,
        topic=topic,
        rating=rating)
    session.add(knowledge_object)
    session.commit()
# add_subject("potatoes","potatoes" , 10)

def query_all_articles():
   """
   Print all the students
   in the database.
   """
   knowledge = session.query(
      Knowledge).all()
   return knowledge

print(query_all_articles())


def query_article_by_topic(topic):
   """
   Find the first student
   in the database, by knowledge = session.query(
      Knowledge).all()
   return knowledge
their name
   """
   knowledge = session.query(
       Knowledge).filter_by(
       topic=topic).first()
   return knowledge
# print(query_article_by_topic("potatoes"))
def query_article_by_rating(rating):
    knowledge = session.query(
        Knowledge).filter_by(
        rating=rating).first()
    return knowledge
print(query_article_by_rating(1))
# knowledge = session.query(
#       Knowledge).all()
#    return knowledge


def delete_article_by_topic(topic):
   """
   Delete all students with a
   certain name from the database.
   """
   session.query(Knowledge).filter_by(
       topic=topic).delete()
   session.commit()


# delete_article_by_topic("eggplants")


def delete_all_articles():
    session.query( Knowledge).delete()
    session.commit()
delete_all_articles()
add_subject("potatoes","potatoes" , 10)
print(query_all_articles())

def edit_article_rating(topic,rating):
    knowledge_object = session.query(
    Knowledge).filter_by( 
    topic=topic).first()
    knowledge_object.rating = rating
    session.commit()
edit_article_rating("potatoes",9)
print(query_all_articles())

