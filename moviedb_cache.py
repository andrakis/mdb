#!/usr/bin/env python

# Provides a datastore for the movie database that can be reloaded from disk.
# SQLite was chosen because:
#  o No additional software setup or configuration (mysql, memcache, etc)
#  o Persistant data store
#  o Can be moved over to traditional SQL or memcache servers fairly simply
#  o Still provides most of the benefits of traditional SQL:
#    - Table locking
#    - Atomic operations
#    - Transactions
#    Though these are available, this application does not make use of them
#    presently. A more readable and simple implementation is the main goal,
#    and can easily be updated to incorporate such features if they prove
#    desirable at a later date.

from moviedb_config import MDB_Config

class MDB_CacheProvider_SQLite3:
	def __init__(self, connection_string):
		import sqlite3
		print "[Cache] Connecting to sqlite3://%s" % connection_string
		self.connection = sqlite3.connect(connection_string)

class MDB_Cache:
	def __init__(self, config):
		if config.getCacheProvider() == "sqlite3":
			self.provider = MDB_CacheProvider_SQLite3(config.getCacheConnectionString())
		else:
			raise ValueError('Invalid cache provider')

if __name__ == "__main__":
	config = MDB_Config()
	cache = MDB_Cache(config)
