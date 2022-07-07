"""
    █▀▄▀█ █▀█ █▀█ █ █▀ █ █ █▀▄▀█ █▀▄▀█ █▀▀ █▀█
    █ ▀ █ █▄█ █▀▄ █ ▄█ █▄█ █ ▀ █ █ ▀ █ ██▄ █▀▄
    Copyright 2022 t.me/morisummermods
    Licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International
"""
from bs4 import BeautifulSoup
import requests
from urllib.parse import quote_plus

headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36",
}


def search(request: str) -> list:
    """
    Search songs on musixmatch
    Returns list of dicts with keys "title", "artists", "link", "picture"
    """
    link = "https://www.musixmatch.com/search/"
    page = requests.get(link + quote_plus(request), headers=headers)
    soup = BeautifulSoup(page.text, "html.parser")
    tracks = []
    for track in soup.find_all("li", class_="showArtist"):
        artists = ", ".join(
            [i.get_text() for i in track.find_all("a", class_="artist")]
        )
        title = track.find("a", class_="title")
        track_link = "https://www.musixmatch.com" + title["href"]
        title = track.find("a", class_="title").get_text()
        pic = (
            track.find("img")["srcset"].split()[-2]
            if "has-picture" in str(track)
            else None
        )
        tracks.append(
            {"title": title, "artists": artists, "link": track_link, "picture": pic}
        )
    return tracks


def lyrics(link: str) -> str:
    """Extract lyrics from musixmatch link"""
    page = requests.get(link, headers=headers)
    soup = BeautifulSoup(page.text, "html.parser")
    return "".join(
        p.get_text() + "\n" for p in soup.find_all("p", class_="mxm-lyrics__content")
    )


song = search("Rick Astley")[0]
song_lyrics = lyrics(song["link"])
print(f"Lyrics for {song['artists']} - {song['title']}")
print(song_lyrics)
