<template>
  <div class="container my-5">
    <h1 class="text-info fw-bold">보노보노의 영화 추천</h1>
    <div class="row row-cols-auto">
    <RecMovieListItem 
    v-for="movie in reclist"
    :key="movie.pk"
    :movie="movie"
    />
    </div>
  </div>
</template>

<script>
import RecMovieListItem from '@/components/recomended/RecMovieListItem'
import { mapGetters,mapActions } from 'vuex'

  export default {
    data() {
      return {
        newlist: []
      }
    },
    components: {
      RecMovieListItem
    },
    computed: {
      ...mapGetters(['reclist','currentUser'])
    },
    methods: {
      ...mapActions(['recMovies']),
    },
    created() {
      this.recMovies()
    },
  }
</script>
