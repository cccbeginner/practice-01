import { createRouter, createWebHistory } from 'vue-router';
import LoginPage from './views/LoginPage.vue';
import RegisterPage from './views/RegisterPage.vue';
import ProfilePage from './views/ProfilePage.vue';
import UpdatePage from './views/UpdatePage.vue';

function isLoggedIn(){
    const token = localStorage.getItem('token');
    if(token) return true;
    else return false;
}

const routes = [
  {
    path: '/',
    component: isLoggedIn() ? ProfilePage : LoginPage,
  },
  { path: '/register', component: isLoggedIn() ? null : RegisterPage },
  //{ path: '/profile', component: isLoggedIn() ? ProfilePage : null },
  { path: '/update', component: isLoggedIn() ? UpdatePage : null },
];

const router = createRouter({
    history: createWebHistory(),
    routes,
  });

export default router;