import requests
import yaml
from datetime import datetime

def load_urls(config_path="monitor/config.yaml"):
    """ This function loads the urls from the yaml file """
    
    with open(config_path, "r") as f:
        data = yaml.safe_load(f)
    return data.get("urls", [])

def check_url(url):
    try:
        response = requests.get(url, timeout=5)
        return response.status_code == 200
    except requests.RequestException:
        return False

def run_checks():
    urls = load_urls()
    for url in urls:
        if not check_url(url):
            log_downtime(url)

def log_downtime(url):
    with open("logs/down.log", "a") as f:
        timestamp = datetime.now().isoformat()
        f.write(f"[{timestamp}] DOWN: {url}\n")
