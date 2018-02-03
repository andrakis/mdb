#!/usr/bin/env python
import json
try:
    import urllib2 as urlreq # Python 2.x
except:
    import urllib.request as urlreq # Python 3.x

from moviedb_records import MDB_Movies, MDB_Movie

class MDB_ApiLibrary:
	Providers = [ 'cinemaworld', 'filmworld' ]
	Endpoints = {
		'Movies': '%s/movies',
		'MovieById': '%s/movie/%s'
	}

	def __init__(self, ApiKey, ApiEndpoint, UserAgent):
		self.headers = {
			'x-access-token': ApiKey,
			'User-Agent': UserAgent
		}
		self.endpoint_base = ApiEndpoint
		self.providers = MDB_ApiLibrary.Providers
	
	def request(self, endpoint):
		url = self.endpoint_base + endpoint
		print "Requesting %s" % url
		req = urlreq.Request(url)
		for name in self.headers:
			print "Setting header '%s' => '%s'" % (name, self.headers[name])
			req.add_header(name, self.headers[name])
		return urlreq.urlopen(req).read()
	
	def parseMoviesResponse(self, response):
		return MDB_Movies.FromJSON(json.loads(response))
	
	def getMovies(self, provider):
		if provider in MDB_ApiLibrary.Providers:
			return self.parseMoviesResponse(self.request("%s/movies" % provider))
		return []

if __name__ == "__main__":
	from moviedb_config import MDB_Config
	config = MDB_Config()
	if False == config.isValid():
		print "Missing required configuration."
	else:
		apilib = MDB_ApiLibrary(config.getApiKey(), config.getApiEndpoint(), config.getUserAgent())
		print apilib.getMovies('cinemaworld').getMovies()

