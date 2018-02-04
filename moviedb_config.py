#!/usr/bin/env python

try:
	from configparser import ConfigParser
except ImportError:
	from ConfigParser import ConfigParser  # ver. < 3.0

class MDB_Config:
	def __init__(self, config_file = "moviedb.ini"):
		self.config = ConfigParser()
		self.config.read(config_file)

		self.api_key = self.getConfigValue("Api", "Key")
		self.api_endpoint = self.getConfigValue("Api", "Endpoint")
		self.api_providers = []
		for provider in self.getConfigValue("Api", "Providers", "").split(','):
			self.api_providers.append(provider.strip())
		self.useragent = self.getConfigValue("Api", "User-Agent", "moviedb")
		self.cache_provider = self.getConfigValue("Cache", "Provider", "sqlite3")
		self.cache_connection_string = self.getConfigValue("Cache", "Connection String", "moviedb_cache.db")
	
	def getConfigValue(self, section, option, default = None):
		if self.config.has_section(section) and self.config.has_option(section, option):
			return self.config.get(section, option)
		else:
			return default

	def getApiKey(self): return self.api_key
	def getApiEndpoint(self): return self.api_endpoint
	def getApiProviders(self): return self.api_providers
	def getUserAgent(self): return self.useragent
	def getCacheProvider(self): return self.cache_provider
	def getCacheConnectionString(self): return self.cache_connection_string

	# Has all config been successfully loaded?
	def isValid(self):
		return self.api_key != None and self.api_endpoint != None


if __name__ == "__main__":
	config = MDB_Config()
	if config.isValid():
		print("Api key: %s" % config.getApiKey())
		print("Providers: %s" % config.getApiProviders())
