import os
import cv2
import argparse
from tqdm import tqdm


parser = argparse.ArgumentParser(description='Extract frames from an MP4 file')
parser.add_argument('mp4_file', type=str, help='path to the MP4 file')
args = parser.parse_args()


def extract_frames(video_path, output_path):
    # Create output directory
    os.makedirs(output_path, exist_ok=True)
    
    # Open video file
    cap = cv2.VideoCapture(video_path)

    # Get video frame count and fps
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))

    # Loop through video and extract frames
    for i in tqdm(range(total_frames)):
        # Read frame
        ret, frame = cap.read()

        # Check if frame was successfully read
        if not ret:
            break

        # Set frame filename and path
        filename = f"{i:05d}.jpg"
        filepath = os.path.join(output_path, filename)

        # Save frame to file
        cv2.imwrite(filepath, frame)

    # Release video file
    cap.release()

    print(f"Extracted {total_frames} frames at {fps} fps to {output_path}")

# Extract frames from MP4 file
extract_frames(args.mp4_file, "frames")