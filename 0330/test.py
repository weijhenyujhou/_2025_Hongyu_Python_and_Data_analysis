import beautifulsoup4
try:
    from bs4 import BeautifulSoup
except ImportError:
    print("BeautifulSoup4 is not installed. Installing...")
    import subprocess
    import sys
    subprocess.check_call([sys.executable, "-m", "pip",
                          "install", "beautifulsoup4"])
    from bs4 import BeautifulSoup
    print("BeautifulSoup4 installed successfully!")
