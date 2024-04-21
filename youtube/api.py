from pyyoutube import Api

from config import settings

api = Api(api_key=settings.yt_api_key)
ts = api.search(q="best steam deck accessory")
for item in ts.items[:1]:
    item_dict = item.to_dict_ignore_none()
    print(item_dict)
    snippet = item_dict.get("snippet")
    print(snippet)
