import os
import sys
import subprocess

# ============================
# Project Folder
# ============================

# Folder where all your .py files are stored
PROJECT_FOLDER = os.path.dirname(os.path.abspath(__file__))

# ============================
# Project List
# ============================

projects = {
    "1": "Face and Hand Marks Detection using Pyt",
    "2": "Hand Landmarks Detection",
    "3": "Pose landmark detection using Mediapipe",
    "4": "On-device ,Real-time Body Pose Trackin",
    "5": "Real-time Body Pose Tracking with inout",
    "6": "Object Detection with Webcam Using Me",
    "7": "3D Object Detection",
    "8": "3D Object Detection from Video",
    "9": "Instant Motion Tracking",
    "10": "Mediapipe 3D face transform",
    "11": "Media 3d Face Transform 2",
    "12": "Media 3D Face Transform 3",
    "13": "Media 3D Face Transform 4",
    "14": "Whole Detection"
}

# ============================
# Function to Find File
# ============================

def find_file(keyword):
    """
    Finds a Python file containing the keyword.
    """

    if not os.path.exists(PROJECT_FOLDER):
        return None

    for file in os.listdir(PROJECT_FOLDER):
        if file.endswith(".py") and keyword.lower() in file.lower():
            return os.path.join(PROJECT_FOLDER, file)

    return None


# ============================
# Main Loop
# ============================

while True:

    print("\n" + "=" * 65)
    print("             MEDIAPIPE PROJECT LAUNCHER")
    print("=" * 65)

    print("1. Face and Hand Marks Detection using Python")
    print("2. Hand Landmarks Detection")
    print("3. Pose Landmark Detection using Mediapipe")
    print("4. On-device, Real-time Body Pose Tracking")
    print("5. Real-time Body Pose Tracking with Input Video")
    print("6. Object Detection with Webcam Using Mediapipe")
    print("7. 3D Object Detection")
    print("8. 3D Object Detection from Video")
    print("9. Instant Motion Tracking")
    print("10. Mediapipe 3D Face Transform")
    print("11. Media 3D Face Transform 2")
    print("12. Media 3D Face Transform 3")
    print("13. Media 3D Face Transform 4")
    print("14. Whole Detection")
    print("0. Exit")

    choice = input("\nSelect Project : ")

    if choice == "0":
        print("\nGoodbye!")
        break

    if choice not in projects:
        print("\nInvalid Choice!")
        continue

    filepath = find_file(projects[choice])

    if filepath is None:
        print("\n❌ Project file not found.")
        print("Looking inside:", PROJECT_FOLDER)

        print("\nAvailable Python Files:\n")

        if os.path.exists(PROJECT_FOLDER):
            for f in os.listdir(PROJECT_FOLDER):
                if f.endswith(".py"):
                    print("•", f)

        input("\nPress Enter...")
        continue

    print("\nLaunching...\n")
    print(filepath)

    subprocess.run([sys.executable, filepath])

    print("\nProject Closed.")
    input("Press Enter to return to Main Menu...")