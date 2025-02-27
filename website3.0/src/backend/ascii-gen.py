import cv2
import numpy as np
import os
import sys

ASCII_CHARS = ["@", "#", "8", "&", "%", "$", "?", "*", "+", ";", ":", ",", ".", " "]
WIDTH_DEFAULT = 100

def bgr2gray(bgr):
    return np.dot(bgr[..., :3], [0.1140, 0.5870, 0.2989])

def min_max_normalize(data):
    min_vals = np.min(data)
    max_vals = np.max(data)
    return ((data - min_vals) / (max_vals - min_vals)) * (len(ASCII_CHARS) - 1)

def gen_img_art(frame, width=WIDTH_DEFAULT):
    img_height, img_width = frame.shape[:2]
    ratio = img_height / img_width
    height = int(ratio * width * 0.5)
    img = cv2.resize(frame, (width, height))
    img = bgr2gray(img)
    img = min_max_normalize(img)
    
    ascii_frame = []
    for y in range(height):
        row = []
        for x in range(width):
            index = int(img[y, x])
            row.append(ASCII_CHARS[index])
        ascii_frame.append("".join(row))
    return ascii_frame

def gen_video_art(video_path, width=WIDTH_DEFAULT):
    cap = cv2.VideoCapture(video_path)
    ascii_frames = []

    if not cap.isOpened():
        raise Exception("Could not open video.")

    frame_count = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frame_count += 1
        if frame_count % 5 == 0:
            art = gen_img_art(frame, width)
            ascii_frames.append(art)

    cap.release()
    return ascii_frames

def save_ascii_art(ascii_art, output_path):
    with open(output_path, 'w') as f:
        # if video
        if isinstance(ascii_art[0], list):
            for frame in ascii_art:
                f.write("\n".join(frame) + "\n\n")
        # else it is a frame
        else: 
            f.write("\n".join(ascii_art))
            
def process_file(file_path, width):
    """Process the file (image or video) and generate ASCII art."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file '{file_path}' does not exist.")

    if not width or width <= 0:
        width = WIDTH_DEFAULT

    if file_path.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
        # process image
        frame = cv2.imread(file_path)
        if frame is None:
            raise Exception("Could not read image.")
        ascii_art = gen_img_art(frame, width)
    elif file_path.lower().endswith(('.mp4', '.avi', '.mov', '.mkv')):
        # process video
        ascii_art = gen_video_art(file_path, width)
    else:
        raise ValueError("Unsupported file type.")
    
    # save to text file
    output_path = os.path.splitext(file_path)[0] + '_ascii_art.txt'
    save_ascii_art(ascii_art, output_path)
    return output_path

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python process_file.py <file_path> <width>")
        sys.exit(1)

    file_path = sys.argv[1]
    try:
        width = int(sys.argv[2])
    except ValueError:
        print("Width must be an integer.")
        sys.exit(1)

    try:
        output_path = process_file(file_path, width)
        print(output_path)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
