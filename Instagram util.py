
# Import the necessary classes from the library
from instagram_private_api import Client, ClientError
from moviepy.editor import ImageSequenceClip, TextClip, CompositeVideoClip
from open_ai_text_gen_util import generate_hashtags_from_topic
from dalle_util import generate_image

def post_reel(topic):
    # Set your Instagram username and password
    username = "YOUR_USERNAME"
    password = "YOUR_PASSWORD"
    caption = topic
    hashtags = generate_hashtags_from_topic(topic)

    # Set the caption and thumbnail for the reel
    caption = "My new reel!"
    thumbnail = "path/to/thumbnail.jpg"

    # Set the list of videos that you want to include in the reel
    videos = ["path/to/video1.mp4", "path/to/video2.mp4"]

    # Authenticate with Instagram and get the user ID
    api = Client(username, password)
    user_id = api.authenticated_user_id

    # Create the reel
    try:
        api.reel_create(user_id, caption, thumbnail, videos)
        print("Reel created successfully!")
    except ClientError as error:
        print(f"Error creating reel: {error}")

def create_reel_video(text, images):
def create_reel_video(script):
    # Set the text and images that you want to include in the video
    text = script
    images = generate_image(script)

    # Create a TextClip object for the text
    text_clip = TextClip(text, fontsize=70, color='white').set_position('center').set_duration(2)

    # Create an ImageSequenceClip object for the images
    image_clip = ImageSequenceClip(images, fps=1).set_duration(6)

    # Combine the text and image clips into a single video clip
    video_clip = CompositeVideoClip([text_clip, image_clip])

    # Save the video to a file
    video_clip.write_videofile("video.mp4")

