import json
import requests
from secrets import spotify_user_id, spotify_token

'''''''''


Step 1: Log into YouTube
Step 2: Make sure we grab "Liked Videos"
Step 3: Create a New Playlist for Liked Videos
Step 4: Search the song in Spotify
Step 5: Add the song to the playlist

RESOURCES: YouTube API, Spotify API, Youtube-dl
'''''

class CreateSpotifyPlaylist:

    def __init__(self):
        self.user_id = spotify_user_id
        self.spotify_token = spotify_token

    def get_youtube_client(self):
        pass

    def getliked_videos(selfs):
        pass

    #use Spotify API here
    def createPlaylist(selfs):
        requestBody = json.dumps({
            "name": "Liked Videos From YouTube",
            "description": "My liked videos from YouTube",
             "public": True

        })

        query: "https://api.spotify.com/v1/users/{}/playlists".format(spotify_user_id)

        response = requests.post(
            query,
            data = requestBody,
            headers={
                "Content-Type": "application/json",
                "Authorization": "Bearer{}".format(spotify_token)
            }
        )

        response_json = response.json()


        #playlist id
        return response_json






    def getSpotify_URL(self):

        query = "https://api.spotify.com/v1/search?q=Muse&type=track%2C%20artist&market=US&limit=10&offset=5".format(
            song_name,
            artist
        )



        response = requests.get(
        query,
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer{}".format(spotify_token)
        }
    )




    def addSongtoPlaylist(self):
        pass