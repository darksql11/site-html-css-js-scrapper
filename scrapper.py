import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin
from concurrent.futures import ThreadPoolExecutor

start_url = "https://nadoclient.net" # UR SITE (EXAMPLE)
visited = set()
queue = {start_url}

html_folder = "nadoclient_html" # EXAMPLE
js_folder = "nadoclient_js" # EXAMPLE
css_folder = "nadoclient_css" # EXAMPLE

for folder in [html_folder, js_folder, css_folder]:
    if not os.path.exists(folder):
        os.makedirs(folder)

html_count = 0
js_count = 0
css_count = 0

def update_counters(html=0, js=0, css=0):
    global html_count, js_count, css_count
    html_count += html
    js_count += js
    css_count += css

def download_and_parse(url):
    if url in visited:
        return set()
    
    headers = {'User-Agent': 'Mozilla/5.0'}
    try:
        response = requests.get(url, headers=headers, timeout=5)
        visited.add(url)
        
        if response.status_code == 200:
            html_content = response.text
            html_filename = url.replace("https://", "").replace("http://", "").replace("/", "_") + ".html"
            html_path = os.path.join(html_folder, html_filename)
            
            with open(html_path, "w", encoding="utf-8") as file:
                file.write(html_content)
            print(f"HTML: {html_filename} downloaded!")
            
            soup = BeautifulSoup(html_content, "html.parser")
            new_urls = set()
            
            for script in soup.find_all("script", src=True):
                js_url = urljoin(url, script["src"])
                if js_url not in visited:
                    try:
                        js_response = requests.get(js_url, headers=headers, timeout=5)
                        visited.add(js_url)
                        if js_response.status_code == 200:
                            js_content = js_response.text
                            js_filename = js_url.split("/")[-1].split("?")[0]
                            js_path = os.path.join(js_folder, js_filename)
                            with open(js_path, "w", encoding="utf-8") as file:
                                file.write(js_content)
                            print(f"JS: {js_filename} downloaded!")
                            update_counters(js=1)
                    except:
                        print(f"JS {js_url} couldnt be downloaded...")
            
            for link in soup.find_all("link", rel="stylesheet", href=True):
                css_url = urljoin(url, link["href"])
                if css_url not in visited:
                    try:
                        css_response = requests.get(css_url, headers=headers, timeout=5)
                        visited.add(css_url)
                        if css_response.status_code == 200:
                            css_content = css_response.text
                            css_filename = css_url.split("/")[-1].split("?")[0]
                            css_path = os.path.join(css_folder, css_filename)
                            with open(css_path, "w", encoding="utf-8") as file:
                                file.write(css_content)
                            print(f"CSS: {css_filename} downloaded!")
                            update_counters(css=1)
                    except:
                        print(f"CSS {css_url} couldnt be downloaded...")
            
            for link in soup.find_all("a", href=True):
                full_url = urljoin(url, link["href"])
                if full_url.startswith(start_url) and full_url not in visited:
                    new_urls.add(full_url)
            
            update_counters(html=1)
            return new_urls
        
        else:
            print(f"{url} couldnt be downloaded. Status code: {response.status_code}")
            return set()
    
    except:
        print(f"Error downloading {url}")
        return set()

with ThreadPoolExecutor(max_workers=10) as executor:
    while queue:
        futures = {executor.submit(download_and_parse, url): url for url in queue}
        queue = set()
        
        for future in futures:
            try:
                new_urls = future.result()
                queue.update(new_urls)
            except:
                print("An error occurred")

print(f"Total {html_count} HTML, {js_count} JS, {css_count} CSS files downloaded!")
print(f"Files are in: {html_folder}, {js_folder}, {css_folder}")
