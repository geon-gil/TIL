<template>
  <div class="container my-5">
    <SearchForm />
    <h1 class="text-info my-5">{{ this.$route.params.search }} 검색결과</h1>
    <div class="row row-cols-auto">
      <SearchResultListItem 
      v-for="movie in searchlist"
      :key="movie.id"
      :movie="movie"
      />
    </div>
    <div v-if="!searchlist">
      <h2 class="text-danger" >검색 결과가 없습니다</h2>
      <img src="../assets/bonobono.jpg" style="width: 500px; height: 500px;">
    </div>
  </div>
</template>

<script>
import SearchForm from '@/components/home/SearchForm'
import SearchResultListItem from '@/components/home/SearchResultListItem'
import { mapGetters,mapActions } from 'vuex'
export default {
  components: {
    SearchResultListItem,
    SearchForm
  },
  computed: {
    ...mapGetters(['searchlist'])
  },
  methods: {
    ...mapActions(['searchMovies']),
  },
  created() {
    this.searchMovies(this.$route.params.search)
  },
}
</script>
