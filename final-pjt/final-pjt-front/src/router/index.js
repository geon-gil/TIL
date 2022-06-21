import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '@/views/HomeView'
import LoginView from '@/views/LoginView'
import RecommendedView from '@/views/RecommendedView'
import SignupView from '@/views/SignupView'
import ProfileView from '@/views/ProfileView'
import SearchView from '@/views/SearchView'
import DetailView from '@/views/DetailView'
import LogoutView from '@/views/LogoutView'
import SignoutView from '@/views/SignoutView'
import ReviewView from '@/views/ReviewView'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/login',
    name: 'LoginView',
    component: LoginView
  },
  {
    path: '/logout',
    name: 'logout',
    component: LogoutView
  },
  {
    path: '/recommended',
    name: 'RecommendedView',
    component: RecommendedView
  },
  {
    path: '/signup',
    name: 'SignupView',
    component: SignupView
  },
  {
    path: '/signout',
    name: 'SignoutView',
    component: SignoutView
  },
  {
    path: '/profile/:username',
    name: 'ProfileView',
    component: ProfileView,
  },
  {
    path: '/search/:search',
    name: 'SearchView',
    component: SearchView,
  },
  {
    path: '/detail/:movie_id',
    name: 'DetailView',
    component: DetailView,
  },
  {
    path: '/:moviePk/review/:reviewPk',
    name: 'ReviewView',
    component: ReviewView,
  },

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

router.beforeEach((to, from, next) => {
  const token = localStorage.getItem( 'token' )
  if(to.name === 'LoginView') {
    if (token) {
      next({ name: 'home' })
    }
  }
  else if (to.name === 'home') {
    if (!token) {
      next({ name: 'LoginView' })
    }
  }
  else if (to.name === 'RecommendedView') {
    if (!token) {
      next({ name: 'LoginView' })
    }
  }
  next()
})
export default router
