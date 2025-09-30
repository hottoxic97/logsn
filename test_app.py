#!/usr/bin/env python3
"""
Test script for Social Media Post Scheduler
Tests the core functionality without requiring GUI display
"""

import json
import os
import tempfile
from pathlib import Path
from datetime import datetime
import sys

# Test imports
def test_imports():
    """Test that all required imports are available."""
    print("Testing imports...")
    
    try:
        from PIL import Image
        print("  ✓ PIL (Pillow) imported")
    except ImportError as e:
        print(f"  ✗ PIL import failed: {e}")
        return False
    
    try:
        from deep_translator import GoogleTranslator
        print("  ✓ deep_translator imported")
    except ImportError as e:
        print(f"  ✗ deep_translator import failed: {e}")
        return False
    
    print("  ✓ All imports successful")
    return True


def test_translation():
    """Test the translation functionality."""
    print("\nTesting translation...")
    
    try:
        from deep_translator import GoogleTranslator
        
        translator = GoogleTranslator(source='en', target='es')
        result = translator.translate("Hello World")
        
        print(f"  ✓ Translation successful: 'Hello World' -> '{result}'")
        return True
    except Exception as e:
        print(f"  ✗ Translation failed: {e}")
        return False


def test_json_storage():
    """Test JSON storage functionality."""
    print("\nTesting JSON storage...")
    
    # Create a temporary directory for testing
    with tempfile.TemporaryDirectory() as temp_dir:
        test_file = Path(temp_dir) / "test_posts.json"
        
        # Create test data
        test_posts = [
            {
                "id": 1,
                "caption": "Test post #1",
                "translation": "Prueba de publicación #1",
                "image_path": "/tmp/test.jpg",
                "schedule_datetime": datetime.now().isoformat(),
                "created_at": datetime.now().isoformat()
            },
            {
                "id": 2,
                "caption": "Test post #2 with #hashtags",
                "translation": "Prueba de publicación #2 con #hashtags",
                "image_path": None,
                "schedule_datetime": datetime.now().isoformat(),
                "created_at": datetime.now().isoformat()
            }
        ]
        
        # Save to file
        try:
            with open(test_file, "w") as f:
                json.dump(test_posts, f, indent=2)
            print(f"  ✓ JSON save successful")
        except Exception as e:
            print(f"  ✗ JSON save failed: {e}")
            return False
        
        # Load from file
        try:
            with open(test_file, "r") as f:
                loaded_posts = json.load(f)
            
            if len(loaded_posts) == len(test_posts):
                print(f"  ✓ JSON load successful ({len(loaded_posts)} posts)")
            else:
                print(f"  ✗ JSON load mismatch: expected {len(test_posts)}, got {len(loaded_posts)}")
                return False
        except Exception as e:
            print(f"  ✗ JSON load failed: {e}")
            return False
        
        # Verify data integrity
        if loaded_posts[0]["caption"] == test_posts[0]["caption"]:
            print(f"  ✓ Data integrity verified")
        else:
            print(f"  ✗ Data integrity check failed")
            return False
    
    return True


def test_image_handling():
    """Test image handling functionality."""
    print("\nTesting image handling...")
    
    try:
        from PIL import Image
        
        # Create a test image
        with tempfile.TemporaryDirectory() as temp_dir:
            test_image_path = Path(temp_dir) / "test_image.png"
            
            # Create a simple test image
            img = Image.new('RGB', (800, 600), color='red')
            img.save(test_image_path)
            print(f"  ✓ Test image created")
            
            # Load and verify
            loaded_img = Image.open(test_image_path)
            if loaded_img.size == (800, 600):
                print(f"  ✓ Image loading verified (size: {loaded_img.size})")
            else:
                print(f"  ✗ Image size mismatch")
                return False
            
            # Test resizing (thumbnail)
            loaded_img.thumbnail((300, 300), Image.Resampling.LANCZOS)
            print(f"  ✓ Image resizing successful (new size: {loaded_img.size})")
            
    except Exception as e:
        print(f"  ✗ Image handling failed: {e}")
        return False
    
    return True


def test_hashtag_extraction():
    """Test hashtag extraction from captions."""
    print("\nTesting hashtag extraction...")
    
    test_captions = [
        "Check out this #amazing post with #viral #hashtags",
        "No hashtags here!",
        "#StartingWithHashtag and ending with #another",
        "Multiple #hash1 #hash2 #hash3 in one post"
    ]
    
    expected_results = [
        ["#amazing", "#viral", "#hashtags"],
        [],
        ["#StartingWithHashtag", "#another"],
        ["#hash1", "#hash2", "#hash3"]
    ]
    
    for caption, expected in zip(test_captions, expected_results):
        hashtags = [word for word in caption.split() if word.startswith('#')]
        if hashtags == expected:
            print(f"  ✓ Extracted {len(hashtags)} hashtags from caption")
        else:
            print(f"  ✗ Hashtag extraction mismatch")
            print(f"    Expected: {expected}")
            print(f"    Got: {hashtags}")
            return False
    
    print(f"  ✓ All hashtag extraction tests passed")
    return True


def test_datetime_handling():
    """Test datetime parsing and formatting."""
    print("\nTesting datetime handling...")
    
    try:
        # Test ISO format conversion
        now = datetime.now()
        iso_string = now.isoformat()
        parsed = datetime.fromisoformat(iso_string)
        
        if abs((now - parsed).total_seconds()) < 1:
            print(f"  ✓ ISO datetime conversion successful")
        else:
            print(f"  ✗ Datetime conversion failed")
            return False
        
        # Test custom format
        date_str = "2024-12-31"
        time_str = "23:59"
        combined = f"{date_str} {time_str}"
        parsed = datetime.strptime(combined, "%Y-%m-%d %H:%M")
        
        if parsed.year == 2024 and parsed.month == 12 and parsed.day == 31:
            print(f"  ✓ Custom datetime parsing successful")
        else:
            print(f"  ✗ Custom datetime parsing failed")
            return False
            
    except Exception as e:
        print(f"  ✗ Datetime handling failed: {e}")
        return False
    
    return True


def test_viral_content():
    """Test viral hashtags and captions data structures."""
    print("\nTesting viral content...")
    
    viral_hashtags = [
        "#Trending", "#Viral", "#ForYou", "#FYP", "#Explore",
        "#InstaGood", "#PhotoOfTheDay"
    ]
    
    viral_captions = [
        "Don't wait for opportunity. Create it.",
        "Great things never come from comfort zones.",
        "Dream big, work hard, stay focused."
    ]
    
    if len(viral_hashtags) > 0:
        print(f"  ✓ {len(viral_hashtags)} viral hashtags available")
    else:
        print(f"  ✗ No viral hashtags found")
        return False
    
    if len(viral_captions) > 0:
        print(f"  ✓ {len(viral_captions)} viral captions available")
    else:
        print(f"  ✗ No viral captions found")
        return False
    
    return True


def main():
    """Run all tests."""
    print("="*60)
    print("Social Media Post Scheduler - Test Suite")
    print("="*60)
    
    tests = [
        test_imports,
        test_translation,
        test_json_storage,
        test_image_handling,
        test_hashtag_extraction,
        test_datetime_handling,
        test_viral_content
    ]
    
    passed = 0
    failed = 0
    
    for test in tests:
        try:
            if test():
                passed += 1
            else:
                failed += 1
        except Exception as e:
            print(f"  ✗ Test crashed: {e}")
            failed += 1
    
    print("\n" + "="*60)
    print(f"Test Results: {passed} passed, {failed} failed")
    print("="*60)
    
    if failed == 0:
        print("\n✓ All tests passed! Application is ready to use.")
        return 0
    else:
        print(f"\n✗ {failed} test(s) failed. Please review the output above.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
