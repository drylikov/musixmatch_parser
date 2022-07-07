# Musixmatch parser
Musixmatch songs and lyrics parser via beautifulsoup4

## Requirements:
```
pip install beautifulsoup4
```

## Usage: 
### `search(text)`
Search songs. 
Inputs search request in str format.
Returns tracks list of dicts.

### `lyrics(url)`
Extract lyrics from link.
Inputs url to song in str format.
Return str of extracted lyrics.

## Example:
```python
song = search("Rick Astley")[0]
song_lyrics = lyrics(song["link"])
print(f"Lyrics for {song['artists']} - {song['title']}")
print(song_lyrics)
```
