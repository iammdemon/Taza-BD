import os
import re

dir_path = r'c:\Users\seomd\Downloads\PrettyFresh\src'
for root, _, files in os.walk(dir_path):
    for f in files:
        if f.endswith('.tsx') or f.endswith('.ts'):
            path = os.path.join(root, f)
            with open(path, 'r', encoding='utf-8') as file:
                content = file.read()
            
            # Replace the img tag followed by </span> with just the img tag
            new_content = re.sub(
                r'(<img src="/logo\.png"[^>]*\s*/>)\s*</span>', 
                r'\1', 
                content
            )
            
            if content != new_content:
                with open(path, 'w', encoding='utf-8') as file:
                    file.write(new_content)
                print(f"Fixed {path}")
