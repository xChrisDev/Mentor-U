import { createWebHistory, createRouter } from "vue-router";
import LandingPage from "../pages/LandingPage.vue";
import LoginPage from "../pages/LoginRegisterPage.vue";
import DataRegisterPage from "../pages/DataRegisterPage.vue";

const routes = [
  { path: "/", component: LandingPage },
  { path: "/login", component: LoginPage },
  { path: "/login/data", component: DataRegisterPage}
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
