import edge_tts
import moviepy.editor as mp
from PIL import Image
import os

# Step 1: Convert Text to Speech
def text_to_speech(text, output_audio):
    tts = edge_tts.Communicate(text, "en-US-JennyNeural")
    tts.save(output_audio)

# Step 2: Create a Video from Images and Audio
def create_video(image_folder, audio_file, output_video):
    images = [os.path.join(image_folder, img) for img in os.listdir(image_folder) if img.endswith(".png")]
    images.sort()
    clips = [mp.ImageClip(img).set_duration(5) for img in images]
    
    video = mp.concatenate_videoclips(clips, method="compose")
    audio = mp.AudioFileClip(audio_file)
    video = video.set_audio(audio)
    
    video.write_videofile(output_video, fps=24)

# User Inputs
script_text = "The Art of War meets Stoicism. A strategic guide to life."
audio_output = "narration.mp3"
image_directory = "images"
video_output = "final_video.mp4"

# Run the Process
text_to_speech(script_text, audio_output)
create_video(image_directory, audio_output, video_output)

print("Video generation complete!")
