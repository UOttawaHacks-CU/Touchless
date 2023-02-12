let page;

function insertvalue(text) {
  // console.log(text)
  resulting = text["result"];
  // console.log(resulting)
  document.getElementById("user-input").value = resulting;
  document.getElementById("submit_button").click();
}

function handleSubmitButton() {
  page++;
  fetch("/form")
    .then((response) => response.json())
    .then((data) => insertvalue(data));
  location.replace("127.0.0.1:5000/index" + page);
}

document.addEventListener("DOMContentLoaded", function () {
  // This is called after the browser has loaded the web page
  page = 0;
  document
    .getElementById("submit_button")
    .addEventListener("click", handleSubmitButton());
});
