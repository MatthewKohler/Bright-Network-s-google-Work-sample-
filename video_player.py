"""A video player class."""

from video_library import VideoLibrary


class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        print("all videos")
        
        list_Of_Vidoes = []
        """
        list_Of_Videos.append(VideoLibrary())
        print(list_Of_Vidoes)
        
        file1 = open('videos.txt', 'r')
        count = 0
 
        while True:
            count += 1
        # Get next line from file
            line = file1.readline()
            list_Of_Vidoes.append(line) 
            
 
    # if line is empty
    # end of file is reached
            if not line:
                break
            print("{}".format( line.strip()))

        print(list_Of_Vidoes)
        """
        Video_File = open('videos.txt', 'r')
        letter_Count = 1
        letter_Count_Two = 1 
        n = 1
        
        while True:
            char_Break_One = Video_File.read(1)
            if char_Break_One == ("|"):
                
                phrase_One = Video_File.read(letter_Count)
                print(phrase_One)
                list_Of_Vidoes.insert(n, phrase_One)
                break
            letter_Count = letter_Count + 1

        while True:
            char_Break_Two = Video_File.read(1)
            if char_Break_Two == ("|"):
                phrase_Two = Video_File.read( letter_Count_Two)
                print(phrase_Two)
                break
            letter_Count_Two = letter_Count_Two + 1
                    









        

    def play_video(self, video_id):
        search_File = open('videos.txt', "r")
        for line in search_File:
            if video_id in line:
                print ("Playing video", video_id)
    

    def stop_video(self):
        """Stops the current video."""

        print("stop_video needs implementation")

    def play_random_video(self):
        """Plays a random video from the video library."""

        print("play_random_video needs implementation")

    def pause_video(self):
        """Pauses the current video."""

        print("pause_video needs implementation")

    def continue_video(self):
        """Resumes playing the current video."""

        print("continue_video needs implementation")

    def show_playing(self):
        """Displays video currently playing."""

        print("show_playing needs implementation")

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.
        Args:
            playlist_name: The playlist name.
        """
        print("create_playlist needs implementation")

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.
        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        print("add_to_playlist needs implementation")

    def show_all_playlists(self):
        """Display all playlists."""

        print("show_all_playlists needs implementation")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.
        Args:
            playlist_name: The playlist name.
        """
        print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.
        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.
        Args:
            playlist_name: The playlist name.
        """
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.
        Args:
            playlist_name: The playlist name.
        """
        print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.
        Args:
            search_term: The query to be used in search.
        """
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.
        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.
        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.
        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
