import cv2
import numpy as np
import os

ASCII_CHARS = ["@", "#", "8", "&", "%", "$", "?", "*", "+", ";", ":", ",", ".", " "]

def bgr2gray(bgr):
    return np.dot(bgr[..., :3], [0.1140, 0.5870, 0.2989])

def min_max_normalize(data):
    min_vals = np.min(data)
    max_vals = np.max(data)
    return ((data - min_vals) / (max_vals - min_vals)) * (len(ASCII_CHARS) - 1)

def gen_img_art(frame, width):
    img_height, img_width = frame.shape[:2]
    ratio = img_height / img_width
    height = int(ratio * width * 0.5)
    img = cv2.resize(frame, (width, height))
    img = bgr2gray(img)
    img = min_max_normalize(img)
    
    output = []
    for y in range(height):
        row = []
        for x in range(width):
            index = int(img[y, x])
            row.append(ASCII_CHARS[index])
        output.append("".join(row))
    return output

def gen_art(video_path, width=100):
    cap = cv2.VideoCapture(video_path)
    ascii_frames = []

    if not cap.isOpened():
        raise Exception("Could not open video.")

    base_filename = os.path.splitext(os.path.basename(video_path))[0]
    output_file = os.path.join(app.config['OUTPUT_FOLDER'], f"{base_filename}_ascii_art.txt")

    with open(output_file, "w") as file:
        frame_count = 0
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            frame_count += 1
            if frame_count % 5 == 0:
                art = gen_img_art(frame, width)
                file.write(f"\n--- Frame {int(frame_count / 5)} ---\n")
                file.write("\n".join(art))
                file.write("\n\n")

    cap.release()
    return output_file