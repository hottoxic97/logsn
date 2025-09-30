# Social Media Post Scheduler (logsn)

A comprehensive desktop application for scheduling and managing social media posts with automatic translation, viral hashtags, and image handling.

## Features

- **Automatic Translation**: Text is automatically translated as you type (no manual buttons needed)
- **Viral Hashtags**: Clickable viral hashtags that can be inserted into your posts
- **Viral Captions**: Pre-made viral captions for easy post creation
- **Image Handling**: 
  - Full image preview with minimize/maximize toggle
  - Images are properly embedded in posts (not as placeholder text)
  - Minimized view shows filename only
- **Scheduled Posts**: 
  - View scheduled posts in compact or expanded view
  - Expanded view shows full details including images, hashtags, and translations
  - Toggle between views with a button
- **Post Management**: Schedule, view, and delete posts easily

## Installation

1. Clone this repository:
```bash
git clone https://github.com/hottoxic97/logsn.git
cd logsn
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the application:
```bash
python run_app.py
```

### Creating a Post

1. **Select an Image** (optional): Click "Select Image" to choose an image file
2. **Minimize/Maximize**: Use the "Minimize Preview" button to toggle between full image preview and filename-only display
3. **Enter Caption**: Type your post caption in the text area
4. **Auto Translation**: Translation appears automatically as you type (no buttons needed!)
5. **Add Viral Content**: 
   - Toggle between "Viral Hashtags" and "Viral Captions" using radio buttons
   - Double-click any hashtag or caption to insert it into your post
6. **Schedule**: Set the date and time, then click "Schedule Post"

### Viewing Scheduled Posts

- **Toggle View**: Click "Toggle Expanded View" to switch between:
  - **Compact View**: Shows post ID, date/time, and caption preview
  - **Expanded View**: Shows full details with images, translations, and hashtags
- **Delete Posts**: Select a post and click "Delete Selected"

## Bug Fixes in Version 4

1. ✅ **Translation Entry Readable**: Auto-translation display is now clear and separated from input
2. ✅ **No Manual Translation Buttons**: Translation happens automatically as you type
3. ✅ **Viral Hashtags Restored**: Clickable viral hashtags are back and can be toggled with viral captions
4. ✅ **Image Minimize Fixed**: Minimize button now fully hides preview and shows only filename
5. ✅ **Images in Posts**: Images are now properly embedded in the expanded view, not as placeholder text

## Data Storage

Scheduled posts are automatically saved to `~/.logsn/scheduled_posts.json`

## Requirements

- Python 3.7+
- Pillow (PIL) for image handling
- deep-translator for automatic translation
- tkinter (usually comes with Python)

## License

MIT License