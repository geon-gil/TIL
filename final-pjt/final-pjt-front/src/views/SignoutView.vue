<template>
  <div>
    <h1>회원탈퇴</h1>
  </div>
</template>

<script>
  import { mapActions, mapGetters } from 'vuex'

  export default {
    methods: {
      ...mapActions(['signout'])
    },
    computed: {
      ...mapGetters(['isLoggedIn'])
    },
    created() {
      if (this.isLoggedIn) {
        this.signout()
      } else {
        alert('잘못된 접근')
        this.$router.back()
      }
    },
  }
</script>
