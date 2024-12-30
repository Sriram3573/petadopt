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
