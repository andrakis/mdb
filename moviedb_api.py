#!/usr/bin/env python
import json
try:
    import urllib2 as urlreq # Python 2.x
except:
    import urllib.request as urlreq # Python 3.x

from moviedb_exceptions import *
from moviedb_records import MDB_Movies, MDB_Movie

# Helpers for HTTP requests
class MDB_HTTP_Helpers:
	FamilyInformational = 1
	FamilySuccess = 2
	FamilyRedirection = 3
	FamilyClientErrors = 4
	FamilyServerErrors = 5
	FamilyUnknown = 6

	# Get family of http response code
	@staticmethod
	def HttpFamily(code):
		# This isn't all that elegant, but it is more readable than
		# other approaches.
		if code >= 600: return MDB_HTTP_Helpers.FamilyUnknown
		if code >= 500: return MDB_HTTP_Helpers.FamilyServerErrors
		if code >= 400: return MDB_HTTP_Helpers.FamilyClientErrors
		if code >= 300: return MDB_HTTP_Helpers.FamilyRedirection
		if code >= 200: return MDB_HTTP_Helpers.FamilySuccess
		if code >= 100: return MDB_HTTP_Helpers.FamilyInformational
		raise ValueError(code)

# Provides an interface to the remote API
class MDB_ApiLibrary:
	def __init__(self, config):
		self.headers = {
			'x-access-token': config.getApiKey(),
			'User-Agent': config.getUserAgent()
		}
		self.endpoint_base = config.getApiEndpoint()
		self.providers = config.getApiProviders()

	def request(self, endpoint):
		url = self.endpoint_base + endpoint
		print("Requesting %s" % url)
		req = urlreq.Request(url)
		for name in self.headers:
			print("Setting header '%s' => '%s'" % (name, self.headers[name]))
			req.add_header(name, self.headers[name])
		try:
			return urlreq.urlopen(req).read()
		except urlreq.HTTPError as e:
			family = MDB_HTTP_Helpers.HttpFamily(e.code)
			if family == MDB_HTTP_Helpers.FamilyServerErrors:
				print("API is down! (HTTP code %s)" % e.code)
				raise APIUnavailableException()
			elif family == MDB_HTTP_Helpers.FamilyClientErrors:
				print("Invalid API request (HTTP code %s)" % e.code)
				raise APIInvalidRequestException()
			else:
				print("Unknown response code family: %s" % e.code)
				raise e

	def parseMoviesResponse(self, provider, response):
		#print(response.decode('utf8'))
		return MDB_Movies.FromJSON(provider, json.loads(response.decode('utf8')))

	def getMovies(self, provider):
		if provider in self.providers:
			return self.parseMoviesResponse(provider, self.request("%s/movies" % provider))
		return None

	def parseMovieResponse(self, provider, response):
		return MDB_Movie.FromJSON(provider, json.loads(response.decode('utf8')))

	def getMovie(self, provider, movieid):
		if provider in self.providers:
			return self.parseMovieResponse(provider, self.request("%s/movie/%s" % (provider, movieid)))
		return None

if __name__ == "__main__":
	from moviedb_config import MDB_Config
	config = MDB_Config()
	if False == config.isValid():
		print("Missing required configuration.")
	else:
		apilib = MDB_ApiLibrary(config)
		firstProvider = config.getApiProviders()[0]
		print(apilib.getMovies(firstProvider).getMovies())
		print(apilib.getMovie(firstProvider, "cw0076759"))

