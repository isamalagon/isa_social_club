
# Egypt Travel Tips 

Welcome to my mini Django project! This app shares travel tips for Egypt — things I wish I knew before, or stuff I learned from friends and blogs. 

# What it does

- Lets you view and add travel tips about Egypt  
- Has a fun little status endpoint just for vibes  
- Uses Django + Django REST Framework  
- No fancy frontend — just clean JSON and working endpoints

# Endpoints

| URL               | What it does                     |
|-------------------|----------------------------------|
| `/egypt/`         | List all tips or add a new one   |
| `/egypt/status/`  | Returns a fun little message     |

# Sample tips

```json
{
  "title": "bring small cash",
  "description": "for snacks, water, and random tips lol"
}
