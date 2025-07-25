#!/usr/bin/env python3
import os
from PIL import Image
import json

def sprite_to_ansi(image_path, output_dir, scale=2):
    """Convert one sprite to ANSI text with better transparency handling"""
    try:
        img = Image.open(image_path)
        digimon_name = os.path.splitext(os.path.basename(image_path))[0]
        
        os.makedirs(os.path.join(output_dir, digimon_name), exist_ok=True)
        
        if img.size != (16, 16):
            img = img.resize((16, 16), Image.NEAREST)
        img = img.resize((16*scale, 16*scale), Image.NEAREST)
        
        has_alpha = img.mode == 'RGBA'
        if has_alpha:
            alpha = img.split()[-1]
            img = img.convert('RGB')  
        
        sprite_path = os.path.join(output_dir, digimon_name, "sprite.txt")
        with open(sprite_path, 'w', encoding='utf-8') as f:
            for y in range(0, img.height, 2):
                for x in range(img.width):
                    top_r, top_g, top_b = img.getpixel((x, y))
                    bottom_r, bottom_g, bottom_b = (0, 0, 0)
                    
                    draw_bottom = True
                    if y+1 < img.height:
                        bottom_r, bottom_g, bottom_b = img.getpixel((x, y+1))
                        if has_alpha and alpha.getpixel((x, y+1)) < 128:  
                            draw_bottom = False
                    
                    if has_alpha and alpha.getpixel((x, y)) < 128:  
                        if draw_bottom:
                            f.write(f"\033[48;2;{bottom_r};{bottom_g};{bottom_b}m▄")  
                        else:
                            f.write("\033[0m ")
                    else:
                        if draw_bottom:
                            f.write(f"\033[38;2;{top_r};{top_g};{top_b};48;2;{bottom_r};{bottom_g};{bottom_b}m▀")
                        else:
                            f.write(f"\033[38;2;{top_r};{top_g};{top_b}m▀")
                f.write("\033[0m\n")  
                
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
    batch_convert("raw_sprites/16x16", "digimon_data", 2)  