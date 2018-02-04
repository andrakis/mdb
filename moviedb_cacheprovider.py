#!/usr/bin/env python
from moviedb_exceptions import InvalidCacheProviderException

# Abstract class for a cache provider
class MDB_CacheProvider:
	def __init__(self, config):
		self.setupConnection(config)
		self.setupTables()
		self.populateCache()

	# Setup database connection
	def setupConnection(self, config): raise NotImplementedError()
	# Setup tables
	def setupTables(self): raise NotImplementedError()
	# Populate cache
	def populateCache(self): raise NotImplementedError()
	# Populate cache via provider
	def populateProvider(self, provider, api): raise NotImplementedError()

# When cache is unavailable
class MDB_CacheProvider_None(MDB_CacheProvider):
	def setupConnection(self, config):
		print("Cache unavailable")

	def setupTables(self):
		print("No tables to setup")

	def populateCache(self):
		print("No cache to populate")

	def populateProvider(self, provider, api):
		print("No cache to populate")

class MDB_CacheProviders:
	@staticmethod
	def GetCacheProvider(config):
		provider = config.getCacheProvider()
		if provider == 'sqlite3':
			try:
				from moviedb_cacheprovider_sqlite3 import MDB_CacheProvider_SQLite3
				return MDB_CacheProvider_SQLite3(config.getCacheConnectionString())
			except:
				print("Failed to setup sqlite3, package missing?")
		return MDB_CacheProvider_None(None)

if __name__ == "__main__":
	cache = MDB_CacheProviders.GetCacheProvider('sqlite3', ':memory:')
