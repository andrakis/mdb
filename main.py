#!/usr/bin/env python

# Main application entry point
from moviedb_config import MDB_Config
from moviedb_cache import MDB_Cache
from moviedb_api import MDB_ApiLibrary

if __name__ == "__main__":
	config = MDB_Config()
	if False == config.isValid():
		print("Configuration not valid. See README.md")
	else:
		cache = MDB_Cache(config)
		apilib = MDB_ApiLibrary(config)

		print("Attempting to populate cache...")
		for provider in config.getApiProviders():
			cache.populateProvider(provider, apilib)

		print("Startup complete")

