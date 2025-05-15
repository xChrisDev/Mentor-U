import { createWebHistory, createRouter } from "vue-router";
import LandingPage from "../pages/LandingPage.vue";
import LoginPage from "../pages/LoginRegisterPage.vue";
import DataRegisterPage from "../pages/DataRegisterPage.vue";
import MentorHomePage from "../pages/MentorHomePage.vue";
import StudentHomePage from "../pages/StudentHomePage.vue";
import ErrorPage from '../pages/ErrorPage.vue'

const routes = [
  { path: "/", component: LandingPage },
  { path: "/error", component: ErrorPage },
  { path: "/login", component: LoginPage },
  { path: "/register", component: DataRegisterPage},
  { path: "/home/mentor", component: MentorHomePage},
  { path: "/home/student", component: StudentHomePage}
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
