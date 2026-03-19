import os
import re

# List of files to update
files = [
    "index.html", "about.html", "profile.html", "ce-message.html", "history.html",
    "organogram.html", "executives.html", "careers.html", "legislation.html",
    "telecommunications.html", "broadcasting.html", "postal.html", "internet.html",
    "draft-docs.html", "licensing-framework.html", "itu-workshop.html",
    "complaints.html", "media.html", "tenders.html", "projects.html",
    "licensing.html", "consumer-protection.html", "contact.html",
    "news-view.html", "documents-view.html", "equipment-search.html", "license-portal.html"
]

base_path = r"c:\Users\fbda22-013\OneDrive - Botswana Accountancy College\Desktop\BOCRA 2"

# Define the Official Branding Blocks (from index.html)
# Using local logo paths to avoid hotlinking/CSP/CORS issues in browser
NEW_HEAD_FONTS = """  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">"""

NEW_TOP_BAR = """  <!-- Top Utility Bar (Official BOCRA Style) -->
  <div class="top-banner" id="top-banner">
    <div class="container top-banner-content">
      <a href="https://registration.bocra.org.bw/" target="_blank" class="top-bar-link"><i class="fa-solid fa-laptop"></i> BOCRA Portal</a>
      <a href="#" class="top-bar-link"><i class="fa-solid fa-chart-line"></i> QOS Monitoring</a>
      <a href="licensing.html" class="top-bar-link"><i class="fa-solid fa-file-signature"></i> Licensing</a>
      <div class="search-box">
        <i class="fa-solid fa-magnifying-glass" style="color: #fff; font-size: 0.8rem;"></i>
        <span style="color: #fff; margin-left: 8px; font-size: 0.8rem;">Search BOCRA</span>
      </div>
    </div>
  </div>"""

NEW_HEADER = """  <!-- Header -->
  <header class="header" id="header">
    <div class="container header-container">
      <a href="index.html" class="logo">
        <img src="Bocra_final-logo-cropped.png" alt="BOCRA Logo" />
      </a>
      <div class="nav-wrapper-outer">
        <div class="nav-wrapper">
          <nav class="main-nav" id="main-nav">
            <ul class="nav-list">
              <li class="has-dropdown">
                <a href="#">About <i class="fa-solid fa-chevron-down"></i></a>
                <ul class="dropdown">
                  <li><a href="profile.html">Profile</a></li>
                  <li><a href="ce-message.html">A Word From The Chief Executive</a></li>
                  <li><a href="history.html">History Of Communication Regulation</a></li>
                  <li><a href="organogram.html">Organogram</a></li>
                  <li><a href="about.html#board">Board of Directors</a></li>
                  <li><a href="executives.html">Executive Management</a></li>
                  <li><a href="careers.html">Careers</a></li>
                </ul>
              </li>
              <li class="has-dropdown">
                <a href="#">Mandate <i class="fa-solid fa-chevron-down"></i></a>
                <ul class="dropdown">
                  <li><a href="legislation.html">Legislation</a></li>
                  <li><a href="telecommunications.html">Telecommunications</a></li>
                  <li><a href="broadcasting.html">Broadcasting</a></li>
                  <li><a href="postal.html">Postal</a></li>
                  <li><a href="internet.html">Internet</a></li>
                </ul>
              </li>
              <li id="nav-projects"><a href="projects.html">Projects</a></li>
              <li class="has-dropdown">
                <a href="#">Documents <i class="fa-solid fa-chevron-down"></i></a>
                <ul class="dropdown">
                  <li><a href="draft-docs.html">Draft Documents And Legislation</a></li>
                  <li><a href="https://www.bocra.org.bw/sites/default/files/2024-03/ICT%20Licensing%20Framework.pdf">ICT Licencing Framework</a></li>
                  <li><a href="itu-workshop.html">ITU Capacity Building Workshop</a></li>
                </ul>
              </li>
              <li id="nav-complaints"><a href="complaints.html">Complaints</a></li>
              <li id="nav-media"><a href="media.html">Media</a></li>
              <li id="nav-tenders"><a href="tenders.html">Tenders</a></li>
              <li><a href="https://registration.bocra.org.bw/" class="nav-highlight" target="_blank">ASMS-WebCP</a></li>
            </ul>
          </nav>
        </div>
        <button class="mobile-menu-btn" id="mobile-menu-btn">
          <i class="fa-solid fa-bars"></i>
        </button>
      </div>
    </div>
  </header>"""

NEW_FOOTER = """  <!-- Footer -->
  <footer class="footer">
    <div class="container">
      <div class="footer-top">
        <div class="footer-col brand-col">
          <img src="Bocra_final-logo-cropped.png" alt="BOCRA Logo" class="footer-logo">
          <p><strong>Botswana Communications Regulatory Authority</strong></p>
          <p><i class="fa-solid fa-location-dot"></i> Plot 50671 Independence Avenue, Gaborone</p>
          <p><i class="fa-solid fa-phone"></i> +267 395 7755</p>
          <p><i class="fa-solid fa-envelope"></i> <a href="mailto:info@bocra.org.bw">info@bocra.org.bw</a></p>
        </div>
        <div class="footer-col link-col">
          <h4>Explore</h4>
          <ul style="list-style: none;">
            <li><a href="about.html">About BOCRA</a></li>
            <li><a href="licensing.html">Licensing</a></li>
            <li><a href="media.html">Media Center</a></li>
            <li><a href="tenders.html">Tenders</a></li>
          </ul>
        </div>
        <div class="footer-col link-col">
          <h4>Resources</h4>
          <ul style="list-style: none;">
            <li><a href="#">Tariffs</a></li>
            <li><a href="#">FAQs</a></li>
            <li><a href="#">Important Links</a></li>
            <li><a href="#">Privacy Notice</a></li>
          </ul>
        </div>
        <div class="footer-col brand-col">
          <h4>Staff Mail</h4>
          <p><a href="#"><i class="fa-solid fa-envelope"></i> BOCRA Staff Mail</a></p>
          <div class="social-links">
            <a href="#"><i class="fa-brands fa-facebook-f"></i></a>
            <a href="#"><i class="fa-brands fa-twitter"></i></a>
            <a href="#"><i class="fa-brands fa-youtube"></i></a>
            <a href="#"><i class="fa-brands fa-linkedin-in"></i></a>
          </div>
        </div>
      </div>
    </div>
    <div class="footer-bottom">
      <div class="container">
        <p>&copy; <span id="year">2024</span> Botswana Communications Regulatory Authority. All Rights Reserved.</p>
      </div>
    </div>
  </footer>"""

def update_file(filename):
    filepath = os.path.join(base_path, filename)
    if not os.path.exists(filepath):
        print(f"Skipping {filename}, not found.")
        return
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Update Fonts/Styles in Head
    if "Montserrat" not in content:
        if "fonts.googleapis.com" not in content:
            content = re.sub(r'<head>.*?(<link rel="stylesheet" href="style.css" />)', r'<head>\n' + NEW_HEAD_FONTS + r'\n  \1', content, flags=re.DOTALL)
        else:
            content = re.sub(r'(<link rel="preconnect" href="https://fonts.googleapis.com">.*?)(<link rel="stylesheet" href="style.css" />)', NEW_HEAD_FONTS + r'\n  \2', content, flags=re.DOTALL)

    # 2. Update Top Banner
    content = re.sub(r'<!-- Top Utility Bar.*?</div>\s*</div>', NEW_TOP_BAR, content, flags=re.DOTALL)
    content = re.sub(r'<div class="top-banner".*?</div>\s*</div>', NEW_TOP_BAR, content, flags=re.DOTALL)

    # 3. Update Header
    content = re.sub(r'<!-- Header -->.*?<header.*?</header>', NEW_HEADER, content, flags=re.DOTALL)

    # 4. Update Footer
    content = re.sub(r'<!-- Footer -->.*?<footer.*?</footer>', NEW_FOOTER, content, flags=re.DOTALL)

    # Set active class for the current page
    if "complaints.html" in filename:
        content = content.replace('<li id="nav-complaints"><a href="complaints.html">', '<li id="nav-complaints"><a href="complaints.html" class="active">')
    elif "media.html" in filename:
        content = content.replace('<li id="nav-media"><a href="media.html">', '<li id="nav-media"><a href="media.html" class="active">')
    elif "tenders.html" in filename:
        content = content.replace('<li id="nav-tenders"><a href="tenders.html">', '<li id="nav-tenders"><a href="tenders.html" class="active">')
    elif "projects.html" in filename:
        content = content.replace('<li id="nav-projects"><a href="projects.html">', '<li id="nav-projects"><a href="projects.html" class="active">')

    # Remove extra closing tags if any were left over from previous failed edits
    # Specifically looking for the pattern that caused double divs
    content = content.replace('</div>\n    </div>\n  </div>\n  </div>', '</div>\n    </div>\n  </div>')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Successfully refined {filename}")

for f in files:
    update_file(f)

print("Site-wide refinement complete!")
