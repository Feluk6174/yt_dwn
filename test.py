
import pafy 
  
url = "https://www.youtube.com/watch?v=bSfpSOBD30U"
video = pafy.new(url)

audiostreams = video.audiostreams
for i in audiostreams:
    print(i.bitrate, i.extension, i.get_filesize())
  
audiostreams[3].download()