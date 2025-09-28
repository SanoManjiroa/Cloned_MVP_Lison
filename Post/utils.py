import requests

def upload_to_imbb(image_file, api_key):
    """
    Uploads an image file to ImgBB and returns the direct image URL.
    """
    url = "https://api.imgbb.com/1/upload"
    files = {"image": image_file.read()}  # file-like object
    payload = {"key": api_key}

    response = requests.post(url, data=payload, files=files)
    result = response.json()

    if result.get("success"):
        return result["data"]["url"]  # direct link to the image
    else:
        return None
