# STEP 1: Import the necessary modules.
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision


def work():

    images = []
    results = []

    IMAGE_FILENAMES = [
        "C:/Users/Colin/Downloads/Thumbs/thumbs-up-3282064.jpg",
        "C:/Users/Colin/Downloads/Thumbs/gettyimages-1363140175-612x612.jpg",
        "C:/Users/Colin/Downloads/Thumbs/thumbs-down.jpg",
        "C:/Users/Colin/Downloads/Thumbs/thumbdown.jpg"
    ]

    for image_file_name in IMAGE_FILENAMES:
    # STEP 3: Load the input image.
        image = mp.Image.create_from_file(image_file_name)

        # STEP 4: Recognize gestures in the input image.
        recognition_result = recognizer.recognize(image)

        # STEP 5: Process the result. In this case, visualize it.
        images.append(image)
        top_gesture = recognition_result.gestures[0][0]
        hand_landmarks = recognition_result.hand_landmarks
        results.append((top_gesture, hand_landmarks))

    display_batch_of_images_with_gestures_and_hand_landmarks(images, results)


def collectGestures():
    base_options = python.BaseOptions(model_asset_path='C:/Users/Colin/Downloads/gesture_recognizer.task')
    options = vision.GestureRecognizerOptions(base_options=base_options)
    recognizer = vision.GestureRecognizer.create_from_options(options)


if __name__ == '__main__':
    collectGestures()