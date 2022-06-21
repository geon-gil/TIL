<template>
  <div @click="moviedetail" class="col-2">
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
  methods:{
    moviedetail() {
      this.$router.push({name: 'DetailView',params: {movie_id: this.movie.pk}})
    }
  },
}
</script>

<style>
.card-img-top{
  height: 18rem;
  object-fit: cover;
}
</style>