import subprocess
import os
import sys


def _path_to_ffmpeg() -> str:
    try:
        path = subprocess.check_output(["which", "ffmpeg"], text=True)
        return path
    except subprocess.CalledProcessError as e:
        sys.exit(f"ERROR: Command failed with return code {e.returncode}")


def _get_name(filepath: str) -> (str, str):
    file_exists = os.path.exists(filepath)
    if file_exists:
        file, extension = os.path.splitext(filepath)
    else:
        sys.exit(f'ERROR: File at "{filepath}" does not exist')
    return (file, extension)


def run_ffmpeg(filepath: str, activation_bytes: str) -> str:
    base_name, extension = _get_name(filepath)
    if extension == ".aax":
        file_mp4 = base_name + ".mp4"
        file_m4b = base_name + ".m4b"
    else:
        raise Exception(
            f'You must have a file with extension ".aax", you included a file with "{extension}"'
        )

    try:
        subprocess.check_output(
            [
                "ffmpeg",
                "-activation_bytes",
                activation_bytes,
                "-i",
                filepath,
                "-c",
                "copy",
                file_mp4,
            ]
        )
        subprocess.check_output(
            [
                "ffmpeg",
                "-activation_bytes",
                activation_bytes,
                "-i",
                filepath,
                "-c",
                "copy",
                file_m4b,
            ]
        )
    except subprocess.CalledProcessError as e:
        sys.exit(f"FFMPEG failed with return code {e.returncode}")
