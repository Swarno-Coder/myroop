from pytube import YouTube
video = YouTube("https://www.youtube.com/watch?v=-cfyCH3l3Y4&ab_channel=WunderbarFilms")
stream = video.streams.get_highest_resolution()
stream.download()