import os
import re

SECTIONS_DIR = r"C:\Users\dell\.gemini\antigravity\scratch\neoglyn-strict-theme\sections"

# Map of placeholder texts to visually matching Unsplash images
IMAGE_MAP = {
    # Product Main
    "https://via.placeholder.com/800x1000/F5D0C5/001F3F?text=Neoglyn+Lumina+Angle+1": "https://images.unsplash.com/photo-1616683693504-3ea7e9ad6fec?q=80&w=800&auto=format&fit=crop",
    "https://via.placeholder.com/800x1000/EAEAEA/001F3F?text=Lumina+Detail+Front": "https://images.unsplash.com/photo-1596755389378-c31d87e1f467?q=80&w=800&auto=format&fit=crop",
    "https://via.placeholder.com/800x1000/F0F0F0/001F3F?text=Lumina+Detail+Back": "https://images.unsplash.com/photo-1556228578-0d85b1a4d571?q=80&w=800&auto=format&fit=crop",
    "https://via.placeholder.com/800x1000/D9E6E6/001F3F?text=Lumina+In+Use": "https://images.unsplash.com/photo-1615397323608-8e805d7b5b5c?q=80&w=800&auto=format&fit=crop",
    "https://via.placeholder.com/120x150/F5D0C5/001F3F?text=Thumb+1": "https://images.unsplash.com/photo-1616683693504-3ea7e9ad6fec?q=80&w=120&auto=format&fit=crop",
    "https://via.placeholder.com/120x150/EAEAEA/001F3F?text=Thumb+2": "https://images.unsplash.com/photo-1596755389378-c31d87e1f467?q=80&w=120&auto=format&fit=crop",
    "https://via.placeholder.com/120x150/F0F0F0/001F3F?text=Thumb+3": "https://images.unsplash.com/photo-1556228578-0d85b1a4d571?q=80&w=120&auto=format&fit=crop",
    "https://via.placeholder.com/120x150/D9E6E6/001F3F?text=Thumb+4": "https://images.unsplash.com/photo-1615397323608-8e805d7b5b5c?q=80&w=120&auto=format&fit=crop",
    
    # Collection Main
    "https://via.placeholder.com/400x500/F5D0C5/001F3F?text=Pro+Advanced": "https://images.unsplash.com/photo-1616683693504-3ea7e9ad6fec?q=80&w=400&auto=format&fit=crop",
    "https://via.placeholder.com/400x500/EAEAEA/001F3F?text=Repair+Serum": "https://images.unsplash.com/photo-1629198688000-71f23e745b6e?q=80&w=400&auto=format&fit=crop",
    "https://via.placeholder.com/400x500/D9E6E6/001F3F?text=Lumina+Mini": "https://images.unsplash.com/photo-1596755389378-c31d87e1f467?q=80&w=400&auto=format&fit=crop",
    "https://via.placeholder.com/400x500/FAFAFA/001F3F?text=Travel+Case": "https://images.unsplash.com/photo-1599811801759-9686ce88d227?q=80&w=400&auto=format&fit=crop",
    "https://via.placeholder.com/400x500/F0F0F0/001F3F?text=Prep+Cleanser": "https://images.unsplash.com/photo-1556228578-0d85b1a4d571?q=80&w=400&auto=format&fit=crop",
    "https://via.placeholder.com/400x500/E5E5E5/001F3F?text=Pro+Bundle": "https://images.unsplash.com/photo-1615397323608-8e805d7b5b5c?q=80&w=400&auto=format&fit=crop",
    
    # About Us
    "https://via.placeholder.com/600x800/E5E5E5/001F3F?text=Laboratory": "https://images.unsplash.com/photo-1581093458791-9f3c3900df4b?q=80&w=600&auto=format&fit=crop",
    
    # How It Works
    "https://via.placeholder.com/300x300/F5D0C5/001F3F?text=Cleanse": "https://images.unsplash.com/photo-1556228578-0d85b1a4d571?q=80&w=300&auto=format&fit=crop",
    "https://via.placeholder.com/300x300/FAFAFA/001F3F?text=Treat": "https://images.unsplash.com/photo-1616683693504-3ea7e9ad6fec?q=80&w=300&auto=format&fit=crop",
    "https://via.placeholder.com/300x300/EBEBEB/001F3F?text=Glow": "https://images.unsplash.com/photo-1615397323608-8e805d7b5b5c?q=80&w=300&auto=format&fit=crop",
    
    # Contact
    "https://via.placeholder.com/600x400/EAEAEA/001F3F?text=Interactive+Map": "https://images.unsplash.com/photo-1524661135-423995f22d0b?q=80&w=600&auto=format&fit=crop",
    
    # Order Confirm
    "https://via.placeholder.com/64x64/E0EBEB/001F3F?text=Pro": "https://images.unsplash.com/photo-1616683693504-3ea7e9ad6fec?q=80&w=64&auto=format&fit=crop"
}

# Generic fallback for any other via.placeholder.com
FALLBACK_IMG = "https://images.unsplash.com/photo-1616683693504-3ea7e9ad6fec?q=80&w=800&auto=format&fit=crop"

def process_files():
    for root, dirs, files in os.walk(SECTIONS_DIR):
        for file in files:
            if file.endswith('.liquid'):
                filepath = os.path.join(root, file)
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                original_content = content
                
                # Replace mapping
                for old_url, new_url in IMAGE_MAP.items():
                    content = content.replace(old_url, new_url)
                
                # Replace any remaining via.placeholder.com
                content = re.sub(r'https://via\.placeholder\.com/[a-zA-Z0-9\?\=\+\-]+', FALLBACK_IMG, content)
                
                if content != original_content:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(content)
                    print(f"Updated images in {file}")

if __name__ == "__main__":
    process_files()
