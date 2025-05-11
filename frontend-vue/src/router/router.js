import { createWebHistory, createRouter } from "vue-router";
import LandingPage from "../pages/LandingPage.vue";

const routes = [{ path: "/", component: LandingPage }];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
