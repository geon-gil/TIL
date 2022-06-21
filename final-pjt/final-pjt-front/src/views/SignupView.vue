<template>
  <div class="container">
    <h1 class="text-light">Signup</h1>
    <div class="row d-flex justify-content-center">
      <hr>
      <account-error-list v-if="authError"></account-error-list>
      <form @submit.prevent="signup(credentials)" class="col-6">
        <div class="my-5 d-flex">
          <label for="username" class="text-light col-3 fs-4">아이디:</label>
          <input 
            class="form-control"  
            v-model="credentials.username" 
            type="text" 
            id="username" 
            required 
            style="color: black; font-size:25px;"
          />
        </div>
        <hr>
        <div class="my-5 d-flex">
          <label for="password1" class="text-light col-3 fs-4">패스워드:</label>
          <input 
            class="form-control"
            v-model="credentials.password1" 
            type="password" 
            id="password1" 
            required style="color: black; font-size:25px;"
          />
        </div>
        <hr>
        <div class="my-5 d-flex">
          <label for="password2" class="text-light col-3 fs-4">패스워드 확인:</label>
          <input 
            class="form-control" 
            v-model="credentials.password2" 
            type="password" 
            id="password2" 
            required 
            style="color: black; font-size:25px;"
          />
        </div>
        <hr>
        <div class="my-5">
          <button class="btn btn-primary my-5">Signup</button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
import AccountErrorList from '@/components/account/AccountErrorList.vue'

export default {
  name: 'SignupView',
  components: {
    AccountErrorList,
  },
  data() {
    return {
      credentials: {
        username: '',
        password1: '',
        password2: '',
      }
    }
  },
  computed: {
    ...mapGetters(['authError'])
  },
  methods: {
    ...mapActions(['signup'])
  },
}
</script>

