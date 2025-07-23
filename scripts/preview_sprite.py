#!/usr/bin/env python3
import argparse
import os

def preview_sprite(sprite_path):
    with open(sprite_path, 'r', encoding='utf-8') as f:
        print(f.read())

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('sprite', help='Path to sprite.txt')
    args = parser.parse_args()
    preview_sprite(args.sprite)