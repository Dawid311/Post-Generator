from moviepy.editor import ImageClip, TextClip, CompositeVideoClip

# Bild und Textdaten
IMAGE_PATH = "_ARC6946.jpg"
VIDEO_OUTPUT = "instagram_post.mp4"
KONZERT_TEXT = "Konzert am 22.08 | 19:00 Uhr\nKatys Garage, Dresden Neustadt\nSei dabei!"

# Bildclip erstellen
image_clip = ImageClip(IMAGE_PATH).set_duration(8).resize(height=1080)

# Textclip animiert einblenden
text_clip = (
    TextClip(KONZERT_TEXT, fontsize=80, color='white', font='Arial-Bold', method='caption', size=image_clip.size, align='center')
    .set_position('center')
    .set_duration(8)
    .crossfadein(2)
)

# Video zusammensetzen
video = CompositeVideoClip([image_clip, text_clip])
video.write_videofile(VIDEO_OUTPUT, fps=24)

print(f"Video gespeichert als {VIDEO_OUTPUT}")
