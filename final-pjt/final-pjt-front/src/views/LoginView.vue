<template>
  <div class="container">
    <h1 class="text-light">Login</h1>
    <div class="row d-flex justify-content-center">
      <form @submit.prevent="login(credentials)" class="col-6">
        <hr>
        <account-error-list v-if="authError"></account-error-list>
        <div class="my-5 d-flex">
          <label for="username" class="text-light mx-3 fs-3">username: </label>
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
          <label for="password" class="text-light mx-3 fs-3">password: </label>
          <input 
            class="form-control" 
            v-model="credentials.password" 
            type="password" 
            id="password" 
            required 
            style="color: black; font-size:25px;"
          />
        </div>
        <hr>
        <button class="btn btn-primary my-5">Login</button>
      </form>

    </div>
    
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
import AccountErrorList from '@/components/account/AccountErrorList.vue'

export default {
  name: 'LoginView',
  components: {
    AccountErrorList,
  },
  data() {
    return {
      credentials: {
        username: '',
        password: '',
      }
    }
  },
  computed: {
    ...mapGetters(['authError'])
  },
  methods: {
    ...mapActions(['login'])
  },
}
</script>
