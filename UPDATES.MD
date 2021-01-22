## Convert audio to still video for youtube
http://trac.ffmpeg.org/wiki/Encode/YouTube

There's some info about using FFmpeg to encode audio with a still image for YouTube, here, and some advice for doing bulk conversions in Windows, here.

As for encoding, I find that this works:

ffmpeg -loop 1 -r 1 -i pic.jpg -i audio.mp3 -c:a copy -shortest -c:v libx264 output.mp4

The -c:v libx264 encoding considerably reduces the output file size as mentioned at: https://superuser.com/a/1472572/128124

## Extracting Speech from Video using Python
https://towardsdatascience.com/extracting-speech-from-video-using-python-f0ec7e312d38
