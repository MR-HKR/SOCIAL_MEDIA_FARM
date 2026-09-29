from pathlib import Path

from storage.config.data_paths import paths


video_folder = Path(paths.Edited_videos)


def process_video(action):

    videos = sorted(
        video for video in video_folder.iterdir()
        if video.is_file()
        and video.suffix.lower() in ['.mp4', '.mkv', '.mov', '.avi', '.webm']
    )

    if not videos:
        return

    video = videos[0]

    action(video)

    video.unlink()