#!/usr/bin/env python3
"""
Social Media Post Scheduler - Version 4
A comprehensive application for scheduling and managing social media posts with viral hashtags,
automatic translation, and image handling.
"""

import tkinter as tk
from tkinter import ttk, scrolledtext, filedialog, messagebox
from datetime import datetime, timedelta
import json
import os
from pathlib import Path
from PIL import Image, ImageTk
import threading
from typing import Dict, List, Optional
import webbrowser

# Try to import translation library (fallback to basic implementation if not available)
try:
    from deep_translator import GoogleTranslator
    TRANSLATION_AVAILABLE = True
except ImportError:
    TRANSLATION_AVAILABLE = False
    print("deep_translator not installed. Translation will be simulated.")


class SocialMediaScheduler:
    """Main application class for social media post scheduling."""
    
    def __init__(self, root):
        self.root = root
        self.root.title("Social Media Post Scheduler v4")
        self.root.geometry("1400x900")
        
        # Data storage
        self.scheduled_posts = []
        self.current_image_path = None
        self.image_minimized = False
        self.expanded_view = False
        
        # Viral hashtags database (sample data - would be fetched from API in production)
        self.viral_hashtags = [
            "#Trending", "#Viral", "#ForYou", "#FYP", "#Explore",
            "#InstaGood", "#PhotoOfTheDay", "#Love", "#Instagood",
            "#Fashion", "#Beautiful", "#Happy", "#Cute", "#TBT",
            "#FollowMe", "#Like4Like", "#Follow", "#Picoftheday", "#Art"
        ]
        
        # Viral captions database
        self.viral_captions = [
            "Don't wait for opportunity. Create it.",
            "Great things never come from comfort zones.",
            "Dream big, work hard, stay focused.",
            "Be yourself; everyone else is already taken.",
            "In a world where you can be anything, be kind.",
            "Life is short, make every moment count.",
            "Success doesn't just find you. You have to go out and get it.",
            "The best time for new beginnings is now."
        ]
        
        self.setup_ui()
        self.load_scheduled_posts()
        
    def setup_ui(self):
        """Set up the main user interface."""
        # Create main container with paned window
        main_paned = ttk.PanedWindow(self.root, orient=tk.HORIZONTAL)
        main_paned.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Left panel - Image preview and post creation
        left_panel = ttk.Frame(main_paned)
        main_paned.add(left_panel, weight=1)
        
        # Right panel - Scheduled posts and hashtags
        right_panel = ttk.Frame(main_paned)
        main_paned.add(right_panel, weight=1)
        
        self.setup_left_panel(left_panel)
        self.setup_right_panel(right_panel)
        
    def setup_left_panel(self, parent):
        """Set up the left panel with image preview and post creation."""
        # Image preview section
        image_frame = ttk.LabelFrame(parent, text="Image Preview", padding=10)
        image_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Image preview canvas
        self.image_canvas = tk.Canvas(image_frame, bg="#f0f0f0", height=300)
        self.image_canvas.pack(fill=tk.BOTH, expand=True, pady=5)
        
        # Image filename label (shown when minimized)
        self.image_filename_label = tk.Label(image_frame, text="No image selected", 
                                             font=("Arial", 10, "italic"), fg="#666")
        self.image_filename_label.pack(pady=5)
        
        # Image controls
        img_control_frame = ttk.Frame(image_frame)
        img_control_frame.pack(fill=tk.X, pady=5)
        
        self.select_image_btn = ttk.Button(img_control_frame, text="Select Image",
                                           command=self.select_image)
        self.select_image_btn.pack(side=tk.LEFT, padx=5)
        
        self.minimize_image_btn = ttk.Button(img_control_frame, text="Minimize Preview",
                                             command=self.toggle_image_preview,
                                             state=tk.DISABLED)
        self.minimize_image_btn.pack(side=tk.LEFT, padx=5)
        
        # Post creation section
        post_frame = ttk.LabelFrame(parent, text="Create Post", padding=10)
        post_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Caption input
        ttk.Label(post_frame, text="Post Caption:").pack(anchor=tk.W, pady=(0, 5))
        self.caption_text = scrolledtext.ScrolledText(post_frame, height=8, wrap=tk.WORD)
        self.caption_text.pack(fill=tk.BOTH, expand=True, pady=5)
        self.caption_text.bind("<KeyRelease>", self.auto_translate)
        
        # Translation display (automatic)
        ttk.Label(post_frame, text="Auto Translation:").pack(anchor=tk.W, pady=(5, 5))
        self.translation_text = scrolledtext.ScrolledText(post_frame, height=4, wrap=tk.WORD,
                                                          bg="#f9f9f9", state=tk.DISABLED)
        self.translation_text.pack(fill=tk.BOTH, pady=5)
        
        # Language selection
        lang_frame = ttk.Frame(post_frame)
        lang_frame.pack(fill=tk.X, pady=5)
        
        ttk.Label(lang_frame, text="Translate to:").pack(side=tk.LEFT, padx=5)
        self.target_language = tk.StringVar(value="es")
        languages = [("Spanish", "es"), ("French", "fr"), ("German", "de"), 
                    ("Italian", "it"), ("Portuguese", "pt"), ("Japanese", "ja")]
        for lang_name, lang_code in languages:
            ttk.Radiobutton(lang_frame, text=lang_name, variable=self.target_language,
                          value=lang_code).pack(side=tk.LEFT, padx=5)
        
        # Schedule controls
        schedule_frame = ttk.Frame(post_frame)
        schedule_frame.pack(fill=tk.X, pady=10)
        
        ttk.Label(schedule_frame, text="Schedule for:").pack(side=tk.LEFT, padx=5)
        
        # Date/Time inputs
        self.schedule_date = tk.StringVar(value=datetime.now().strftime("%Y-%m-%d"))
        ttk.Entry(schedule_frame, textvariable=self.schedule_date, width=12).pack(side=tk.LEFT, padx=5)
        
        self.schedule_time = tk.StringVar(value=datetime.now().strftime("%H:%M"))
        ttk.Entry(schedule_frame, textvariable=self.schedule_time, width=8).pack(side=tk.LEFT, padx=5)
        
        ttk.Button(schedule_frame, text="Schedule Post", 
                  command=self.schedule_post).pack(side=tk.LEFT, padx=20)
        
    def setup_right_panel(self, parent):
        """Set up the right panel with hashtags and scheduled posts."""
        # Viral hashtags section
        hashtag_frame = ttk.LabelFrame(parent, text="Viral Hashtags", padding=10)
        hashtag_frame.pack(fill=tk.BOTH, padx=5, pady=5)
        
        # Toggle button for hashtags/captions
        toggle_frame = ttk.Frame(hashtag_frame)
        toggle_frame.pack(fill=tk.X, pady=5)
        
        self.hashtag_mode = tk.StringVar(value="hashtags")
        ttk.Radiobutton(toggle_frame, text="Show Viral Hashtags", 
                       variable=self.hashtag_mode, value="hashtags",
                       command=self.update_viral_content).pack(side=tk.LEFT, padx=5)
        ttk.Radiobutton(toggle_frame, text="Show Viral Captions",
                       variable=self.hashtag_mode, value="captions",
                       command=self.update_viral_content).pack(side=tk.LEFT, padx=5)
        
        # Viral content display
        viral_scroll_frame = ttk.Frame(hashtag_frame)
        viral_scroll_frame.pack(fill=tk.BOTH, expand=True, pady=5)
        
        viral_scrollbar = ttk.Scrollbar(viral_scroll_frame)
        viral_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.viral_listbox = tk.Listbox(viral_scroll_frame, yscrollcommand=viral_scrollbar.set,
                                        font=("Arial", 10), height=8)
        self.viral_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        viral_scrollbar.config(command=self.viral_listbox.yview)
        self.viral_listbox.bind("<Double-Button-1>", self.insert_viral_content)
        
        self.update_viral_content()
        
        # Scheduled posts section
        posts_frame = ttk.LabelFrame(parent, text="Scheduled Posts", padding=10)
        posts_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # View toggle
        view_toggle_frame = ttk.Frame(posts_frame)
        view_toggle_frame.pack(fill=tk.X, pady=5)
        
        self.view_mode_btn = ttk.Button(view_toggle_frame, text="Toggle Expanded View",
                                        command=self.toggle_view_mode)
        self.view_mode_btn.pack(side=tk.LEFT, padx=5)
        
        ttk.Button(view_toggle_frame, text="Delete Selected",
                  command=self.delete_selected_post).pack(side=tk.LEFT, padx=5)
        
        # Posts display
        posts_scroll_frame = ttk.Frame(posts_frame)
        posts_scroll_frame.pack(fill=tk.BOTH, expand=True, pady=5)
        
        posts_scrollbar = ttk.Scrollbar(posts_scroll_frame)
        posts_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.posts_display = scrolledtext.ScrolledText(posts_scroll_frame, 
                                                       yscrollcommand=posts_scrollbar.set,
                                                       wrap=tk.WORD, font=("Arial", 10))
        self.posts_display.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        posts_scrollbar.config(command=self.posts_display.yview)
        
        # Configure tags for styling
        self.posts_display.tag_configure("header", font=("Arial", 11, "bold"), foreground="#0066cc")
        self.posts_display.tag_configure("caption", font=("Arial", 10))
        self.posts_display.tag_configure("hashtag", font=("Arial", 10), foreground="#1DA1F2")
        self.posts_display.tag_configure("image", font=("Arial", 9, "italic"), foreground="#666")
        self.posts_display.tag_configure("separator", foreground="#ccc")
        
    def select_image(self):
        """Open file dialog to select an image."""
        filetypes = (
            ("Image files", "*.jpg *.jpeg *.png *.gif *.bmp"),
            ("All files", "*.*")
        )
        filename = filedialog.askopenfilename(title="Select an image", filetypes=filetypes)
        
        if filename:
            self.current_image_path = filename
            self.display_image(filename)
            self.minimize_image_btn.config(state=tk.NORMAL)
            self.image_minimized = False
            
    def display_image(self, image_path):
        """Display the selected image on the canvas."""
        try:
            # Load and resize image
            img = Image.open(image_path)
            
            # Calculate aspect ratio and resize
            canvas_width = self.image_canvas.winfo_width()
            canvas_height = self.image_canvas.winfo_height()
            
            if canvas_width <= 1:
                canvas_width = 400
            if canvas_height <= 1:
                canvas_height = 300
                
            img_ratio = img.width / img.height
            canvas_ratio = canvas_width / canvas_height
            
            if img_ratio > canvas_ratio:
                new_width = canvas_width
                new_height = int(canvas_width / img_ratio)
            else:
                new_height = canvas_height
                new_width = int(canvas_height * img_ratio)
            
            img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
            
            # Convert to PhotoImage
            self.photo = ImageTk.PhotoImage(img)
            
            # Display on canvas
            self.image_canvas.delete("all")
            self.image_canvas.create_image(canvas_width // 2, canvas_height // 2,
                                          image=self.photo, anchor=tk.CENTER)
            
            # Update filename label
            filename = os.path.basename(image_path)
            self.image_filename_label.config(text=f"📷 {filename}")
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load image: {str(e)}")
            
    def toggle_image_preview(self):
        """Toggle between full preview and minimized (filename only) view."""
        self.image_minimized = not self.image_minimized
        
        if self.image_minimized:
            # Minimize - hide canvas, show only filename
            self.image_canvas.pack_forget()
            self.minimize_image_btn.config(text="Show Preview")
            if self.current_image_path:
                filename = os.path.basename(self.current_image_path)
                self.image_filename_label.config(text=f"📷 {filename}", font=("Arial", 12, "bold"))
        else:
            # Maximize - show canvas
            self.image_canvas.pack(fill=tk.BOTH, expand=True, pady=5)
            self.minimize_image_btn.config(text="Minimize Preview")
            if self.current_image_path:
                self.display_image(self.current_image_path)
                filename = os.path.basename(self.current_image_path)
                self.image_filename_label.config(text=f"📷 {filename}", font=("Arial", 10, "italic"))
                
    def auto_translate(self, event=None):
        """Automatically translate text as user types."""
        # Use threading to avoid UI blocking
        threading.Thread(target=self._translate_text, daemon=True).start()
        
    def _translate_text(self):
        """Translate text in background thread."""
        source_text = self.caption_text.get("1.0", tk.END).strip()
        
        if not source_text:
            self.root.after(0, lambda: self._update_translation(""))
            return
            
        try:
            if TRANSLATION_AVAILABLE:
                translator = GoogleTranslator(source='auto', target=self.target_language.get())
                translated = translator.translate(source_text)
            else:
                # Fallback simulation
                translated = f"[{self.target_language.get().upper()}] {source_text}"
            
            self.root.after(0, lambda: self._update_translation(translated))
        except Exception as e:
            self.root.after(0, lambda: self._update_translation(f"Translation error: {str(e)}"))
            
    def _update_translation(self, text):
        """Update translation text widget."""
        self.translation_text.config(state=tk.NORMAL)
        self.translation_text.delete("1.0", tk.END)
        self.translation_text.insert("1.0", text)
        self.translation_text.config(state=tk.DISABLED)
        
    def update_viral_content(self):
        """Update the viral content display based on selected mode."""
        self.viral_listbox.delete(0, tk.END)
        
        if self.hashtag_mode.get() == "hashtags":
            for hashtag in self.viral_hashtags:
                self.viral_listbox.insert(tk.END, hashtag)
        else:
            for caption in self.viral_captions:
                self.viral_listbox.insert(tk.END, caption)
                
    def insert_viral_content(self, event=None):
        """Insert selected viral content into caption."""
        selection = self.viral_listbox.curselection()
        if not selection:
            return
            
        content = self.viral_listbox.get(selection[0])
        current_text = self.caption_text.get("1.0", tk.END).strip()
        
        if current_text:
            self.caption_text.insert(tk.END, f"\n{content}")
        else:
            self.caption_text.insert("1.0", content)
            
    def schedule_post(self):
        """Schedule a new post."""
        caption = self.caption_text.get("1.0", tk.END).strip()
        
        if not caption:
            messagebox.showwarning("Warning", "Please enter a caption for the post.")
            return
            
        try:
            # Parse schedule date/time
            schedule_datetime_str = f"{self.schedule_date.get()} {self.schedule_time.get()}"
            schedule_datetime = datetime.strptime(schedule_datetime_str, "%Y-%m-%d %H:%M")
            
            # Create post object
            post = {
                "id": len(self.scheduled_posts) + 1,
                "caption": caption,
                "translation": self.translation_text.get("1.0", tk.END).strip(),
                "image_path": self.current_image_path,
                "schedule_datetime": schedule_datetime.isoformat(),
                "created_at": datetime.now().isoformat()
            }
            
            self.scheduled_posts.append(post)
            self.save_scheduled_posts()
            self.refresh_posts_display()
            
            # Clear inputs
            self.caption_text.delete("1.0", tk.END)
            self.current_image_path = None
            self.image_canvas.delete("all")
            self.image_filename_label.config(text="No image selected")
            self.minimize_image_btn.config(state=tk.DISABLED)
            
            messagebox.showinfo("Success", "Post scheduled successfully!")
            
        except ValueError as e:
            messagebox.showerror("Error", f"Invalid date/time format: {str(e)}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to schedule post: {str(e)}")
            
    def toggle_view_mode(self):
        """Toggle between compact and expanded view."""
        self.expanded_view = not self.expanded_view
        self.refresh_posts_display()
        
    def refresh_posts_display(self):
        """Refresh the scheduled posts display."""
        self.posts_display.config(state=tk.NORMAL)
        self.posts_display.delete("1.0", tk.END)
        
        if not self.scheduled_posts:
            self.posts_display.insert("1.0", "No scheduled posts yet.\n\n")
            self.posts_display.insert(tk.END, "Create your first post using the form on the left!")
            self.posts_display.config(state=tk.DISABLED)
            return
            
        # Sort posts by schedule datetime
        sorted_posts = sorted(self.scheduled_posts, 
                            key=lambda p: p.get("schedule_datetime", ""))
        
        for i, post in enumerate(sorted_posts):
            schedule_dt = datetime.fromisoformat(post["schedule_datetime"])
            
            if self.expanded_view:
                # Expanded view with full details
                self.posts_display.insert(tk.END, f"Post #{post['id']}\n", "header")
                self.posts_display.insert(tk.END, f"Scheduled: {schedule_dt.strftime('%Y-%m-%d %H:%M')}\n\n")
                
                self.posts_display.insert(tk.END, "Caption:\n", "header")
                self.posts_display.insert(tk.END, f"{post['caption']}\n\n", "caption")
                
                if post.get("translation"):
                    self.posts_display.insert(tk.END, "Translation:\n", "header")
                    self.posts_display.insert(tk.END, f"{post['translation']}\n\n", "caption")
                
                # Extract and display hashtags
                caption_text = post['caption']
                hashtags = [word for word in caption_text.split() if word.startswith('#')]
                if hashtags:
                    self.posts_display.insert(tk.END, "Hashtags: ", "header")
                    self.posts_display.insert(tk.END, " ".join(hashtags) + "\n\n", "hashtag")
                
                # Display image if available
                if post.get("image_path") and os.path.exists(post["image_path"]):
                    self.posts_display.insert(tk.END, "Image: ", "header")
                    self.posts_display.insert(tk.END, f"{os.path.basename(post['image_path'])}\n", "image")
                    
                    # Try to embed image preview
                    try:
                        img = Image.open(post["image_path"])
                        img.thumbnail((300, 300), Image.Resampling.LANCZOS)
                        photo = ImageTk.PhotoImage(img)
                        
                        # Store reference to prevent garbage collection
                        if not hasattr(self, 'post_images'):
                            self.post_images = []
                        self.post_images.append(photo)
                        
                        self.posts_display.image_create(tk.END, image=photo)
                        self.posts_display.insert(tk.END, "\n")
                    except:
                        pass
                        
                self.posts_display.insert(tk.END, "\n" + "="*60 + "\n\n", "separator")
            else:
                # Compact view
                self.posts_display.insert(tk.END, f"#{post['id']} ", "header")
                self.posts_display.insert(tk.END, f"{schedule_dt.strftime('%m/%d %H:%M')} - ")
                caption_preview = post['caption'][:50] + "..." if len(post['caption']) > 50 else post['caption']
                self.posts_display.insert(tk.END, caption_preview)
                if post.get("image_path"):
                    self.posts_display.insert(tk.END, " 📷", "image")
                self.posts_display.insert(tk.END, "\n")
        
        self.posts_display.config(state=tk.DISABLED)
        
    def delete_selected_post(self):
        """Delete the selected post."""
        # Get selected text range
        try:
            sel_start = self.posts_display.index(tk.SEL_FIRST)
            # Extract post ID from selection
            selected_text = self.posts_display.get(sel_start, sel_start + " lineend")
            
            # Parse post ID
            if selected_text.startswith("#"):
                post_id = int(selected_text.split()[0][1:])
                
                # Find and remove post
                self.scheduled_posts = [p for p in self.scheduled_posts if p["id"] != post_id]
                self.save_scheduled_posts()
                self.refresh_posts_display()
                messagebox.showinfo("Success", f"Post #{post_id} deleted.")
            else:
                messagebox.showwarning("Warning", "Please select a post to delete.")
        except tk.TclError:
            messagebox.showwarning("Warning", "Please select a post to delete.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to delete post: {str(e)}")
            
    def save_scheduled_posts(self):
        """Save scheduled posts to JSON file."""
        data_dir = Path.home() / ".logsn"
        data_dir.mkdir(exist_ok=True)
        
        data_file = data_dir / "scheduled_posts.json"
        
        try:
            with open(data_file, "w") as f:
                json.dump(self.scheduled_posts, f, indent=2)
        except Exception as e:
            print(f"Failed to save posts: {e}")
            
    def load_scheduled_posts(self):
        """Load scheduled posts from JSON file."""
        data_dir = Path.home() / ".logsn"
        data_file = data_dir / "scheduled_posts.json"
        
        if data_file.exists():
            try:
                with open(data_file, "r") as f:
                    self.scheduled_posts = json.load(f)
                self.refresh_posts_display()
            except Exception as e:
                print(f"Failed to load posts: {e}")


def main():
    """Main entry point for the application."""
    root = tk.Tk()
    app = SocialMediaScheduler(root)
    root.mainloop()


if __name__ == "__main__":
    main()
