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
add_subject("eggplants","eggplants" , 1)

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
   in the database, by their name
   """
   knowledge = session.query(
       Knowledge).filter_by(
       topic=topic).first()
   return knowledge
print(query_article_by_topic("potatoes"))
def query_article_by_rating(rating):
	knowledge = session.query(
		Knowledge).filter_by(
		rating=rating).first()
	return knowledge
print(query_article_by_rating(1))


def delete_article_by_topic():
	pass

def delete_all_articles():
	pass

def edit_article_rating():
	pass
