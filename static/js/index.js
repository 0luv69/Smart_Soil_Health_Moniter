const formOpenBtnLogin = document.querySelector("#form-open-login"),
  formOpenBtnSignup = document.querySelector("#form-open-signup"),
  home = document.querySelector(".home"),
  formContainer = document.querySelector(".form_container"),
  formCloseBtn = document.querySelector(".form_close"),
  signupBtn = document.querySelector("#signup"),
  loginBtn = document.querySelector("#login"),
  pwShowHide = document.querySelectorAll(".pw_hide"),
  mainPageSignupBtn = document.querySelector(".btn");

  const popupState = localStorage.getItem('popupState');


if (popupState === 'login') {
  home.classList.add("show");
  formContainer.classList.remove("active")
} 
else if (popupState === 'signup') {
  home.classList.add("show");
  formContainer.classList.add("active");
}


formOpenBtnLogin.addEventListener("click", () => {
  home.classList.add("show");
  formContainer.classList.remove("active");
  localStorage.setItem('popupState', 'login');

});

formOpenBtnSignup.addEventListener("click", () => {
  home.classList.add("show");
  formContainer.classList.add("active");
  localStorage.setItem('popupState', 'signup');
});

mainPageSignupBtn.addEventListener("click", () => { // Add this block
  home.classList.add("show");
  formContainer.classList.add("active");
});

formCloseBtn.addEventListener("click", () => {
  localStorage.setItem('popupState', 'none');
home.classList.remove("show")});

pwShowHide.forEach((icon) => {
  icon.addEventListener("click", () => {
    let getPwInput = icon.parentElement.querySelector("input");
    if (getPwInput.type === "password") {
      getPwInput.type = "text";
      icon.classList.replace("uil-eye-slash", "uil-eye");
    } else {
      getPwInput.type = "password";
      icon.classList.replace("uil-eye", "uil-eye-slash");
    }
  });
});

signupBtn.addEventListener("click", (e) => {
  e.preventDefault();
  formContainer.classList.add("active");
});

loginBtn.addEventListener("click", (e) => {
  e.preventDefault();
  formContainer.classList.remove("active");
});

  // Event listener for main page signup button
  mainPageSignupBtn.addEventListener("click", () => {
    home.classList.add("show");
    formContainer.classList.add("active");
  });

  // Event listeners for password show/hide icons
  pwShowHide.forEach((icon) => {
    icon.addEventListener("click", () => {
      let getPwInput = icon.parentElement.querySelector("input");
      if (getPwInput.type === "password") {
        getPwInput.type = "text";
        icon.classList.replace("uil-eye-slash", "uil-eye");
      } else {
        getPwInput.type = "password";
        icon.classList.replace("uil-eye", "uil-eye-slash");
      }
    });
  });

  // Event listener for signup button
  signupBtn.addEventListener("click", (e) => {
    e.preventDefault();
    if (validatePassword()) {
      formContainer.classList.add("active");
    }
  });

  // Event listener for login button
  loginBtn.addEventListener("click", (e) => {
    e.preventDefault();
    formContainer.classList.remove("active");
  });

  // Event listener for form close button
  formCloseBtn.addEventListener("click", () => home.classList.remove("show"));



