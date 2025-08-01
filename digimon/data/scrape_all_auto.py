#!/usr/bin/env python3
import os
import time
import json
from scrape_digimon import scrape_digimon_data

def needs_scraping(folder_path):
    """Check if folder needs scraping"""
    data_file = os.path.join(folder_path, "data.json")
    if not os.path.exists(data_file):
        return True
    
    try:
        with open(data_file, 'r') as f:
            data = json.load(f)
            return "description" not in data or data["description"].endswith("is a Digimon.")
    except:
        return True

def main():
    base_dir = "digimon_data"
    processed = 0
    skipped = 0
    failed = []
    
    print(f"Scanning {base_dir} for Digimon to scrape...")
    
    for folder in sorted(os.listdir(base_dir)):
        folder_path = os.path.join(base_dir, folder)
        if os.path.isdir(folder_path):
            if needs_scraping(folder_path):
                print(f"\n⌛ Processing {folder}...", end=" ", flush=True)
                try:
                    if scrape_digimon_data(folder):
                        processed += 1
                        print("✅")
                    else:
                        failed.append(folder)
                        print("❌ (will retry later)")
                except Exception as e:
                    print(f"⚠️ Error: {str(e)}")
                    failed.append(folder)
                time.sleep(1)
            else:
                skipped += 1
    
    if failed:
        print("\n🔁 Retrying failed Digimon...")
        for folder in failed.copy():
            print(f"Retrying {folder}...", end=" ", flush=True)
            if scrape_digimon_data(folder):
                failed.remove(folder)
                processed += 1
                print("✅")
            else:
                print("❌")
            time.sleep(2)
    
    print(f"\n🎉 Done! Processed: {processed}, Skipped: {skipped}, Failed: {len(failed)}")
    if failed:
        print("These Digimon need manual attention:")
        for name in failed:
            print(f"- {name}")

if __name__ == "__main__":
    main()