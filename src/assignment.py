import os
import spotipy
import matplotlib.pyplot as plt
from spotipy.oauth2 import SpotifyClientCredentials

# Load credentials
client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')

# Set artist
artist_id = '3TVXtAsR1Inumwj472S9r4'

if __name__ == '__main__':

    # Connect to Spotify
    connection = spotipy.Spotify(
        auth_manager=SpotifyClientCredentials(
            client_id=client_id,
            client_secret=client_secret
        )
    )

    # Get top tracks for artest
    response = connection.artist_top_tracks(artist_id)

    if response:

        # Get the track listing


        # Get the name, popularity and duration for each track


        # Plot the duration vs popularity


        # Save the plot
        plt.savefig('./assets/duration_plot.jpg', dpi=300)
