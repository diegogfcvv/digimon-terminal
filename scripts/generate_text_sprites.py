#!/usr/bin/env python3
import os
from PIL import Image
import json

def sprite_to_ansi(image_path, output_dir, scale=2):
    """Convert one sprite to ANSI text"""
    try:
        img = Image.open(image_path)
        digimon_name = os.path.splitext(os.path.basename(image_path))[0]
        
        os.makedirs(os.path.join(output_dir, digimon_name), exist_ok=True)
        
        if img.size != (16, 16):
            img = img.resize((16, 16))
        img = img.resize((16*scale, 16*scale), Image.NEAREST)
        
        if img.mode == 'RGBA':
            background = Image.new('RGB', img.size, (0, 0, 0))
            background.paste(img, mask=img.split()[-1])
            img = background
        elif img.mode != 'RGB':
            img = img.convert('RGB')
        
        sprite_path = os.path.join(output_dir, digimon_name, "sprite.txt")
        with open(sprite_path, 'w', encoding='utf-8') as f:
            for y in range(0, img.height, 2):
                for x in range(img.width):
                    r,g,b = img.getpixel((x, y))
                    r2,g2,b2 = img.getpixel((x, y+1)) if y+1 < img.height else (0,0,0)
                    f.write(f"\033[38;2;{r};{g};{b};48;2;{r2};{g2};{b2}m▀\033[0m")
                f.write("\n")
        
        json_path = os.path.join(output_dir, digimon_name, "data.json")
        if not os.path.exists(json_path):
            with open(json_path, 'w') as f:
                json.dump({
                    "name": digimon_name.capitalize(),
                    "description": f"A {digimon_name.capitalize()} Digimon",
                    "level": "Rookie",
                    "type": "Unknown"
                }, f, indent=2)
        
        print(f"Converted {digimon_name}")
    except Exception as e:
        print(f"Failed {image_path}: {str(e)}")

def batch_convert(input_dir, output_dir="digimon_data", scale=2):
    """Convert all PNGs in directory"""
    print(f"Converting sprites from {input_dir} to {output_dir} (scale: {scale}x)")
    for filename in os.listdir(input_dir):
        if filename.lower().endswith('.png'):
            sprite_to_ansi(
                os.path.join(input_dir, filename),
                output_dir,
                scale
            )
    print("Conversion complete!")

if __name__ == '__main__':
    import sys
    if sys.platform == "win32":
        os.system("chcp 65001")     
    batch_convert("raw_sprites/16x16", "digimon_data", 3)