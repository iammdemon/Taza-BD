import os
import re

dir_path = r'c:\Users\seomd\Downloads\PrettyFresh\src'
for root, _, files in os.walk(dir_path):
    for f in files:
        if f.endswith('.tsx') or f.endswith('.ts'):
            path = os.path.join(root, f)
            with open(path, 'r', encoding='utf-8') as file:
                content = file.read()
            
            new_content = re.sub(
                r'<span className="logo-icon"[^>]*>.*?</span>\s*<span className="logo-text"[^>]*>.*?</span>', 
                r'<img src="/logo.png" alt="TAZA Logo" height="32" style={{ maxHeight: "32px", width: "auto" }} />', 
                content, 
                flags=re.DOTALL
            )
            
            if content != new_content:
                with open(path, 'w', encoding='utf-8') as file:
                    file.write(new_content)
                print(f"Updated {path}")
