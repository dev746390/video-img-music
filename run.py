from moviepy.editor import ImageClip, AudioFileClip, concatenate_videoclips

# Load audio clip
audio = AudioFileClip("sample.wav")

# Load image clips
images = [ImageClip(f"{i}.jpg").set_duration(audio.duration/6) for i in range(1, 7)]

# Create a video clip by concatenating the image clips
video = concatenate_videoclips(images, method="compose")

# Set the audio of the video clip to the audio clip
video = video.set_audio(audio)

# Write the video to a file
video.write_videofile("output.mp4", fps=30, audio_fps=44100, codec="libx264")
