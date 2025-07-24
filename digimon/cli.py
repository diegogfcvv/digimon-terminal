#!/usr/bin/env python3
import os
import random
import argparse
import json
from . import DATA_DIR

class DigimonViewer:
    def __init__(self, data_dir=DATA_DIR):
        self.data_dir = data_dir
        self.digimon_list = self._load_digimon_list()

    def _load_digimon_list(self):
        return [d.name for d in self.data_dir.iterdir() if d.is_dir()]

    def get_random_digimon(self):
        return random.choice(self.digimon_list)

    def show_digimon(self, name, show_metadata=True):
        try:
            sprite_path = self.data_dir / name / "sprite.txt"
            with open(sprite_path, 'r', encoding='utf-8') as f:
                print(f.read())
                
            if show_metadata:
                data_path = self.data_dir / name / "data.json"
                with open(data_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    print(f"\n\033[1m{data['name']}\033[0m")
                    if 'description' in data:
                        print(f"\n{data['description']}")
        except Exception as e:
            print(f"Error displaying {name}: {str(e)}")

def main():
    parser = argparse.ArgumentParser(description="Digimon Terminal Viewer")
    parser.add_argument(
        "-n", "--name", 
        help="Show specific Digimon by name"
    )
    parser.add_argument(
        "-r", "--random", 
        action="store_true", 
        help="Show random Digimon"
    )
    parser.add_argument(
        "-m", "--metadata", 
        action="store_true", 
        help="Show name and description"
    )
    parser.add_argument(
        "-l", "--list", 
        action="store_true", 
        help="List all available Digimon"
    )
    args = parser.parse_args()

    viewer = DigimonViewer()

    if args.list:
        print("Available Digimon:")
        for d in sorted(viewer.digimon_list):
            print(f"- {d}")
        return

    if args.name:
        input_name = args.name.lower()
        matched_name = next(
            (d for d in viewer.digimon_list if d.lower() == input_name),
            None
        )
        
        if not matched_name:
            print(f"Digimon '{args.name}' not found. Available Digimon:")
            for d in sorted(viewer.digimon_list):
                print(f"- {d}")
            return
            
        viewer.show_digimon(matched_name, args.metadata)
        
    elif args.random:
        random_digi = viewer.get_random_digimon()
        viewer.show_digimon(random_digi, args.metadata)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()