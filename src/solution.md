# Interacting with the Spotify API

Spotify can be used as a data source for various data science projects. In this exercise, we will learn how to interact with the API of this social network. `Spotipy` is an open-source Python library that allows high-level use of the Spotify API.

## Step 1: Create a Spotify Developer Account

Before starting to code, you need access to Spotify developer credentials. Visit [developer.spotify.com](https://developer.spotify.com/documentation/web-api).

- Log in with your Spotify account (or create one if you don't have one yet).

- Go to the Dashboard and click on Create an App. Fill in the required fields. In Redirect URI, enter: `http://localhost/`

![Spotify create app](https://github.com/4GeeksAcademy/interacting-with-api-python-project-tutorial/blob/main/assets/spotify_1.PNG?raw=true)

Once the app is created, go to the **Settings** section to copy your `Client ID` and `Client Secret`. You will use them later to authenticate with the API.

## Step 2: Initial configuration

- Create an `app.py` file inside the `./src/` folder.
- Install all the requirements from the `requirements.txt` file or just the required library.

```python
! pip install spotipy
```

    Collecting spotipy
      Downloading spotipy-2.23.0-py3-none-any.whl (29 kB)
    Collecting redis>=3.5.3 (from spotipy)
      Downloading redis-4.6.0-py3-none-any.whl (241 kB)
        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 241.1/241.1 kB 11.2 MB/s eta 0:00:00
    Requirement already satisfied: requests>=2.25.0 in /usr/local/python/3.10.8/lib/python3.10/site-packages (from spotipy) (2.27.1)
    Requirement already satisfied: six>=1.15.0 in /home/codespace/.local/lib/python3.10/site-packages (from spotipy) (1.16.0)
    Requirement already satisfied: urllib3>=1.26.0 in /usr/local/python/3.10.8/lib/python3.10/site-packages (from spotipy) (1.26.16)
    Collecting async-timeout>=4.0.2 (from redis>=3.5.3->spotipy)
      Downloading async_timeout-4.0.2-py3-none-any.whl (5.8 kB)
    Requirement already satisfied: certifi>=2017.4.17 in /home/codespace/.local/lib/python3.10/site-packages (from requests>=2.25.0->spotipy) (2023.5.7)
    Requirement already satisfied: charset-normalizer~=2.0.0 in /usr/local/python/3.10.8/lib/python3.10/site-packages (from requests>=2.25.0->spotipy) (2.0.12)
    Requirement already satisfied: idna<4,>=2.5 in /home/codespace/.local/lib/python3.10/site-packages (from requests>=2.25.0->spotipy) (3.4)
    Installing collected packages: async-timeout, redis, spotipy
    Successfully installed async-timeout-4.0.2 redis-4.6.0 spotipy-2.23.0

## Step 3: Environment variables

You already have the `.env` file in the root of the project. Make sure it contains the following variables with your Spotify credentials (replace the content with your own data):

```env
CLIENT_ID=your_client_id
CLIENT_SECRET=your_client_secret
```

> ⚠️ It is important to place your data in environment variables to avoid exposing your credentials if you upload the project to a repository.

Now, in the `app.py` file, add the following code to read the environment variables:

```python
import os
import pandas as pd
import matplotlib.pyplot as plt
from dotenv import load_dotenv

# load the .env file variables
load_dotenv()

# Get credential values
client_id = os.environ.get("CLIENT_ID")
client_secret = os.environ.get("CLIENT_SECRET")
```

With this, your credentials will be ready to use for authentication with the Spotify API.

## Step 4: Initialize Spotipy library


- Import Spotipy.
- Connect to the API. To do this, you can use the `spotipy.Spotify()` function.

    ```python
    import spotipy
    from spotipy.oauth2 import SpotifyClientCredentials

    auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    spotify = spotipy.Spotify(auth_manager=auth_manager)
    ```

    > 💡 NOTE: Use the following documentation as a guide for the parameters: https://spotipy.readthedocs.io/en/2.22.1

## Step 5: Make API requests

In this case, I have chosen Drake. First, I get his ID by searching for his Spotify page and getting it from the URI. Now, I perform the search for his top 10 songs.

```py
artist_id = "3TVXtAsR1Inumwj472S9r4"

# Get the top tracks of an artist
results = spotify.artist_top_tracks(artist_id)

songs = []
for track in results['tracks']:
    songs.append({
        'name': track['name'],
        'popularity': track['popularity'],
        'duration_min': track['duration_ms'] / 60000
    })
```

## Step 6: Transform to Pandas DataFrame

Once we have modified the answer, we create the Pandas DataFrame from it:

```py

tracks_df = pd.DataFrame(songs)

print(tracks_df.head(3))
```

## Step 7: Analyze statistical relationship

A scatter plot is a good alternative to determine visually and graphically whether two variables may or may not be related to each other:

```py
plt.scatter(df['duration_min'], df['popularity'])
plt.xlabel('Duration (minutes)')
plt.ylabel('Popularity')
plt.title('Relationship between duration and popularity')
plt.show()
```

![Scatter plot of popularity and duration of songs](https://github.com/4GeeksAcademy/interacting-with-the-twitter-api-project-tutorial/blob/main/assets/scatter_plot.png?raw=true)

As can be seen, there is no direct relationship between the length of the song and its popularity.
