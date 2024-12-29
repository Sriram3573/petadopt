document.querySelector(".hero button").addEventListener("click", () => {
    window.location.href = "adopt.html"; // Redirect to Adopt Page
  });
  // Scroll to Top Button
const scrollToTopBtn = document.getElementById("scrollToTopBtn");

// Scroll to top when button is clicked
scrollToTopBtn.addEventListener("click", function () {
  window.scrollTo({
    top: 0,
    behavior: "smooth",
  });
});
