document.querySelector("#contact-form").addEventListener("submit", function(e) {
  e.preventDefault();

  const name = document.getElementById("name").value.trim();
  const email = document.getElementById("email").value.trim();
  const message = document.getElementById("message").value.trim();

  if (!name || !email || !message) {
    alert("Please fill out all required fields!");
    return;
  }

  if (!/^\S+@\S+\.\S+$/.test(email)) {
    alert("Please enter a valid email address.");
    return;
  }

  emailjs.init("VC5uoc_rt7U3-gau-");

  const serviceID = "service_tfqmgxb";
  const templateID = "template_8yr6sec";

  const templateParams = {
    name: name,
    email: email,
    message: message,
  };

  emailjs.send(serviceID, templateID, templateParams)
    .then(function(response) {
      alert("Email sent successfully! Thank you for reaching out.");
    })
    .catch(function(error) {
      alert("Failed to send email. Please try again later.");
      console.error("EmailJS error: ", error);
    });
});
