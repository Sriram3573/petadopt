
document.querySelector("form").addEventListener("submit", (e) => {
  e.preventDefault();

  // Collect form values
  const name = document.getElementById("full-name").value.trim();
  const email = document.getElementById("email").value.trim();
  const phone = document.getElementById("phone").value.trim();
  const message = document.getElementById("message").value.trim();

  // Form validation
  if (!name || !email || !phone || !message) {
    alert("Please fill out all required fields!");
    return;
  }

  if (!/^\S+@\S+\.\S+$/.test(email)) {
    alert("Please enter a valid email address.");
    return;
  }

  // EmailJS Integration
  emailjs.init("YOUR_PUBLIC_KEY"); // Replace with your EmailJS public key

  const serviceID = "YOUR_SERVICE_ID"; // Replace with your EmailJS service ID
  const templateID = "YOUR_TEMPLATE_ID"; // Replace with your EmailJS template ID

  const templateParams = {
    name: name,
    email: email,
    phone: phone,
    message: message,
  };

  emailjs.send(serviceID, templateID, templateParams)
    .then(response => {
      alert("Email sent successfully! Thank you for reaching out.");
    })
    .catch(error => {
      alert("Failed to send email. Please try again later.");
      console.error("EmailJS error: ", error);
    });
});
