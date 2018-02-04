#!/usr/bin/env python
class MDB_Movies:
	def __init__(self, provider, movies):
		self.provider = provider
		self.movies = movies
	
	def getProvider(self): return self.provider
	
	def getMovies(self): return self.movies
	
	def getMovie(self, id): return self.movies[id]

	def __repr__(self):
		repre = "Movies(%s): [" % self.getProvider()
		movies = []
		for movieid in self.movies:
			movie = self.getMovie(movieid)
			movies.append(str(movie))
		return repre + ", ".join(movies) + "]"

	@staticmethod
	def FromJSON(provider, content):
		movies = {}
		for movieJSON in content["Movies"]:
			movie = MDB_Movie.FromJSON(provider, movieJSON)
			movies[movie.getId()] = movie
		return MDB_Movies(provider, movies)

class MDB_Movie:
	ExtendedFields = [
		'Rated', 'Released', 'Runtime', 'Genre',
		'Director', 'Writer', 'Actors', 'Plot',
		'Language', 'Country', 'Awards', 'Metascore',
		'Rating', 'Votes', 'Price'
	]

	def __init__(self, provider, title, year, id, type, poster):
		self.provider = provider
		self.title = title
		self.year = year
		self.id = id
		self.type = type
		self.poster = poster
		# Extended attributes
		self.extended = {}

	def getProvider(self): return self.provider
	def getTitle(self): return self.title
	def getYear(self): return self.year
	def getId(self): return self.id
	def getType(self): return self.type
	def getPoster(self): return self.poster

	def setExtended(self, name, value): self.extended[name] = value
	def getExtended(self, name):
		if name in self.extended:
			return self.extended[name]
		return None

	def __repr__(self):
		return str(self)
	
	def __str__(self):
		extended = ""
		if MDB_Movie.ExtendedFields[0] in self.extended:
			extended = " (extended)"
		return "(%s) %s%s" % (self.getId(), self.getTitle(), extended)

	@staticmethod
	def FromJSON(provider, content):
		movie = MDB_Movie(provider, content['Title'], content['Year'],
		                  content['ID'], content['Type'], content['Poster'])
		for field in MDB_Movie.ExtendedFields:
			if field in content:
				movie.setExtended(field, content[field])
		return movie

if __name__ == "__main__":
	import json
	apiresponse = json.load(open("api.sample", "r"))
	movies = MDB_Movies.FromJSON("test", apiresponse)
	print(movies)
	apiresponse = json.load(open("api_movie.sample", "r"))
	movie = MDB_Movie.FromJSON("test", apiresponse)
	print(movie)
