import re
import os

files = ['ce-message.html', 'history.html', 'organogram.html', 'about.html', 'executives.html', 'careers.html', 'complaints.html', 'media.html', 'tenders.html']

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()
    header_block = re.search(r'(<!-- Top Utility Bar.*?</header>)', text, re.DOTALL).group(1)
    footer_block = re.search(r'(<footer class="footer">.*?</footer>)', text, re.DOTALL).group(1)

for fname in files:
    if not os.path.exists(fname): 
        print(f"Skipping {fname}, does not exist")
        continue
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract the main content part between header and footer
    # Using regex to wipe out everything before the "hero" section or `<main>` section
    match_start = re.search(r'(<section class=".*?hero")', content)
    if not match_start:
        match_start = re.search(r'(<main>)', content)
        
    if not match_start:
        print(f"Skipping {fname}, no main body start found")
        continue

    # Find where footer or script tags start to signify end of main part
    match_end = re.search(r'(<footer class="footer">)', content)
    if not match_end:
        match_end = re.search(r'(<script src="script.js">)', content)

    if not match_end:
        print(f"Skipping {fname}, no footer / script end found")
        continue
        
    head_part = content[:match_start.start()]
    # remove old headers from head part
    head_part = re.sub(r'<!-- Top Utility Bar.*', '', head_part, flags=re.DOTALL)
    head_part = re.sub(r'<div class="top-banner.*', '', head_part, flags=re.DOTALL)
    head_part = re.sub(r'<header class="header".*', '', head_part, flags=re.DOTALL)

    # preserve up to <body> tag
    body_match = re.search(r'(<body[^>]*>)', content)
    if body_match:
        # just take up to body tag from original content
        head_part = content[:body_match.end()]

    
    main_part = content[match_start.start():match_end.start()]
    
    # clean main part of any rogue top-banners
    main_part = re.sub(r'<!-- Top Utility Bar.*?(?:</header>|Search BOCRA</span>\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>)', '', main_part, flags=re.DOTALL)
    main_part = re.sub(r'<div class="top-banner.*?(?:</header>|Search BOCRA</span>\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>)', '', main_part, flags=re.DOTALL)
    main_part = re.sub(r'<div class="top-banner.*?(?:</header>|Search BOCRA</span>\s*</div>\s*</div>\s*</div>\s*</div>)', '', main_part, flags=re.DOTALL)

    tail_part = content[match_end.start():]
    # Keep only scripts and end tags, drop old footers
    tail_part = re.sub(r'<footer class="footer">.*?</footer>', '', tail_part, flags=re.DOTALL)

    new_content = head_part + "\n" + header_block + "\n" + main_part + "\n" + footer_block + "\n" + tail_part
    with open(fname, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Fixed {fname}")
