import random

import time

from pathlib import Path

from storage.config.data_paths import paths

from services.proccesors.clip_handler import process_clip

from services.uplouders.tiktok import upload_video


STATE_FILE = Path(paths.Storage_folder) / 'automation_state.txt'
OVERRIDE_FILE = Path(paths.Storage_folder) / 'override_state.txt'

TIMER_RANGE = [3600, 4000]

def main_action():
    process_clip(upload_video)
    pass


def get_random_time():
    return random.randint(
        TIMER_RANGE[0],
        TIMER_RANGE[1]
    )


def read_number(file):

    if not file.exists():
        return None

    try:
        return int(file.read_text().strip())
    except ValueError:
        return None


def write_state(file, value):
    file.write_text(str(value))


def start_timer():

    while True:

        # Check for manual override
        override = read_number(OVERRIDE_FILE)

        if override is not None:
            write_state(STATE_FILE, override)
            write_state(OVERRIDE_FILE, 'none')

        # Read current timer
        remaining = read_number(STATE_FILE)

        # No timer exists, create a random one
        if remaining is None:
            remaining = get_random_time()
            write_state(STATE_FILE, remaining)

        # Timer finished
        if remaining <= 0:

            main_action()

            print('\nTimer finished.')

            # Generate the next random timer
            remaining = get_random_time()
            write_state(STATE_FILE, remaining)

            print(f'Next timer: {remaining}s')

        print(
            f'\rNext action in {remaining}s',
            end='',
            flush=True
        )

        time.sleep(1)

        # Tick timer
        write_state(STATE_FILE, remaining - 1)


def background_service():
    start_timer()


