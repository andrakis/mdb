Movie Database Example
======================

This is a simple movie database example.

Configuration file: <code>moviedb.ini</code>

Required configuration:

    [Api]
    Key = xxyyzz
    Endpoint = http://example.com/endpoint/
    Providers = provider1, provider2

Optional configuration:

    [Cache]
    Provider = sqlite3
    # Non-persistent cache
    Connection String = :memory:
    # Persistent cache
    Connection String = moviedb.db
