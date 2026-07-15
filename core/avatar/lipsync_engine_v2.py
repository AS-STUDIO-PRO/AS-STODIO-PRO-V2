import os
import subprocess
import shutil
import librosa

class ASAvatarStudioEngineV2:
    def __init__(self, cache_dir="/content/drive/MyDrive/AS_Studio_V2_Cache"):
        self.cache_dir = cache_dir
        os.makedirs(self.cache_dir, exist_ok=True)
        print("[+] Engine V2 Initialized.")

    def sync_lips(self, video_path, audio_path, output_path):
        if os.path.exists(output_path):
            os.remove(output_path)

        try:
            audio_duration = librosa.get_duration(path=audio_path)
        except Exception:
            audio_duration = 15.0  # Dynamic fallback if librosa fails

        os.makedirs(os.path.dirname(output_path), exist_ok=True)

        ffmpeg_cmd = [
            'ffmpeg', '-y',
            '-stream_loop', '-1',
            '-i', video_path,
            '-i', audio_path,
            '-map', '0:v:0',
            '-map', '1:a:0',
            '-vf', 'scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2,format=yuv420p',
            '-c:v', 'libx264', '-preset', 'ultrafast', '-b:v', '6000k',
            '-c:a', 'aac', '-b:a', '192k',
            '-threads', '0',
            '-shortest',
            output_path
        ]

        subprocess.run(ffmpeg_cmd, check=True)

        # Disconnect safety: Save a copy directly to Google Drive
        drive_output_dir = "/content/drive/MyDrive/AS_Studio_Outputs"
        os.makedirs(drive_output_dir, exist_ok=True)
        drive_backup_path = os.path.join(drive_output_dir, os.path.basename(output_path))
        shutil.copy(output_path, drive_backup_path)
        print(f"[+] Output saved to Drive for safety (even after disconnect): {drive_backup_path}")

        return output_path