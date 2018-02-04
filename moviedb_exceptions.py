#!/usr/bin/env python

# Various exceptions specific to this application.

# API unavailable at this time - server down or timing out (but not 404)
class APIUnavailableException(Exception):
	pass

# API reported 404, URL is probably incorrect
class APIInvalidRequestException(Exception):
	pass

# Invalid cache provider
class InvalidCacheProviderException(Exception):
	pass
