import { createApp } from "vue";
import "./style.css";
import App from "./App.vue";
import router from "./router/router";
import AOS from "aos";
import "aos/dist/aos.css";

AOS.init({
  duration: 1000,
});
const app = createApp(App);
app.use(router);
app.mount("#app");
