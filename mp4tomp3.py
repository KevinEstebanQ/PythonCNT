import os
from moviepy.editor import VideoFileClip

def convert_mov_to_mp4(input_mov_path, output_mp4_path):
    """
    Converts a .mov video file to .mp4 format.
    """
    try:
        video_clip = VideoFileClip(input_mov_path)
        video_clip.write_videofile(output_mp4_path, codec="libx264", audio_codec="aac")
        video_clip.close()
        print(f"✅ Converted: '{input_mov_path}' → '{output_mp4_path}'")
    except Exception as e:
        print(f"❌ Failed to convert '{input_mov_path}': {e}")

if __name__ == "__main__":
    folder_path = r"C:\Users\Kevin\Desktop\Videos papa"  # Change this to your folder path
    output_folder = r"C:\Users\Kevin\Desktop\Videos papa\mp4"  # Output directory (optional)

    os.makedirs(output_folder, exist_ok=True)

    for filename in os.listdir(folder_path):
        if filename.lower().endswith(".mov"):
            input_path = os.path.join(folder_path, filename)
            output_filename = os.path.splitext(filename)[0] + ".mp4"
            output_path = os.path.join(output_folder, output_filename)
            convert_mov_to_mp4(input_path, output_path)