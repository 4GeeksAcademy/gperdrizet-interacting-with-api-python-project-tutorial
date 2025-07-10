import os
import spotipy
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
from spotipy.oauth2 import SpotifyClientCredentials

# Load credentials
client_id=os.getenv('CLIENT_ID')
client_secret=os.getenv('CLIENT_SECRET')

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

    # Get top tracks for artest
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

        # Run ordinary least squares regression on popularity
        Y=np.array(popularities).reshape(-1, 1)
        X=durations
        X=sm.add_constant(X)

        model=sm.OLS(Y,X)
        results=model.fit()
        print(results.summary())
        p_value=results.summary2().tables[1]['P>|t|'].iloc[1]

        # Plot the duration vs popularity
        plt.title('Dependence of track popularity on duration')
        plt.scatter(durations, popularities, color='black')
        plt.plot(durations, results.predict(X), color='red')
        plt.text(2.1, 75, f'Regression coefficent p-value = {p_value:.3f}')
        plt.ylabel('Popularity')
        plt.xlabel('Duration')
        plt.savefig('./assets/duration_plot.jpg', dpi=300)
