#!/usr/bin/env python3

import os
import subprocess
import sys

def install_dependencies():
    if sys.platform.startswith("linux"):
        os.system("sudo apt-get update")
        os.system("sudo apt-get install ffmpeg")
    elif sys.platform.startswith("darwin"):
        os.system("brew update")
        os.system("brew install ffmpeg")
    else:
        print("Unsupported operating system")
        sys.exit(1)

def check_dependencies():
    try:
        subprocess.check_output(["ffmpeg", "-version"])
        subprocess.check_output(["ffprobe", "-version"])
    except FileNotFoundError:
        print("FFmpeg and FFprobe not found, installing...")
        install_dependencies()

def calculate_vmaf_psnr(source, converted):
    command = (
        f'ffmpeg -i {source} -i {converted} -lavfi '
        f'"[0:v]setpts=PTS-STARTPTS[ref];[1:v]setpts=PTS-STARTPTS[main];'
        f'[main][ref]libvmaf=model_path=vmaf_v0.6.1.pkl:psnr=1:log_fmt=json" '
        f'-f null -'
    )
    output = subprocess.check_output(command, shell=True, text=True)
    print(output)

def main():
    check_dependencies()

    if len(sys.argv) != 3:
        print("Usage: python check_vmaf_psnr.py <source_video> <converted_video>")
        sys.exit(1)

    source_video = sys.argv[1]
    converted_video = sys.argv[2]

    if not os.path.isfile(source_video) or not os.path.isfile(converted_video):
        print("One or both of the input files do not exist.")
        sys.exit(1)

    calculate_vmaf_psnr(source_video, converted_video)

if __name__ == "__main__":
    main()
