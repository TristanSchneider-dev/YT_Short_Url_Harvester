# YT_Short_Url_Harvester
The given scripts are written in Python and serve different purposes:

1. **scrape_urls.py**:
   - This script uses Selenium to scrape YouTube URLs from YouTube Shorts.
   - It opens the Firefox browser using the GeckoDriver.
   - The script scrolls the webpage and saves the URLs of the scrolled pages.
   - The URLs are stored in a text file ("yt_short_urls.txt").
   - The script runs continuously until the "Ctrl + C" key combination is pressed.

2. **manage_urls.py**:
   - This script reads the URLs stored in the "yt_short_urls.txt" file.
   - It reads the URLs from the file and stores them in a list.
   - It extracts the part of the URL that comes after "https://www.youtube.com/shorts/" and keeps only that part.
   - The script outputs the unique characters used in the URLs in alphabetical order.
   - It also prints the number of unique characters.

3. **generate_urls.py**:
   - This script generates all possible combinations of YouTube Shorts URLs.
   - It uses the "itertools" module and generates combinations of the given character list.
   - The combinations are assembled into complete YouTube Shorts URLs ("https://www.youtube.com/shorts/{combination}").
   - The generated combinations are written to the "possible_urls.txt" file.

These scripts work together to collect, manage, and generate YouTube Shorts URLs. The scraping script collects the URLs, the management script processes them, and the generation script creates new URLs.
