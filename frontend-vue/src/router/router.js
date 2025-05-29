import { createWebHistory, createRouter } from "vue-router";
import LandingPage from "../pages/LandingPage.vue";
import LoginPage from "../pages/LoginRegisterPage.vue";
import DataRegisterPage from "../pages/DataRegisterPage.vue";
import MentorHomePage from "../pages/MentorHomePage.vue";
import StudentHomePage from "../pages/StudentHomePage.vue";
import ErrorPage from "../pages/ErrorPage.vue";
import { useAuth } from "../composables/useAuth";
import MentorieDetailPage from "../pages/MentorieDetailPage.vue";
import MentorieEnrollPage from "../pages/MentorieEnrollPage.vue";
import ProblemDetailPage from "../pages/ProblemDetailPage.vue";
import MentorRevisionPage from "../pages/MentorRevisionPage.vue";

const routes = [
  { path: "/", component: LandingPage },
  { path: "/error", component: ErrorPage },
  { path: "/login", component: LoginPage, meta: { guestOnly: true } },
  { path: "/register", component: DataRegisterPage},
  {
    path: "/home/mentor/:id",
    component: MentorHomePage,
    props: true,
    meta: { requiresAuth: true, role: "mentor" },
  },
  {
    path: "/home/student/:id",
    component: StudentHomePage,
    props: true,
    meta: { requiresAuth: true, role: "student" },
  },
  {
    path: "/home/mentor/:id/mentories/:id_mentorie",
    component: MentorieDetailPage,
    props: true,
    meta: { requiresAuth: true, role: "mentor" },
  },
  {
    path: "/home/student/:id/mentories/:id_mentorie",
    component: MentorieEnrollPage,
    props: true,
    meta: { requiresAuth: true, role: "student" },
  },
  {
    path: "/home/student/:id/mentories/:id_mentorie/problems/:id_problem",
    component: ProblemDetailPage,
    props: true,
    meta: { requiresAuth: true, role: "student" },
  },
  {
    path: "/home/mentor/:id/mentories/:id_mentorie/solutions/:id_solution",
    component: MentorRevisionPage,
    props: true,
    meta: { requiresAuth: true, role: "mentor" },
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

router.beforeEach(async (to, from, next) => {
  const { fetchUser, isLogged, userData, justRegistered } = useAuth();

  if (!isLogged.value) {
    await fetchUser();
  }

  const isAuth = isLogged.value;
  const role = userData.value?.role;
  const realUserId = userData.value?.data?.user_id;

  if (to.meta.requiresAuth) {
    if (!isAuth) return next("/login");
    if (to.meta.role && role !== to.meta.role) return next("/error");
    if (to.params.id && to.params.id !== String(realUserId)) {
      if (role === "mentor") return next(`/home/mentor/${realUserId}`);
      if (role === "student") return next(`/home/student/${realUserId}`);
    }
  }

  // if (to.meta.guestOnly && isAuth) {
  //   if (role === "mentor") return next(`/home/mentor/${realUserId}`);
  //   if (role === "student") return next(`/home/student/${realUserId}`);
  //   return next("/error");
  // }

  if (to.meta.needsJustRegistered && !justRegistered.value) {
    return next("/login");
  }

  next();
});

export default router;
