function showLogin() {
  document.getElementById("login-form").classList.add("active");
  document.getElementById("register-form").classList.remove("active");
}

function showRegister() {
  document.getElementById("login-form").classList.remove("active");
  document.getElementById("register-form").classList.add("active");
}

function validateEmail(email) {
  const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return re.test(String(email).toLowerCase());
}

document.getElementById("login").addEventListener("submit", function (e) {
  e.preventDefault();

  const email = document.getElementById("login-email").value;
  const password = document.getElementById("login-password").value;
  let isValid = true;

  if (!validateEmail(email)) {
    document.getElementById("login-email-error").innerText =
      "Invalid email address";
    document.getElementById("login-email-error").style.display = "block";
    isValid = false;
  } else {
    document.getElementById("login-email-error").style.display = "none";
  }

  if (password.length < 6) {
    document.getElementById("login-password-error").innerText =
      "Password must be at least 6 characters";
    document.getElementById("login-password-error").style.display = "block";
    isValid = false;
  } else {
    document.getElementById("login-password-error").style.display = "none";
  }

  if (isValid) {
    alert("Login successful");
  }
});

document.getElementById("register").addEventListener("submit", function (e) {
  e.preventDefault();

  const name = document.getElementById("register-name").value;
  const email = document.getElementById("register-email").value;
  const password = document.getElementById("register-password").value;
  let isValid = true;

  if (name.length < 3) {
    document.getElementById("register-name-error").innerText =
      "Name must be at least 3 characters";
    document.getElementById("register-name-error").style.display = "block";
    isValid = false;
  } else {
    document.getElementById("register-name-error").style.display = "none";
  }

  if (!validateEmail(email)) {
    document.getElementById("register-email-error").innerText =
      "Invalid email address";
    document.getElementById("register-email-error").style.display = "block";
    isValid = false;
  } else {
    document.getElementById("register-email-error").style.display = "none";
  }

  if (password.length < 6) {
    document.getElementById("register-password-error").innerText =
      "Password must be at least 6 characters";
    document.getElementById("register-password-error").style.display = "block";
    isValid = false;
  } else {
    document.getElementById("register-password-error").style.display = "none";
  }

  if (isValid) {
    alert("Registration successful");
  }
});
