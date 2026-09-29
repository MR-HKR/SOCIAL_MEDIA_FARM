import subprocess

from pathlib import Path

from storage.config.data_paths import paths


edited_videos_folder = Path(paths.Edited_videos)
edited_videos_folder.mkdir(parents=True, exist_ok=True)


def edit_video(video):

    video = Path(video)

    output = edited_videos_folder / f'{video.stem}.mp4'

    subprocess.run([
        'ffmpeg',
        '-y',
        '-i', str(video),

        '-vf',
        (
            'setpts=0.95*PTS,'
            'hflip,'
            'scale=720:1280:force_original_aspect_ratio=decrease,'
            'pad=720:1280:(ow-iw)/2:(oh-ih)/2:color=black,'
            'drawbox=x=0:y=0:w=iw-1:h=ih-1:'
            'color=white:t=8'
        ),

        '-af',
        'atempo=1.0526',

        '-c:v', 'libx264',
        '-preset', 'ultrafast',
        '-crf', '23',

        '-c:a', 'aac',

        str(output)
    ])

    return output