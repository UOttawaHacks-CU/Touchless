import cv2 
import mediapipe as mp
import pyautogui
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

option = webdriver.ChromeOptions()
option.add_argument("-incognito")
#option.add_argument("--headless")

browser = webdriver.Chrome(executable_path='C/Users/Colin/Downloads/chromedriver_win32', options=option)
browser.get('https://www.ontario.ca/self-assessment')
time.sleep(1)
browser.find_element(By.CLASS_NAME, "ontario-button--primary").click()

# Set up webdriver
def form():

    print('Getting all elements for current webpage')
    time.sleep(1)

    # Control flow if the current url is the multi check
    get_url = browser.current_url
    if (get_url == 'https://www.ontario.ca/self-assessment/question-symptoms-not-immunocompromised'):
        # code for multi check
        back_buttons = browser.find_element(By.CLASS_NAME, "ontario-button--tertiary")
        clear_button = browser.find_element(By.ID, "none_of_the_above")
        sick_button = browser.find_element(By.ID, "fever_and_or_chills")
        submit_button = browser.find_element(By.CLASS_NAME, "ontario-button--primary")
        buttons = [clear_button, sick_button, submit_button]
    else:
        buttons = browser.find_elements(By.CLASS_NAME, "ontario-button--primary")
        back_buttons = browser.find_element(By.CLASS_NAME, "ontario-button--tertiary")
    return (back_buttons, buttons)


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

    Back_button, buttons = form()

    if (len(buttons) > 2):
        multi = True
        Clear = buttons[0]
        Sick = buttons[1]
        Submit = buttons[2]
    else:
        multi = False
        Clear = buttons[0]
        Sick = buttons[1]

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
                        Back_button.click()
                        print('Back clicked')

                        Back_button, buttons = form()

                        if (len(buttons) > 2):
                            multi = True
                            Clear = buttons[0]
                            Sick = buttons[1]
                            Submit = buttons[2]
                        else:
                            multi = False
                            Clear = buttons[0]
                            Sick = buttons[1]
                
                    elif (count == 2):
                        if not multi:
                            Clear.click()
                        else:
                            Clear.click()
                            Submit.click()

                        print('False clicked')
                        Back_button, buttons = form()

                        if (len(buttons) > 2):
                            multi = True
                            Clear = buttons[0]
                            Sick = buttons[1]
                            Submit = buttons[2]
                        else:
                            multi = False
                            Clear = buttons[0]
                            Sick = buttons[1]

                    elif (count == 3):
                        if not multi:
                            Clear.click()
                        else:
                            Clear.click()
                            Submit.click()
                            
                        print('False clicked')
                        Back_button, buttons = form()

                        if (len(buttons) > 2):
                            multi = True
                            Clear = buttons[0]
                            Sick = buttons[1]
                            Submit = buttons[2]
                        else:
                            multi = False
                            Clear = buttons[0]
                            Sick = buttons[1]

                    elif (count == 4):
                        if not multi:
                            Clear.click()
                        else:
                            Clear.click()
                            Submit.click()
                            
                        print('False clicked')
                        Back_button, buttons = form()

                        if (len(buttons) > 2):
                            multi = True
                            Clear = buttons[0]
                            Sick = buttons[1]
                            Submit = buttons[2]
                        else:
                            multi = False
                            Clear = buttons[0]
                            Sick = buttons[1]

                    elif (count == 5):
                        print('True Clicked')

                        if not multi:
                            Sick.click()
                        else:
                            Sick.click()
                            Submit.click()

                        print('You are sick')
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