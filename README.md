# Touchless

## Structure
> /website : front end
> /speechform : get speech to text input and then process and send to backend
> /gestures : read user gestures

## More information from our devpost - (Here)[https://devpost.com/software/touchless-g72ten]

Inspiration
When visiting a clinic, two big complaints that we have are the long wait times and the necessity to use a kiosk that thousands of other people have already touched. We also know that certain methods of filling in information are not accessible to everyone (For example, someone with Parkinsons disease writing with a pen). In response to these problems, we created Touchless.

What it does
Touchless is an accessible and contact-free solution for gathering form information.
Allows users to interact with forms using voices and touchless gestures.
Users use different gestures to answer different questions.
Ex. Raise 1-5 fingers for 1-5 inputs, or thumbs up and down for yes and no.
Additionally, users are able to use voice for two-way interaction with the form. Either way, surface contact is eliminated.
Applicable to doctor’s offices and clinics where germs are easily transferable and dangerous when people touch the same electronic devices.
How we built it
Gesture and voice components are written in Python.
The gesture component uses OpenCV and Mediapipe to map out hand joint positions, where calculations could be done to determine hand symbols.
SpeechRecognition recognizes user speech
The form outputs audio back to the user by using pyttsx3 for text-to-speech, and beepy for alert noises.
We use AWS Gateway to open a connection to a custom lambda function which has been assigned roles using AWS Iam Roles to restrict access. The lambda generates a secure key which it sends with the data from our form that has been routed using Flask, to our noSQL dynmaoDB database.
Challenges we ran into
Tried to set up a Cerner API for FHIR data, but had difficulty setting it up.
As a result, we had to pivot towards using a noSQL database in AWS as our secure backend database for storing our patient data.
Accomplishments we’re proud of
This was our whole team’s first time using gesture recognition and voice recognition, so it was an amazing learning experience for us. We’re proud that we managed to implement these features within our project at a level we consider effective.

What we learned
We learned that FHIR is complicated. We ended up building a custom data workflow that was based on FHIR models we found online, but due to time constraints we did not implement certain headers and keys that make up industrial FHIR data objects.

What’s next for Touchless
In the future, we would like to integrate the voice and gesture components more seamlessly into one rather than two separate components.
