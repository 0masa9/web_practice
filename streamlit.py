import streamlit as st
from ultralytics import YOLO
import tempfile
import os

st.title("野球映像のハイライト生成")

uploaded_file = st.file_uploader("試合映像(mp4)をアップロードしてください", type=["mp4"])

if uploaded_file is not None:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as temp_file:
        temp_file.write(uploaded_file.read())
        video_path = temp_file.name

    st.video(video_path)
    st.write("処理中...")

    # YOLOv8 Poseモデルで検出
    model = YOLO("yolov8n-pose.pt")
    results = model.predict(video_path, save=True, save_txt=True)

    st.success("処理完了！")
    st.video("runs/predict/predict0/video.mp4")  # 出力映像（例）

    # ハイライト動画ダウンロードリンク
    with open("runs/predict/predict0/video.mp4", "rb") as f:
        st.download_button("ハイライトをダウンロード", f, file_name="highlight.mp4")
