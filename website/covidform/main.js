// To add functionality to the form, you can add JavaScript code.
// For example, to handle the form submit event and display an alert with the form data:

const form = document.querySelector('form');
form.addEventListener('submit', (event) => {
  event.preventDefault();
  const name = form.elements.name.value;
  const email = form.elements.email.value;
  const message = form.elements.message.value;
  alert(`Name: ${name}\nEmail: ${email}\nMessage: ${message}`);
});
