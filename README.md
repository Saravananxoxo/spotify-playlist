# Spotify Playlist Creator

Spotify Playlist Creator is a Python script that allows you to create personalized playlists on Spotify based on your recently played tracks and recommended songs.

## Description

Spotify Playlist Creator is a handy Python script that uses the Spotify API to fetch your recently played tracks, ask for your preferred seed tracks, and then generates a playlist with personalized recommendations. It provides an interactive experience for discovering new music based on your listening habits.

## Installation

1. Clone this repository to your local machine:

```bash
git clone https://github.com/your-username/spotify-playlist-creator.git
cd spotify-playlist-creator
```

2. Install the required Python packages:

```bash
pip install spotipy
```

3. Register your Spotify application and obtain the necessary credentials (Client ID and Client Secret) from the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/applications).

4. Add your Spotify application's Redirect URI to the dashboard settings.

5. Open the `spotify_playlist_creator.py` file and replace the placeholders with your Spotify application's Client ID, Client Secret, and Redirect URI:

```python
# Replace these placeholders with your actual credentials
client_id = "YOUR_CLIENT_ID"
client_secret = "YOUR_CLIENT_SECRET"
redirect_uri = "YOUR_REDIRECT_URI"
```

## Usage

1. Run the `spotify_playlist_creator.py` script:

```bash
python spotify_playlist_creator.py
```

2. Follow the instructions prompted on the terminal:

   - View your recently played tracks.
   - Choose up to 5 seed tracks for recommendations.
   - Create a new playlist and add the recommended tracks to it.

3. Enjoy your personalized playlist on Spotify!

## Features

- Fetches your recently played tracks from Spotify.
- Allows you to select seed tracks for generating personalized recommendations.
- Creates a new private playlist and adds the recommended tracks to it.

## Contributing

We welcome contributions to improve Spotify Playlist Creator. To contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch: `git checkout -b my-feature-branch`.
3. Make changes and commit them: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin my-feature-branch`.
5. Open a pull request.

-Please ensure your code follows the project's coding standards and includes appropriate documentation.

#-# Acknowledgments

Special thanks to the Spotipy library for simplifying the interaction with the Spotify API.

## Contact

For questions or feedback, feel free to reach out:

- Email: saravananxoxo@gmail.com
- Twitter: xoxo23nft

---
