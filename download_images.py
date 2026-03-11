import urllib.request
import ssl
import os

images = {
    'demo-hero-1.jpg': 'https://images.unsplash.com/photo-1596755389378-c31d87e1f467?q=80&w=1200',
    'demo-product-1.jpg': 'https://images.unsplash.com/photo-1629198688000-71f23e745b6e?q=80&w=800',
    'demo-product-2.jpg': 'https://images.unsplash.com/photo-1599811801759-9686ce88d227?q=80&w=800',
    'demo-lab.jpg': 'https://images.unsplash.com/photo-1581093458791-9f3c3900df4b?q=80&w=800',
    'demo-skin-before.jpg': 'https://images.unsplash.com/photo-1556228578-0d85b1a4d571?q=80&w=800',
    'demo-skin-after.jpg': 'https://images.unsplash.com/photo-1515377905703-c4788e51af15?q=80&w=800'
}

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

headers = {'User-Agent': 'Mozilla/5.0'}

os.makedirs('assets', exist_ok=True)

for name, url in images.items():
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, context=ctx) as response:
            with open(f'assets/{name}', 'wb') as f:
                f.write(response.read())
        print(f"Downloaded {name}")
    except Exception as e:
        print(f"Failed {name}: {e}")
