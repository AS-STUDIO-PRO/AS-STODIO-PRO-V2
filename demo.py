import os
import sys
import gradio as gr

PROJECT_PATH = "/content/AS-STODIO-PRO-V2"
if PROJECT_PATH not in sys.path:
    sys.path.append(PROJECT_PATH)

from core.avatar.lipsync_engine_v2 import ASAvatarStudioEngineV2
studio = ASAvatarStudioEngineV2()

def yt_safe_runner_v2(video_file, audio_file):
    if video_file is None or audio_file is None:
        return "Error: Please upload both files."
    output_path = os.path.join(PROJECT_PATH, "outputs/as_studio_v2_fast_1080p.mp4")
    return studio.sync_lips(video_path=video_file, audio_path=audio_file, output_path=output_path)

with gr.Blocks() as demo:
    gr.Markdown("# 🚀 AS AVATAR STUDIO V2")
    with gr.Row():
        with gr.Column():
            v_in = gr.Video(label="Target Video")
            a_in = gr.Audio(label="Driving Audio", type="filepath")
            btn = gr.Button("🎬 Render Scene", variant="primary")
        with gr.Column():
            v_out = gr.Video(label="✨ Output Preview")
    btn.click(fn=yt_safe_runner_v2, inputs=[v_in, a_in], outputs=v_out)

if __name__ == "__main__":
    demo.queue(max_size=30)
    # inline=True launches Gradio directly inside Colab outputs frame
    demo.launch(inline=True, share=True, height=500)