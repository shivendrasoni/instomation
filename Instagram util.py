from instagram_private_api import Client, ClientError
from moviepy.editor import ImageSequenceClip, TextClip, CompositeVideoClip

class InstagramReel:
    def __init__(self, username, password):
        self.api = Client(username, password)
        self.user_id = self.api.authenticated_user_id

    def post_reel(self, caption, thumbnail, videos):
        try:
            self.api.reel_create(self.user_id, caption, thumbnail, videos)
            print("Reel created successfully!")
        except ClientError as error:
            print(f"Error creating reel: {error}")

class VideoCreator:
    @staticmethod
    def create_text_clip(text):
        return TextClip(text, fontsize=70, color='white').set_position('center').set_duration(2)

    @staticmethod
    def create_image_sequence_clip(images):
        return ImageSequenceClip(images, fps=1).set_duration(6)

    @staticmethod
    def create_reel_video(text, images):
        text_clip = VideoCreator.create_text_clip(text)
        image_clip = VideoCreator.create_image_sequence_clip(images)

        video_clip = CompositeVideoClip([text_clip, image_clip])
        video_clip.write_videofile("video.mp4")

if __name__ == "__main__":
    # Instagram credentials
    username = "YOUR_USERNAME"
    password = "YOUR_PASSWORD"

    # Set the caption and thumbnail for the reel
    caption = "My new reel!"
    thumbnail = "path/to/thumbnail.jpg"

    # Set the list of videos that you want to include in the reel
    videos = ["path/to/video1.mp4", "path/to/video2.mp4"]

    # Post the reel to Instagram
    insta = InstagramReel(username, password)
    insta.post_reel(caption, thumbnail, videos)

    # Create a new reel video
    text = "Your text here"
    images = ["image1.jpg", "image2.jpg", "image3.jpg"]
    VideoCreator.create_reel_video(text, images)
