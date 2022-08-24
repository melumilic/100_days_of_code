from pprint import pprint
from tokenize import String
from typing import List
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

def playlist_from_date(top_date:String, spotipy_ref:spotipy):
    base_url = "https://www.billboard.com/charts/hot-100/"
    request_url = f"https://www.billboard.com/charts/hot-100/{top_date}/"
    response = requests.get(request_url)
    html_file = response.text

    soup = BeautifulSoup(html_file, "html.parser")

    tracks = soup.select(selector="li ul li h3.c-title")
    tracks = [track.getText().strip() for track in tracks]

    user_id = sp.current_user()["id"]
    playlist_data = sp.user_playlist_create(
        user=user_id, name=f"Top 100 Tracks of {date_input}", public=False
    )
    playlist_id = playlist_data["id"]

    track_ids = get_track_ids(tracks,sp)

    sp.user_playlist_add_tracks(user=user_id, playlist_id=playlist_id, tracks=track_ids)

    return playlist_ref

# takes list of song names and converts them to a list of song URIs
def get_track_ids(track_list:List,spotipy_ref:spotipy)->List:
    track_ids = []
    for track in track_list:
        try:
            track_ids.append(sp.search(q=f"track:{track}", limit=1, type="track")["tracks"]["items"][0]["uri"])
        except IndexError:
            print("track missing")
    return track_ids

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        client_id=os.environ.get("SPOTIPY_CLIENT_ID"),
        client_secret=os.environ.get("SPOTIPY_CLIENT_SECRET"),
        redirect_uri=os.environ.get("SPOTIPY_REDIRECT_URI"),
    )
)

date_input = input("Enter a date(YYYY-MM-DD): ")

playlist_ref = playlist_from_date(top_date=date_input,spotipy_ref=sp)

pprint(playlist_ref)
