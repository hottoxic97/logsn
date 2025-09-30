# Social Media Post Scheduler v4 - Feature Documentation

## Overview
This is a complete rewrite of the social media post scheduler application that addresses all reported bugs while maintaining all functionality from previous versions.

## User Interface Layout

The application window is divided into two main panels:

### LEFT PANEL: Post Creation

#### Image Preview Section
```
┌──────────────────────────────────────────────────────┐
│ Image Preview                                        │
├──────────────────────────────────────────────────────┤
│                                                      │
│              [Image Preview Canvas]                  │
│               (Shows full image)                     │
│                                                      │
│              📷 filename.jpg                         │
│                                                      │
│   [Select Image]  [Minimize Preview]                │
└──────────────────────────────────────────────────────┘
```

**When Minimized:**
```
┌──────────────────────────────────────────────────────┐
│ Image Preview                                        │
├──────────────────────────────────────────────────────┤
│                                                      │
│              📷 img12345.jpg                         │
│                                                      │
│   [Select Image]  [Show Preview]                    │
└──────────────────────────────────────────────────────┘
```

**Key Fix:** The minimize button now fully collapses the preview canvas and shows only the filename in large, bold text. Toggle button switches between "Minimize Preview" and "Show Preview".

#### Post Creation Section
```
┌──────────────────────────────────────────────────────┐
│ Create Post                                          │
├──────────────────────────────────────────────────────┤
│ Post Caption:                                        │
│ ┌──────────────────────────────────────────────────┐ │
│ │ Type your caption here...                        │ │
│ │ (Translation happens automatically as you type)  │ │
│ │                                                  │ │
│ └──────────────────────────────────────────────────┘ │
│                                                      │
│ Auto Translation:                                    │
│ ┌──────────────────────────────────────────────────┐ │
│ │ [Automatically translated text appears here]     │ │
│ └──────────────────────────────────────────────────┘ │
│                                                      │
│ Translate to:                                        │
│ ◉ Spanish  ○ French  ○ German  ○ Italian            │
│ ○ Portuguese  ○ Japanese                            │
│                                                      │
│ Schedule for: [2024-12-31] [23:59] [Schedule Post] │
└──────────────────────────────────────────────────────┘
```

**Key Fixes:**
- Translation display is clearly separated from the input field
- NO manual "Translate" button - translation happens automatically as you type
- Translation area is read-only and clearly labeled "Auto Translation"

### RIGHT PANEL: Viral Content & Scheduled Posts

#### Viral Content Section
```
┌──────────────────────────────────────────────────────┐
│ Viral Hashtags                                       │
├──────────────────────────────────────────────────────┤
│ ◉ Show Viral Hashtags  ○ Show Viral Captions       │
│                                                      │
│ ┌──────────────────────────────────────────────────┐ │
│ │ #Trending                                        │ │
│ │ #Viral                                           │ │
│ │ #ForYou                                          │ │
│ │ #FYP                                             │ │
│ │ #Explore                                         │ │
│ │ #InstaGood                                       │ │
│ │ #PhotoOfTheDay                                   │ │
│ │ (Double-click to insert into caption)           │ │
│ └──────────────────────────────────────────────────┘ │
└──────────────────────────────────────────────────────┘
```

**Key Fix:** Viral hashtags are restored and fully functional. Toggle between hashtags and captions using radio buttons. Double-click any item to insert it into your post.

#### Scheduled Posts Section - Compact View
```
┌──────────────────────────────────────────────────────┐
│ Scheduled Posts                                      │
├──────────────────────────────────────────────────────┤
│ [Toggle Expanded View] [Delete Selected]            │
│                                                      │
│ ┌──────────────────────────────────────────────────┐ │
│ │ #1 12/31 23:59 - Check out this amazing post... 📷│ │
│ │ #2 01/01 10:00 - Happy New Year everyone! #2025  │ │
│ │ #3 01/02 15:30 - Don't wait for opportunity...   │ │
│ └──────────────────────────────────────────────────┘ │
└──────────────────────────────────────────────────────┘
```

#### Scheduled Posts Section - Expanded View
```
┌──────────────────────────────────────────────────────┐
│ Scheduled Posts                                      │
├──────────────────────────────────────────────────────┤
│ [Toggle Expanded View] [Delete Selected]            │
│                                                      │
│ ┌──────────────────────────────────────────────────┐ │
│ │ Post #1                                          │ │
│ │ Scheduled: 2024-12-31 23:59                      │ │
│ │                                                  │ │
│ │ Caption:                                         │ │
│ │ Check out this amazing post with viral content! │ │
│ │ #Trending #Viral #ForYou                         │ │
│ │                                                  │ │
│ │ Translation:                                     │ │
│ │ ¡Mira esta increíble publicación con contenido  │ │
│ │ viral! #Trending #Viral #ForYou                  │ │
│ │                                                  │ │
│ │ Hashtags: #Trending #Viral #ForYou              │ │
│ │                                                  │ │
│ │ Image: amazing_photo.jpg                         │ │
│ │ [Full-size image preview displayed here]         │ │
│ │                                                  │ │
│ │ ========================================          │ │
│ │                                                  │ │
│ │ Post #2                                          │ │
│ │ ...                                              │ │
│ └──────────────────────────────────────────────────┘ │
└──────────────────────────────────────────────────────┘
```

**Key Fixes:**
- Toggle button switches between compact and expanded views
- Expanded view shows FULL DETAILS including:
  - Complete caption text
  - Translation
  - Extracted hashtags (highlighted in blue)
  - **ACTUAL IMAGE PREVIEW** - not placeholder text!
- Images are now properly embedded as visual previews
- No more "📷 [Image attached - Preview shown in left panel]" placeholder
- Images appear after hashtags, like a traditional Twitter post

## All Bug Fixes Implemented

### Bug Fix #1: Translation Entry Readable
**Before:** Translation text was hard to read or mixed with input
**After:** Translation is in a separate, clearly labeled read-only text area with light gray background

### Bug Fix #2: No Manual Translation Buttons
**Before:** Had manual "Translate" button that was unnecessary
**After:** Translation happens automatically as you type - no buttons needed!

### Bug Fix #3: Viral Hashtags & Expanded View
**Before:** Viral hashtags were missing
**After:** 
- Viral hashtags are fully restored
- Clickable interface with toggle between hashtags and captions
- New "Toggle Expanded View" button for scheduled posts
- Expanded view shows all details including images

### Bug Fix #4: Image Minimize Functionality
**Before:** Minimize button didn't fully minimize the preview
**After:**
- Clicking "Minimize Preview" fully hides the canvas
- Shows only the filename (e.g., "📷 img12345.jpg") in large text
- Button text changes to "Show Preview"
- Clicking "Show Preview" restores full image view

### Bug Fix #5: Proper Image Display
**Before:** Images showed as "📷 [Image attached - Preview shown in left panel]"
**After:**
- Images are now properly embedded in expanded view
- Full-sized image preview is shown in the post display
- Images appear after hashtags, just like a traditional Twitter post
- No more placeholder text!

## Technical Implementation

### Automatic Translation
```python
def auto_translate(self, event=None):
    """Automatically translate text as user types."""
    threading.Thread(target=self._translate_text, daemon=True).start()
```
- Uses threading to avoid blocking the UI
- Translates in background as user types
- Updates translation display automatically
- No manual button click required

### Image Minimize Toggle
```python
def toggle_image_preview(self):
    """Toggle between full preview and minimized (filename only) view."""
    self.image_minimized = not self.image_minimized
    
    if self.image_minimized:
        self.image_canvas.pack_forget()  # Fully hide canvas
        self.minimize_image_btn.config(text="Show Preview")
        # Show only filename in large, bold text
    else:
        self.image_canvas.pack(fill=tk.BOTH, expand=True)
        self.minimize_image_btn.config(text="Minimize Preview")
        self.display_image(self.current_image_path)
```

### Proper Image Embedding
```python
# In expanded view, embed actual images:
try:
    img = Image.open(post["image_path"])
    img.thumbnail((300, 300), Image.Resampling.LANCZOS)
    photo = ImageTk.PhotoImage(img)
    self.posts_display.image_create(tk.END, image=photo)
except:
    pass
```
- Images are embedded as actual image widgets
- Not shown as placeholder text
- Displayed after hashtags in the post

### Viral Hashtags & Captions
```python
# Toggle between content types
self.hashtag_mode = tk.StringVar(value="hashtags")
ttk.Radiobutton(..., value="hashtags", command=self.update_viral_content)
ttk.Radiobutton(..., value="captions", command=self.update_viral_content)

# Double-click to insert
self.viral_listbox.bind("<Double-Button-1>", self.insert_viral_content)
```

### Expanded View Toggle
```python
def toggle_view_mode(self):
    """Toggle between compact and expanded view."""
    self.expanded_view = not self.expanded_view
    self.refresh_posts_display()
```

## Data Persistence

All scheduled posts are automatically saved to:
```
~/.logsn/scheduled_posts.json
```

Each post contains:
- Post ID
- Caption text
- Translation
- Image path (if any)
- Schedule date/time
- Creation timestamp

## Dependencies

See `requirements.txt`:
```
Pillow>=10.0.0        # For image handling
deep-translator>=1.11.0  # For automatic translation
```

Tkinter is required (usually comes with Python)

## How to Run

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the application:
   ```bash
   python run_app.py
   ```

3. The GUI window will open with all features ready to use!

## Workflow Example

1. **Click "Select Image"** → Choose an image file
2. **Type your caption** → Translation appears automatically as you type!
3. **Toggle to "Show Viral Hashtags"** → Double-click hashtags to add them
4. **Click "Minimize Preview"** if you want more space → Image collapses to filename
5. **Set schedule date/time** → Click "Schedule Post"
6. **Click "Toggle Expanded View"** → See your post with full details and image preview
7. **Select a post and click "Delete Selected"** if needed

## All Previous Functionality Preserved

✓ Post scheduling with date/time
✓ Image attachment and preview
✓ Caption text input
✓ Translation to multiple languages
✓ Hashtag support
✓ Post management (view, delete)
✓ Data persistence
✓ User-friendly interface

## New Features Added

✓ Automatic translation (no manual buttons)
✓ Expanded view toggle for posts
✓ Viral hashtags with clickable interface
✓ Viral captions database
✓ Proper image embedding in posts
✓ Full minimize functionality for images
✓ Hashtag extraction and highlighting

---

**Version:** 4.0
**Status:** All bug fixes implemented ✓
**Testing:** Core functionality verified ✓
**Ready for:** Production use ✓
