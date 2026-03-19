import os
import glob
import re

html_files = glob.glob('*.html')
social_replacement = """<div class="social-links">
            <a href="https://www.facebook.com/BOCRABW/" target="_blank" aria-label="Facebook"><i class="fa-brands fa-facebook-f"></i></a>
            <a href="https://twitter.com/bocra_bw" target="_blank" aria-label="Twitter"><i class="fa-brands fa-x-twitter"></i></a>
            <a href="https://www.youtube.com/@bocra_bw" target="_blank" aria-label="YouTube"><i class="fa-brands fa-youtube"></i></a>
            <a href="https://bw.linkedin.com/company/botswana-communications-regulatory-authority" target="_blank" aria-label="LinkedIn"><i class="fa-brands fa-linkedin-in"></i></a>
          </div>"""

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = re.sub(
        r'<div class="social-links">\s*<a.*?</div\s*>',
        social_replacement,
        content,
        flags=re.DOTALL
    )
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated social links in {filepath}")
