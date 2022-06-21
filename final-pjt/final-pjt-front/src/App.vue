<template>
  <div>
    <div id="app">
      <b-navbar id="nav" class="d-flex justify-content-between" type="dark" toggleable="lg">
        <div>
          <b-navbar-brand router-link :to="{ name: 'home' }"><img src="https://stickershop.line-scdn.net/stickershop/v1/product/8730/LINEStorePC/main.png;compress=true" style="width: 70px; height: 70px;">
          <img src="./assets/bonovie_sm.png" style="width: 120px;">
          </b-navbar-brand>
        </div>
        <div>
          <b-navbar-toggle target="nav-collapse" right></b-navbar-toggle>
          <b-collapse id="nav-collapse" is-nav>
            <b-navbar-nav class="nav-item ">
              <b-nav-item router-link to="/recommended"><i class="fa-solid fa-video fs-3" style="color: white;"></i></b-nav-item>
              <b-nav-item router-link v-if="!isLoggedIn" to="/login" class="fs-5" style="color: white;">Login</b-nav-item>
              <b-nav-item router-link v-if="isLoggedIn" :to="{ name: 'logout' }" class="fs-5" style="color: white;">Logout</b-nav-item>
              <b-nav-item router-link v-if="!isLoggedIn" to="/signup" class="fs-5">회원가입</b-nav-item>
              <b-nav-item router-link v-if="isLoggedIn" :to="{ name: 'ProfileView', params: { username } }" class="fs-5">{{ currentUser.username }}님</b-nav-item>
            </b-navbar-nav>
          </b-collapse>
        </div>
      </b-navbar>
    <router-view/>
    </div>
      <footer class="fixed-bottom d-flex justify-content-end">
        <a href="#nav">
          <i class="fa-solid fa-circle-up mx-3 display-5"></i>
        </a>
      </footer>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'

export default {
  computed: {
    ...mapGetters(['isLoggedIn','currentUser']),
    username() {
      return this.currentUser.username ? this.currentUser.username : this.fetchCurrentUser()
    },
  },
  methods: {
    ...mapActions(['fetchCurrentUser'])
  }
}
</script>



<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  background-color: black;
}

nav {
  padding: 30px;
  text-align: end;
}

nav div img {
  width: 50px;
  height: 50px;
}

nav a {
  font-weight: bold;
  color: #eff4f8;
  text-decoration-line: none;
  margin-right: 20px;
}

nav a.router-link-exact-active {
  color: skyblue;
}

footer {
  background-color: black;
}

.nav-item :hover {
  cursor: pointer;
  transform: scale(1.1);
  transition: 200ms ease-in;
}

.fa-circle-up :hover {
  cursor: pointer;
}

router-link {
  color: white;
}
</style>
