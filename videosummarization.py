import cv2
import os
from tkinter import Tk, filedialog

def summarize_video_with_exact_duration(video_paths, output_path, target_duration=60):
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    frames_to_save = []
    frame_width, frame_height, fps = None, None, None
    
    for video_path in video_paths:
        cap = cv2.VideoCapture(video_path)
        
        # Verify video opened successfully
        if not cap.isOpened():
            print(f"Error: Could not open video {video_path}")
            continue
        
        # Set video properties based on the first valid video
        if frame_width is None or frame_height is None:
            frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
            frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
            fps = int(cap.get(cv2.CAP_PROP_FPS))
        
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            # Convert frame to gray scale for face detection
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(50, 50))
            
            # If a face is detected, add the frame to the list
            if len(faces) > 0:
                frames_to_save.append(frame)
                
                # Stop collecting frames once we have enough for the target duration
                if len(frames_to_save) >= target_duration * fps:
                    break
        
        cap.release()
    
    # Ensure we have enough frames to create a 60-second video
    min_frames_required = target_duration * fps

    # Write output video ensuring it is at least 60 seconds long
    if frames_to_save:
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        output_video = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height))
        
        for frame in frames_to_save[:min_frames_required]:  # Ensure we only write the required frames
            output_video.write(frame)
        
        output_video.release()
        print(f"Summarized video saved successfully as {output_path}")
    else:
        print("Error: No valid frames found for summarization.")

def select_videos_and_summarize(output_folder="summarized_video", target_duration=60):
    # Open file dialog to select videos
    Tk().withdraw()  # Hide the root window
    video_paths = filedialog.askopenfilenames(
        title="Select CCTV Videos",
        filetypes=[("Video files", "*.mp4 *.avi *.mov")]
    )
    
    if not video_paths:
        print("No video selected.")
        return
    
    # Output file path
    output_path = os.path.join(output_folder, "front_view_summary.mp4")
    
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Summarize the videos ensuring an exact duration requirement
    summarize_video_with_exact_duration(video_paths, output_path, target_duration)

# Example usage
select_videos_and_summarize()*