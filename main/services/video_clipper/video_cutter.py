import subprocess
from pathlib import Path

from storage.config.data_paths import paths


START_TIME = 33
CLIP_LENGTH = 300
CLIP_COUNT = 4

clips_folder = Path(paths.Clips_folder)


def cut_video(video):

    video = Path(video)

    output_folder = clips_folder / video.stem
    output_folder.mkdir(parents=True, exist_ok=True)

    for i in range(CLIP_COUNT):

        start = START_TIME + (i * CLIP_LENGTH)

        output = output_folder / f'{i + 1}_output.mp4'

        subprocess.run([
            'ffmpeg',
            '-ss', str(start),
            '-i', str(video),
            '-t', str(CLIP_LENGTH),
            '-c', 'copy',
            str(output)
        ])

    return output_folder