# Extract frames from video

import cv2
import os
import sys


def extract_frames(video_path, output_path):
    for video_name in os.listdir(video_path):

        video = os.path.join(video_path, video_name)
        output = os.path.join(output_path, video_name)

        if os.path.exists(output):
            continue

        # Create directory for each video
        os.makedirs(output, exist_ok=True)

        # Read video
        cap = cv2.VideoCapture(video)
        frame_count = 0

        while True:
            ret, frame = cap.read()

            if not ret:
                break

            frame_name = f"{frame_count}_{video_name}.jpg"
            frame_path = os.path.join(output, frame_name)

            cv2.imwrite(frame_path, frame)
            frame_count += 1

        cap.release()
        cv2.destroyAllWindows()


# if __name__ == "__main__":
#     raw_videos_path = "./raw_video"

#     for video_folder in os.listdir(raw_videos_path):
#         video_path = os.path.join(raw_videos_path, video_folder)
#         output_path = f"./frames/{video_folder}"

#         extract_frames(video_path, output_path)
#         print(f"Extracted frames from {video_folder}")


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        root_folder = "./raw_video"
        output_path = "./raw_dataset"

        for video_folder in os.listdir(root_folder):
            if len(video_folder) > 1:
                continue
            video_path = os.path.join(root_folder, video_folder)
            output = os.path.join(output_path, video_folder)

            extract_frames(video_path, output)
            print(f"Extracted frames from {video_folder}")

    else:
        video_folder = sys.argv[1]
        output_path = f"./raw_dataset/{video_folder}"
        video_path = "./raw_video_dataset/" + video_folder

        extract_frames(video_path, output_path)
        print(f"Extracted frames from {video_folder}")
