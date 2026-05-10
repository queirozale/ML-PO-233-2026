import cv2
import tqdm
from pathlib import Path
from typing import List


class FrameExtractor:
    def __init__(self, video_path: str | Path, output_folder: Path):
        self.video_path = video_path
        self.output_folder = output_folder

    def extract_frames(self) -> None:
        cap = cv2.VideoCapture(str(self.video_path))
        
        frame_id = 0
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            
            filename = self.output_folder / f"{frame_id:05d}.png"
            cv2.imwrite(str(filename), frame)
            
            frame_id += 1
        
        cap.release()

    def extract(self, video_list: List[str]) -> None:
        for video_path in tqdm(video_list):
            self.video_path = video_path
            self.extract_frames()