function insertvalue(text) {
  // console.log(text)
  resulting = text['result']
  // console.log(resulting)
  document.getElementById("user-input").value = resulting;
  document.getElementById("submit_button").click();
}

function handleSubmitButton() {
  fetch('/form')
    .then((response) => response.json())
    .then((data) => insertvalue(data));
}

document.addEventListener("DOMContentLoaded", function () {
  // This is called after the browser has loaded the web page
  document.getElementById("submit_button").addEventListener("click", handleSubmitButton());
});
