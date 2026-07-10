import urllib.request
import json
import os

os.makedirs('assets', exist_ok=True)

# Query Wikimedia Commons API for the direct image URL of File:馬-Chinese characters evolution.png
filename = "File:馬-Chinese characters evolution.png"
api_url = f"https://commons.wikimedia.org/w/api.php?action=query&titles={urllib.parse.quote(filename)}&prop=imageinfo&iiprop=url&format=json"

try:
    print(f"Querying Wikimedia API: {api_url}")
    headers = {'User-Agent': 'Mozilla/5.0'}
    req = urllib.request.Request(api_url, headers=headers)
    with urllib.request.urlopen(req) as response:
        res_data = json.loads(response.read().decode('utf-8'))
        
    pages = res_data.get("query", {}).get("pages", {})
    image_url = None
    for page_id, page_data in pages.items():
        imageinfo = page_data.get("imageinfo", [])
        if imageinfo:
            image_url = imageinfo[0].get("url")
            break
            
    if image_url:
        print(f"Direct Image URL found: {image_url}")
        dest = 'assets/horse_evolution.png'
        img_req = urllib.request.Request(image_url, headers=headers)
        with urllib.request.urlopen(img_req) as img_response, open(dest, 'wb') as out_file:
            out_file.write(img_response.read())
        print(f"Downloaded successfully to {dest}!")
    else:
        print("Failed to find image URL in API response.")
except Exception as e:
    print(f"Error: {e}")
