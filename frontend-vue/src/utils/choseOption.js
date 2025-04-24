export const setOption = (option) => {
  const homeBtn = document.querySelector("#home-btn");
  const aboutBtn = document.querySelector("#about-btn");
  const servicesBtn = document.querySelector("#services-btn");
  const contactBtn = document.querySelector("#contact-btn");

  homeBtn.classList.remove("active");
  aboutBtn.classList.remove("active");
  servicesBtn.classList.remove("active");
  contactBtn.classList.remove("active");

  switch (option) {
    case "home":
      homeBtn.classList.add("active");
      break;
    case "about":
      aboutBtn.classList.add("active");
      break;
    case "services":
      servicesBtn.classList.add("active");
      break;
    case "contact":
      contactBtn.classList.add("active");
      break;
    default:
      break;
  }
};
