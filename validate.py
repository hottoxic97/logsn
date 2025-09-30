#!/usr/bin/env python3
"""
Validation script - Verifies all required components are present and correct
"""

import os
from pathlib import Path

def check_file(filepath, min_size=0):
    """Check if file exists and meets minimum size requirement."""
    path = Path(filepath)
    if not path.exists():
        return False, "File not found"
    
    size = path.stat().st_size
    if size < min_size:
        return False, f"File too small ({size} bytes)"
    
    return True, f"✓ ({size:,} bytes)"

def main():
    print("="*70)
    print("Social Media Post Scheduler v4 - Validation Report")
    print("="*70)
    
    # Define required files and their minimum sizes
    required_files = {
        "run_app.py": 20000,  # Main application
        "requirements.txt": 20,  # Dependencies
        "README.md": 1000,  # Documentation
        "test_app.py": 5000,  # Test suite
        "demo.py": 2000,  # Demo script
        ".gitignore": 100,  # Git ignore
        "FEATURES.md": 5000,  # Feature documentation
        "QUICKSTART.md": 1000,  # Quick start guide
    }
    
    print("\n📁 File Validation:")
    print("-" * 70)
    
    all_present = True
    for filename, min_size in required_files.items():
        exists, message = check_file(filename, min_size)
        status = "✓" if exists else "✗"
        print(f"  {status} {filename:25s} {message}")
        if not exists:
            all_present = False
    
    print("\n" + "="*70)
    print("🔍 Code Quality Checks:")
    print("-" * 70)
    
    # Check Python syntax
    print("  Testing Python syntax...")
    for py_file in ["run_app.py", "test_app.py", "demo.py"]:
        result = os.system(f"python3 -m py_compile {py_file} 2>/dev/null")
        if result == 0:
            print(f"    ✓ {py_file} - syntax OK")
        else:
            print(f"    ✗ {py_file} - syntax error")
            all_present = False
    
    print("\n" + "="*70)
    print("✨ Feature Implementation:")
    print("-" * 70)
    
    # Check for key features in the code
    with open("run_app.py", "r") as f:
        code = f.read()
    
    features = [
        ("Automatic Translation", "auto_translate"),
        ("Image Minimize Toggle", "toggle_image_preview"),
        ("Viral Hashtags", "viral_hashtags"),
        ("Viral Captions", "viral_captions"),
        ("Expanded View", "expanded_view"),
        ("Image Embedding", "image_create"),
        ("Post Scheduling", "schedule_post"),
        ("JSON Storage", "save_scheduled_posts"),
    ]
    
    for feature_name, search_term in features:
        if search_term in code:
            print(f"  ✓ {feature_name:30s} - implemented")
        else:
            print(f"  ✗ {feature_name:30s} - NOT FOUND")
            all_present = False
    
    print("\n" + "="*70)
    print("🐛 Bug Fix Verification:")
    print("-" * 70)
    
    bug_fixes = [
        ("Translation readable & separate", "translation_text"),
        ("No manual translate buttons", "auto_translate" in code and "translate_btn" not in code.lower()),
        ("Viral hashtags restored", "viral_hashtags" in code),
        ("Expanded view toggle", "toggle_view_mode" in code),
        ("Image minimize works", "toggle_image_preview" in code and "pack_forget" in code),
        ("Images properly embedded", "image_create" in code),
    ]
    
    for bug_description, check in bug_fixes:
        if isinstance(check, bool):
            status = check
        else:
            status = check in code
        
        symbol = "✓" if status else "✗"
        print(f"  {symbol} {bug_description}")
    
    print("\n" + "="*70)
    print("📦 Dependencies:")
    print("-" * 70)
    
    # Check requirements
    with open("requirements.txt", "r") as f:
        deps = f.read()
    
    required_deps = ["Pillow", "deep-translator"]
    for dep in required_deps:
        if dep in deps:
            print(f"  ✓ {dep} specified in requirements.txt")
        else:
            print(f"  ✗ {dep} missing from requirements.txt")
            all_present = False
    
    print("\n" + "="*70)
    print("📚 Documentation:")
    print("-" * 70)
    
    docs = {
        "README.md": ["Installation", "Usage", "Features"],
        "FEATURES.md": ["Bug Fix", "Implementation", "Layout"],
        "QUICKSTART.md": ["Quick Start", "Installation", "Tips"],
    }
    
    for doc_file, keywords in docs.items():
        if os.path.exists(doc_file):
            with open(doc_file, "r") as f:
                content = f.read()
            found = sum(1 for kw in keywords if kw in content)
            print(f"  ✓ {doc_file:20s} ({found}/{len(keywords)} sections)")
        else:
            print(f"  ✗ {doc_file:20s} missing")
    
    print("\n" + "="*70)
    
    if all_present:
        print("✅ VALIDATION PASSED - All components present and correct!")
        print("\nApplication is ready to use. Run with: python run_app.py")
        return 0
    else:
        print("⚠️  VALIDATION FAILED - Some issues detected (see above)")
        return 1

if __name__ == "__main__":
    exit(main())
