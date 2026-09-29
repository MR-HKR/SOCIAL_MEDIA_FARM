from pathlib import Path

from storage.config.data_paths import paths


clips_folder = Path(paths.Clips_folder)


def process_clip(action):

    for folder in sorted(clips_folder.iterdir()):
        

        if not folder.is_dir():
            continue

        clips = sorted(
            video for video in folder.iterdir()
            if video.is_file()
            and video.suffix.lower() == '.mp4'
        )

        if not clips:
            folder.rmdir()
            continue

        clip = clips[0]

        action(clip)

        clip.unlink()

        if not any(folder.iterdir()):
            folder.rmdir()

        return

    