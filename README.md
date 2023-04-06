# Video Quality Metrics - VMAF and PSNR

This Python script calculates the Video Multi-Method Assessment Fusion (VMAF) and Peak Signal-to-Noise Ratio (PSNR) of video files in formats such as MP4, AV1, VP9, HLS, etc. It takes the file paths of the source and converted videos as user input.

## Dependencies

- Python 3
- FFmpeg
- FFprobe

The script will check for dependencies and install them if needed.

## Getting Started

1. Clone the repository:



```bash
git clone https://github.com/yourusername/Video-Quality-Metrics.git
cd Video-Quality-Metrics  `

Make sure you have the VMAF model file vmaf_v0.6.1.pkl in the repository folder. 
You can download it from https://github.com/Netflix/vmaf/tree/master/model

## Run the script with the source and converted video file paths:

bash
Copy code
python check_vmaf_psnr.py <source_video> <converted_video>

Replace <source_video> and <converted_video> with the file paths of the source and converted videos, respectively.

The script will print the VMAF and PSNR values for the given video files.
