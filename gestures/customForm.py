import cv2 
import mediapipe as mp
import pyautogui
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait


# Set up webdriver
def form():
    option = webdriver.ChromeOptions()
    option.add_argument("-incognito")
    #option.add_argument("--headless")
    #option.add_argument("disable-gpu")

    browser = webdriver.Chrome(executable_path='C/Users/Colin/Downloads/chromedriver_win32', options=option)
    browser.get('C:/Users/Colin/VSCode_projects/gesture/form.html')

    # WebDriverWait(browser, 5)
    checkboxes = []
    checkboxes.append(browser.find_element(By.XPATH, '//*[@id="1"]'))
    checkboxes.append(browser.find_element(By.XPATH, '//*[@id="2"]'))
    checkboxes.append(browser.find_element(By.XPATH, '//*[@id="3"]'))

    print(len(checkboxes))
    submitbutton = browser.find_element(By.XPATH, '/html/body/form/input')

    return (checkboxes, submitbutton)


# Count fingers being held up -> int
def count_fingers(hand):
    
    count = 0

    thresh = (hand.landmark[0].y*100 - hand.landmark[9].y*100)/2

    if (hand.landmark[5].y*100 - hand.landmark[8].y*100) > thresh:
        count += 1

    if (hand.landmark[9].y*100 - hand.landmark[12].y*100) > thresh:
        count += 1

    if (hand.landmark[13].y*100 - hand.landmark[16].y*100) > thresh:
        count += 1

    if (hand.landmark[17].y*100 - hand.landmark[20].y*100) > thresh:
        count += 1

    if (hand.landmark[5].x*100 - hand.landmark[4].x*100) > 6:
        count += 1

    return count 


def main():

    capture = cv2.VideoCapture(0)

    drawing = mp.solutions.drawing_utils
    hands = mp.solutions.hands
    hand_obj = hands.Hands(max_num_hands=1)

    start_init = False 

    prev = -1

    radiobuttons, submitbutton = form()

    while True:
        end_time = time.time()
        cap_error, frame = capture.read()

        frame = cv2.flip(frame, 1)

        res = hand_obj.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

        if res.multi_hand_landmarks:

            hand_keyPoints = res.multi_hand_landmarks[0]

            count = count_fingers(hand_keyPoints)

            if not(prev==count):
                if not(start_init):
                    start_time = time.time()
                    start_init = True

                elif (end_time-start_time) > 0.2:
                    if (count == 1):
                        radiobuttons[0].click()
                
                    elif (count == 2):
                        radiobuttons[1].click()

                    elif (count == 3):
                        radiobuttons[2].click()

                    elif (count == 5):
                        submitbutton.click()
                        cv2.destroyAllWindows()
                        capture.release()
                        break

                    prev = count
                    start_init = False


            drawing.draw_landmarks(frame, hand_keyPoints, hands.HAND_CONNECTIONS)

        cv2.imshow("window", frame)

        if cv2.waitKey(1) == 27:
            cv2.destroyAllWindows()
            capture.release()
            break


if __name__ == '__main__':
    main()