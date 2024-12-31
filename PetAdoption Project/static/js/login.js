document.getElementById("login-form").addEventListener("submit", (e) => {
    e.preventDefault();
  
    const username = document.getElementById("username").value.trim();
    const password = document.getElementById("password").value.trim();
  
    if (!username || !password) {
      alert("Please fill in all fields.");
      return;
    }
  
    alert(`Welcome back, ${username}! Redirecting to the Home page...`);
    window.location.href = "home.html"; 
  });
  