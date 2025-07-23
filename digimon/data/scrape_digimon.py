import requests
from bs4 import BeautifulSoup
import json
import os
import re
from urllib.parse import quote

def scrape_digimon_data(digimon_name):
    url_name = quote(digimon_name.replace(" ", "_"))
    url = f"https://digimon.fandom.com/wiki/{url_name}"
    
    try:
        print(f"Fetching {digimon_name}...")
        response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        description = ""
        mw_content = soup.find("div", {"class": "mw-parser-output"})
        
        for element in mw_content.children:
            if element.name == "p" and element.get_text(strip=True):
                desc_text = element.get_text(" ", strip=True)
                if len(desc_text) > 50 and not any(x in desc_text for x in ["Level", "Type", "Attribute"]):
                    description = re.sub(r'\[\s*\d+\s*\]', '', desc_text)
                    break

        data = {
            "name": digimon_name,
            "description": description if description else f"{digimon_name} is a Digimon."
        }

        os.makedirs(f"digimon_data/{digimon_name}", exist_ok=True)
        with open(f"digimon_data/{digimon_name}/data.json", "w", encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        
        print(f"✅ Saved {digimon_name}")
        return True

    except Exception as e:
        print(f"❌ Failed {digimon_name}: {str(e)}")
        return False