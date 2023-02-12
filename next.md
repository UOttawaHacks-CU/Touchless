## Next Steps
- Fix pages to add questions in speechForm/static
- Update /website pages so there is one option for radio buttons with none of the above (done)
    - For these they need to be changed so if you have any symptoms then send to sick page
    - Only allow submission when one radio button has been selected
- Fix /gestures/customform so that at last page or sick page the page stays up but the camera is deconstructed

### Potential
- DB for data from form to be stored


## Updated
- Get speech to text data from each question and store it in a json object of the format:
    {
        "name":"",
        "medical history":""
    }
    - python to send a post request to a url with json data