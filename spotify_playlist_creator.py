import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotipy.exceptions import SpotifyException

def main():
    # Create a Spotify client instance with appropriate authentication
    spotify_client = create_spotify_client()

    try:
        # Get the last played tracks for the user (limited to 50)
        last_played_tracks = spotify_client.current_user_recently_played(limit=50)
        # Ask the user how many tracks they want to visualize
        num_tracks_to_visualise = int(input("How many tracks would you like to visualize? "))

        print(f"\nHere are the last {num_tracks_to_visualise} tracks you listened to on Spotify:")
        # Print out the last played tracks and their artists
        for index, track in enumerate(last_played_tracks['items'][:num_tracks_to_visualise]):
            print(f"{index+1}- {track['track']['name']} - {', '.join([artist['name'] for artist in track['track']['artists']])}")

        # Ask the user to input up to 5 track indexes they'd like to use as seeds
        indexes = input("\nEnter a list of up to 5 tracks you'd like to use as seeds. Use indexes separated by a space: ")
        indexes = indexes.split()
        # Get the Spotify track IDs for the chosen seed tracks
        seed_tracks = [last_played_tracks['items'][int(index)-1]['track']['id'] for index in indexes]

        # Get recommended tracks based on the selected seeds
        recommended_tracks = spotify_client.recommendations(seed_tracks=seed_tracks, limit=20)['tracks']
        print("\nHere are the recommended tracks which will be included in your new playlist:")
        # Print out the recommended tracks and their artists
        for index, track in enumerate(recommended_tracks):
            print(f"{index+1}- {track['name']} - {', '.join([artist['name'] for artist in track['artists']])}")

        # Ask the user for the playlist name
        playlist_name = input("\nWhat's the playlist name? ")
        # Create a new playlist for the user (private, not public)
        playlist = spotify_client.user_playlist_create('31cucljabpztavtiviqpjamf2csm', playlist_name, public=False)
        print(f"\nPlaylist '{playlist['name']}' was created successfully.")

        # Get the URIs (unique identifiers) of the recommended tracks
        playlist_track_uris = [track['uri'] for track in recommended_tracks]
        # Add the recommended tracks to the newly created playlist
        spotify_client.user_playlist_add_tracks('31cucljabpztavtiviqpjamf2csm', playlist['id'], playlist_track_uris)
        print(f"\nRecommended tracks successfully added to playlist '{playlist['name']}'.")

    except SpotifyException as e:
        print(f"Error occurred: {e}")

def create_spotify_client():
    # Create and return a Spotify client instance with authentication settings
    return spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="YOUR CLIENT ID",
                                                     client_secret="YOUR CLIENT SECRET",
                                                     redirect_uri="YOUR REDIRECT",
                                                     scope="user-library-read playlist-modify-private playlist-modify-public user-read-recently-played",
                                                     cache_path=".cache"))

if __name__ == "__main__":
    main()
