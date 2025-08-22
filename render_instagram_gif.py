import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from PIL import Image
import os

def render_gif(html_file, gif_post, gif_story, duration=4, fps=10):
    # Formate
    size_post = (1080, 1080)
    size_story = (1080, 1920)
    frames_post = []
    frames_story = []
    
    # Selenium Headless Chrome
    import tempfile
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--window-size=1080,1920')
    chrome_options.add_argument('--force-device-scale-factor=1')
    # Temporäres User-Data-Verzeichnis
    tmp_dir = tempfile.TemporaryDirectory()
    chrome_options.add_argument(f'--user-data-dir={tmp_dir.name}')
    driver = webdriver.Chrome(options=chrome_options)
    
    # Lokale Datei öffnen
    file_url = f"file://{os.path.abspath(html_file)}"
    driver.get(file_url)
    time.sleep(1)  # Warten bis alles geladen ist
    
    # Screenshots aufnehmen
    for i in range(duration * fps):
        driver.execute_script(f"window.scrollTo(0,0);")
        png = driver.get_screenshot_as_png()
        img = Image.open(BytesIO(png))
        # Quadratisch zuschneiden
        img_post = img.crop((0, 420, 1080, 1500)).resize(size_post, Image.LANCZOS)
        frames_post.append(img_post)
        # Hochformat zuschneiden
        img_story = img.crop((0, 0, 1080, 1920)).resize(size_story, Image.LANCZOS)
        frames_story.append(img_story)
        time.sleep(1/fps)
    driver.quit()
    # GIF speichern
    frames_post[0].save(gif_post, save_all=True, append_images=frames_post[1:], duration=int(1000/fps), loop=0)
    frames_story[0].save(gif_story, save_all=True, append_images=frames_story[1:], duration=int(1000/fps), loop=0)
    print(f"GIFs gespeichert: {gif_post}, {gif_story}")

if __name__ == "__main__":
    from io import BytesIO
    html_file = "instagram_post_pirataone.html"  # Passe hier die Datei an
    render_gif(html_file, "instagram_post.gif", "instagram_story.gif")
