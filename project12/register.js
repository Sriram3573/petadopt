document.getElementById("register-form").addEventListener("submit", (e) => {
    e.preventDefault();
  
    const username = document.getElementById("reg-username").value.trim();
    const email = document.getElementById("email").value.trim();
    const password = document.getElementById("reg-password").value.trim();
    const confirmPassword = document.getElementById("confirm-password").value.trim();
  
    if (!username || !email || !password || !confirmPassword) {
      alert("Please fill in all fields.");
      return;
    }
  
    if (password !== confirmPassword) {
      alert("Passwords do not match.");
      return;
    }
  
    alert(`Registration successful! Welcome, ${username}. Redirecting to the Login page...`);
    window.location.href = "index.html"; // Redirect to Login Page
  });
  