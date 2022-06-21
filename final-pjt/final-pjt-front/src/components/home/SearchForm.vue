<template>
  <div class="d-flex justify-content-between">
    <input type="text"
    class="form-control"
    v-model.trim="searchinput"
    @keyup.enter="setresult"
    style="color: black;"
    >
    <button 
    class="btn btn-primary"
    @click="setresult"
    >Search</button>
  </div>
</template>
<script>
export default {
  data(){
    return {
      searchinput: ''
    }
  },
  methods: {
    setresult() {
      if (this.searchinput){
        this.$router.push({name: 'SearchView' , params: {search: this.searchinput}})
        this.$router.go({name: 'SearchView'})
      }
    }
  },
}
</script>
