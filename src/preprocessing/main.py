import random
from pathlib import Path

if __package__:
    from .frame_extraction import FrameExtractor
else:
    from frame_extraction import FrameExtractor


PROJECT_ROOT = Path(__file__).resolve().parents[2]
VIDEO_DIR = PROJECT_ROOT / "JAAD_clips"
FRAMES_DIR = PROJECT_ROOT / "src" / "data" / "images"
NUM_VIDEOS = 10


def get_random_videos(video_dir: Path, num_videos: int) -> list[Path]:
    videos = sorted(video_dir.glob("*.mp4"))

    if not videos:
        raise FileNotFoundError(f"No .mp4 videos found in {video_dir}")

    if len(videos) < num_videos:
        raise ValueError(f"Expected at least {num_videos} videos, found {len(videos)}")

    return random.sample(videos, num_videos)


def main() -> None:
    FRAMES_DIR.mkdir(parents=True, exist_ok=True)

    selected_videos = get_random_videos(VIDEO_DIR, NUM_VIDEOS)

    for video_path in selected_videos:
        output_folder = FRAMES_DIR / video_path.stem
        output_folder.mkdir(parents=True, exist_ok=True)

        extractor = FrameExtractor(video_path=video_path, output_folder=output_folder)
        extractor.extract_frames()

        print(f"Extracted frames from {video_path.name} to {output_folder}")


if __name__ == "__main__":
    main()
