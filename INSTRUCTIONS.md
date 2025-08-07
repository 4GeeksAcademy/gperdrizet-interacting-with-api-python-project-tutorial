# Interacting with Spotify's API

Spotify can be used as a data source for various data science projects. In this exercise, we will learn how to interact with the API of this social network. `Spotipy` is an open-source and Python library that allows high-level use of the Spotify API.

## Step 1: Create a Spotify Developer Account

Before starting to code, you need access to Spotify developer credentials. Visit [developer.spotify.com](https://developer.spotify.com/documentation/web-api).

- Log in with your Spotify account (or create one if you don't have one yet).

- Go to the Dashboard and click on Create an App. Fill in the required fields. In Redirect URI, enter: `http://localhost/`

![Spotify create app](https://github.com/4GeeksAcademy/interacting-with-api-python-project-tutorial/blob/main/assets/spotify_1.PNG?raw=true)

Once the app is created, go to the **Settings** section to copy your `Client ID` and `Client Secret`. You will use them later to authenticate with the API.

## Step 2: Initial Setup

1. **Set up your Spotify API credentials using Codespace secrets**:
   - Go to your GitHub repository settings
   - Navigate to "Secrets and variables" → "Codespaces"
   - Add two repository secrets:
     - `CLIENT_ID`: Your Spotify client ID
     - `CLIENT_SECRET`: Your Spotify client secret
   - These will automatically be available as environment variables in your Codespace

2. **Create a GitHub Codespace**
   - On your forked repository, click the "Code" button
   - Select "Create codespace on main"
   - If the "Create codespace on main" option is grayed out - go to your codespaces list from the three-bar menu at the upper left and delete an old codespace
   - Wait for the environment to load (dependencies are pre-installed)

3. **Start Working**
   - Write your code in `src/assignment.py`
   - Run your code with the command `python src/assignment.py`

## Step 3: Make API Requests

- Start interacting with the Spotify API: Get the top 10 songs of your favorite artist. To do this, you will need to find the artist's `ID` to use it with the library. This identifier is the web address of the artist on Spotify:

![Find the artist's identifier on Spotify](https://github.com/4GeeksAcademy/interacting-with-api-python-project-tutorial/blob/main/assets/spotify_2.png?raw=true)

- Once you have the API response, focus on the `tracks` element, which will contain the most played songs of the artist. Extract the song name, popularity, and duration (in minutes).

> ⚠️ **NOTE** about possible messages when running the code. You might encounter a message like the following after executing the script:

```
 Exception ignored in: <function Spotify.__del__ ...>
 TypeError: isinstance() arg 2 must be a type, a tuple of types, or a union
```

This message originates from the `spotipy` library and **does not affect the functionality of your code or the API results**. You can safely ignore it; it is an internal object cleanup detail (**garbage collection**) that does not interrupt your analysis.

## Step 4: Transform to Pandas DataFrame

Since the result obtained in these steps is likely to be in table format, convert it to a DataFrame by importing the data in its dictionary format. Next, sort the songs by increasing popularity and display the resulting top 3.

## Step 5: Analyze statistical relationship

Does duration have a relationship with popularity? Could we say that a song that lasts a short time may be more popular than a song that lasts longer? Analyze it by plotting a `scatter plot` and argue your answer.


## Feeling like diving deeper? 😎  
**Advanced Exploration of Musical Attributes - Extended Analysis with Interpretative Focus**

If you've already managed to connect to the Spotify API, extract information about your favorite artist, and represent basic data like popularity and duration, we invite you to take on this extended version of the project. This optional activity will allow you to incorporate new musical variables, apply analytical thinking, and write clear and well-supported conclusions based on the data.

---

### Proposal 🚀  
Take advantage of your access to the artist's data to deepen the analysis by including new metrics offered by the API. The goal is to detect interesting patterns or characteristics and express them in a way that is understandable to any reader.

#### Recommended variables to explore:

- **Danceability**: How easy it is to dance to the song.
- **Valence**: How positive or happy it sounds.
- **Energy**: Overall intensity or strength.
- **Tempo**: Speed (in BPM).

---

1. **Retrieve additional attributes:** Use the `audio_features()` method to obtain the musical attributes of the artist's songs:

    ```python
    track_ids = [track["id"] for track in results["tracks"]]
    features = sp.audio_features(track_ids)
    ```

2. **Create a new DataFrame with complete information:** Combine the previously obtained data (`name, popularity, duration`) with the new metrics.

3. **Perform a simple analysis:** Explore average values, look for extremes, identify visual or statistical correlations.

    - What values stand out for this artist?

    - Is there any trend between popularity and another attribute?

    - Is there something unexpected you found?

    Create a simple chart to complement your conclusion.

4. **Make your work visible:** Based on the analysis, write one or two sentences summarizing what you discovered and post it on LinkedIn. The goal is to communicate your findings objectively, briefly, and with data-backed evidence.

    > **Example:**
    >
    > "The most popular songs of the analyzed artist have an average “danceability” level of > 0.82, suggesting a clear focus on danceable tracks. 🕺💃 #SpotifySecrets"
