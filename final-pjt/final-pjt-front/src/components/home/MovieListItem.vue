<template>
  <div @click="moviedetail" class="movie-item">
    <div class="card mt-5" style="width: 12rem;">
      <img :src="`https://image.tmdb.org/t/p/w500${movie.poster_path}`" class="card-img-top " alt="...">
      <div class="card-body">
        <MarQuee class="card-title fw-bold">{{ movie.title }}</MarQuee>
        <MarQuee>장르 :
        <span v-for="genre in movie.genres"
        :key="genre.pk"
        :genre="genre"
        >{{ genre.name }} </span>
        </MarQuee>
        <p class="card-text text-end">평점: {{ movie.vote_average }}</p>
      </div>
    </div>
  </div>
</template>

<script>


export default {


  props: {
    movie: {
      type: Object
    }
  },
  computed: {

  },
  methods:{
    moviedetail() {
      this.$router.push({name: 'DetailView',params: {movie_id: this.movie.id}})
    },

  },

}
</script>

<style scoped>
.card-img-top{
  height: 18rem;
  object-fit: cover;
}

.movie-item :hover{
  cursor: pointer;
  transform: scale(1.1);
  transition: 50ms ease-in;
}
</style>