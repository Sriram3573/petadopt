// Function to open popup
function openPopup() {
    document.getElementById('popup').style.display = 'block';
}

// Function to close popup
function closePopup() {
    document.getElementById('popup').style.display = 'none';
}

// Show popup when the page is loaded
window.onload = function() {
    if (document.getElementById('popup')) {
        openPopup();
    }
};

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