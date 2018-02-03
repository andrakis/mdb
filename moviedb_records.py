#!/usr/bin/env python
class MDB_Movies:
	def __init__(self, movies):
		self.movies = movies
	
	def getMovies(self):
		return self.movies
	
	def getMovie(self, id):
		return self.movies[id]
	
	@staticmethod
	def FromJSON(content):
		movies = {}
		for movieJSON in content["Movies"]:
			movie = MDB_Movie.FromJSON(movieJSON)
			movies[movie.getId()] = movie
		return MDB_Movies(movies)

class MDB_Movie:
	def __init__(self, title, year, id, type, poster):
		self.title = title
		self.year = year
		self.id = id
		self.type = type
		self.poster = poster

	def getTitle(self): return self.title
	def getYear(self): return self.year
	def getId(self): return self.id
	def getType(self): return self.type
	def getPoster(self): return self.poster

	@staticmethod
	def FromJSON(content):
		return MDB_Movie(content['Title'], content['Year'],
		                 content['ID'], content['Type'], content['Poster'])

if __name__ == "__main__":
	import json
	apiresponse = json.load(open("api.sample", "r"))
	movies = MDB_Movies.FromJSON(apiresponse)
	print movies
	print movies.getMovies()
