CREATE TABLE test (
    -- Information available from movies listing
    provider TEXT NOT NULL,
    id TEXT NOT NULL,
    title TEXT NOT NULL,
    year INTEGER NOT NULL,
    type TEXT NOT NULL,
    posterUrl TEXT NOT NULL,
    -- Populated asynchronously
    posterData BLOB,
    -- Information only available from specific movie page
    rated TEXT,
    released TEXT,
    runtime TEXT,
    genre TEXT,
    director TEXT,
    writer TEXT,
    actors TEXT,
    plot TEXT,
    language TEXT,
    country TEXT,
    awards TEXT,
    metascore TEXT,
    rating TEXT, -- Arguments could be made for making this a floating point value
    votes INTEGER, -- Parsed from text with number separators
    price TEXT, -- No currency type, floating point should not be used
    PRIMARY KEY (provider, id)
);
