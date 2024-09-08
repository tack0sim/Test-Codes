document.addEventListener("DOMContentLoaded", () => {
  const burger = document.querySelector(".burger");
  const burgerMenu = document.querySelector(".burger-menu");

  burger.addEventListener("click", (event) => {
    console.log(event);
    burgerMenu.classList.toggle("active");
  });
});
