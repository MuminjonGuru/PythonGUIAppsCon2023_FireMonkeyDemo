import os
import json
import urllib.request
import requests
from delphifmx import *

# Function to get video thumbnails
def _get_thumbs(self, data):
    if "youtube" in data or "youtu.be" in data:
        youtube_id_regex = re.compile("(?:(?<=(v|V)/)|(?<=be/)|(?<=(\?|\&)v=)|(?<=embed/))([\w-]+)")
        video_id = youtube_id_regex.findall(data)
        video_id = ''.join(''.join(elements) for elements in video_id).replace("?", "").replace("&", "")
        video_thumb = "https://img.youtube.com/vi/" + video_id + "/0.jpg"
    elif "vimeo" in data:
        vimeo_id_regex = re.compile("(?:/video/)(\d+)")
        vimeo_id = vimeo_id_regex.findall(data)[0]
        vimeo_request = requests.get("https://vimeo.com/api/v2/video/" + vimeo_id + ".json")
        data = json.loads(vimeo_request.text)
        video_thumb = data[0]['thumbnail_large']
    else:
        video_thumb = ""
    return video_thumb


class FormMain(Form):

    def __init__(self, owner):
        self.__sm = StyleManager()
        self.__sm.SetStyle(StyleStreaming().LoadFromFile(os.path.join(os.getcwd(), 'Transparent.Style')))
        self.ToolBarTop = None
        self.LblTitle = None
        self.TabControl1 = None
        self.TabItemAPOD = None
        self.LayoutTitle = None
        self.Label1 = None
        self.BtnFetchAPOD = None
        self.LayoutDetails = None
        self.LayoutInformation = None
        self.LblAPODDate = None
        self.LblAPODTitle = None
        self.LblAPODExplanation = None
        self.LayoutImage = None
        self.Image1 = None
        self.TabItemAsteroids = None
        self.TabItemInsights = None
        self.LoadProps(os.path.join(os.path.dirname(os.path.abspath(__file__)), "uMain.pyfmx"))

    def BtnFetchAPODClick(self, Sender):
        response = requests.get('https://api.nasa.gov/planetary/apod?api_key=API_ACCESS_KEY')
        data = response.json()

        self.LblAPODDate.Text = data['date']
        self.LblAPODTitle.Text = data['title']
        self.LblAPODExplanation.Text = data['explanation'][:500]

        # check if the URL is a video or an image
        url = data['url']
        if 'youtube' in url or 'vimeo' in url or 'youtu.be' in url:
            # if it's a video, fetch the thumbnail
            img_url = self._get_thumbs(url)
        else:
            img_url = url

        # fetch the image
        urllib.request.urlretrieve(img_url, 'apod.jpg')

        # load the image
        self.Image1.Bitmap.LoadFromFile('apod.jpg')

        os.remove('apod.jpg')