# Quick Start Guide

## Installation

```bash
# Clone the repository
git clone https://github.com/hottoxic97/logsn.git
cd logsn

# Install dependencies
pip install -r requirements.txt

# Run the application
python run_app.py
```

## First Post in 5 Steps

1. **Select an image** (optional)
   - Click "Select Image" button
   - Choose any JPG, PNG, GIF, or BMP file

2. **Type your caption**
   - Start typing in the "Post Caption" area
   - Watch the translation appear automatically below!

3. **Add viral hashtags** (optional)
   - Look at the "Viral Hashtags" section on the right
   - Double-click any hashtag to add it to your caption
   - Or toggle to "Viral Captions" for pre-made captions

4. **Schedule your post**
   - Set the date (format: YYYY-MM-DD)
   - Set the time (format: HH:MM)
   - Click "Schedule Post"

5. **View your post**
   - Your post appears in the "Scheduled Posts" section
   - Click "Toggle Expanded View" to see full details with image!

## Key Features

### Automatic Translation
- Just type - translation happens automatically!
- No buttons to click
- Choose target language: Spanish, French, German, Italian, Portuguese, or Japanese

### Image Minimize
- Click "Minimize Preview" to collapse the image
- Only the filename shows (e.g., "📷 img12345.jpg")
- Click "Show Preview" to restore full image

### Viral Content
- Toggle between:
  - **Viral Hashtags**: #Trending, #Viral, #ForYou, etc.
  - **Viral Captions**: Motivational quotes and captions
- Double-click to insert into your post

### View Modes
- **Compact View**: Quick list with ID, date/time, and caption preview
- **Expanded View**: Full details including:
  - Complete caption
  - Translation
  - Hashtags (highlighted)
  - Actual image preview (not placeholder!)

## Tips

- Posts are automatically saved to `~/.logsn/scheduled_posts.json`
- You can minimize the image to save screen space while typing
- Hashtags in your caption are automatically extracted and highlighted
- Images appear in expanded view after hashtags (like Twitter posts)
- Delete posts by selecting them and clicking "Delete Selected"

## Troubleshooting

**Translation not working?**
- Check your internet connection
- The app works fine without translation (text will be duplicated)

**Can't see image in expanded view?**
- Make sure the image file still exists at the original location
- Try selecting a different image

**App won't start?**
- Make sure Python 3.7+ is installed
- Install dependencies: `pip install -r requirements.txt`
- Check that tkinter is available (usually comes with Python)

## All Bug Fixes Included

✓ Translation is readable and automatic (no manual buttons)
✓ Viral hashtags are clickable and fully functional
✓ Expanded view shows full post details
✓ Minimize button fully collapses image preview
✓ Images are properly embedded (no placeholder text)

---

Enjoy using the Social Media Post Scheduler v4!
