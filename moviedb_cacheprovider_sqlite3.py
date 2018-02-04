import sqlite3

from moviedb_exceptions import APIUnavailableException
from moviedb_cacheprovider import MDB_CacheProvider

class MDB_CacheProvider_SQLite3(MDB_CacheProvider):
	def setupConnection(self, config):
		print("[Cache] Connecting to sqlite3://%s" % config)
		self.connection = sqlite3.connect(config)
		self.providers = {}

	def setupTables(self):
		with open('moviedb_cache.sql', 'r') as table_cache:
			try:
				print("[Cache] Attempting to create table")
				self.connection.execute(table_cache.read())
				print("[Cache] Table created")
			except sqlite3.OperationalError:
				print("[Cache] Table already present")
	
	def populateCache(self):
		print("[Cache] Populating cache")

	def populateProvider(self, provider, api):
		print("[Cache] Populating for provider %s..." % provider)
		try:
			movies = api.getMovies(provider)
			self.providers[provider] = movies
			return True
		except APIUnavailableException:
			print("API not available, unable to populate cache")
			return False
