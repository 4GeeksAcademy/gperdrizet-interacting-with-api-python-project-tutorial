import os
import spotipy
import matplotlib.pyplot as plt
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyClientCredentials

# load the .env file variables
load_dotenv()

# Load credentials
client_id=os.environ.get('CLIENT_ID')
client_secret=os.environ.get('CLIENT_SECRET')

# Set artist
artist_id='3TVXtAsR1Inumwj472S9r4'

if __name__ == '__main__':

    # Connect to Spotify
    connection=spotipy.Spotify(
        auth_manager=SpotifyClientCredentials(
            client_id=client_id,
            client_secret=client_secret
        )
    )

    response=connection.artist_top_tracks(artist_id)

    if response:

        # Get the track listing
        tracks=response['tracks']

        # Get the name, popularity and duration for each track
        names=[]
        durations=[]
        popularities=[]

        for track in tracks:
            names.append(track['name'])
            durations.append(track['duration_ms']/(1000*60))
            popularities.append(track['popularity'])

        # Plot the duration vs popularity
        plt.title('Dependence of track popularity on duration')
        plt.scatter(popularities, durations, color='black')
        plt.ylabel('Popularity')
        plt.xlabel('Duration')
        plt.savefig('./duration_plot.jpg', dpi=300)
