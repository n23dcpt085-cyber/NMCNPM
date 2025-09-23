document.getElementById("loginForm").addEventListener("submit", function(event) {
  event.preventDefault(); // chặn reload trang

  const username = document.getElementById("username").value.trim();
  const password = document.getElementById("password").value.trim();
  const message = document.getElementById("message");

  if (username === "" || password === "") {
    message.textContent = "Please enter both username and password!";
    return;
  }

  if (username === "admin" && password === "123456") {
    message.style.color = "green";
    message.textContent = "Login successful!";
  } else {
    message.style.color = "red";
    message.textContent = "Invalid username or password!";
  }
});
