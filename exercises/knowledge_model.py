from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Knowledge(Base):
	__tablename__="knowledge"
	knowledge_id = column(integer,primary_key=True)
	subject= column(string)
	wikipdia= column(string)
	rating= column(integer)
	def __repr__(Self):
		return("subject:{}\n"
			"wikipedia:{}\n"
			"rating:{}\n").format(self.subject, self.wikipedia,self.rating)

    # Create a table with 4 columns
	# The first column will be the primary key
	# The second column should be a string representing
	# the name of the Wiki article that you're referencing
	# The third column will be a string representing the 
	# topic of the article. The last column will be
	# an integer, representing your rating of the article.

	pass