<template>
<div class="card-component">
  <div class="container">
    <div class="d-flex justify-content-between">
    <h1 class="text-start text-light my-3">{{ profile.username }} 님</h1>
    <router-link :to="{ name: 'SignoutView' }"><button class="btn btn-danger">회원탈퇴</button></router-link>
    </div>
    <hr>
    <h2 class="text-start text-light my-5">작성한 글</h2>
    
    <ul>
      
      <li v-for="review in profile.review_set" :key="review.id">
        <div class="d-flex justify-content-between"> 
        <div>
          <h3 class="text-start text-light">{{ review.title }}</h3>
          <p class="text-start text-light">{{ review.content }}</p>
        </div>
        <div class="text-end">
          <router-link :to="{ name: 'ReviewView', params: { moviePk:review.movie ,reviewPk: review.id } }">
            <img src="../assets/detail.png" style="width: 80px; height: 50px;">
            <p class="text-info">이동하기</p>
          </router-link>
        </div>
        </div>
        <hr>
      </li>
    </ul>
    <hr>
    <h2 class="text-start text-light mt-5">찜목록</h2>
        <div class="row row-cols-auto my-5">
          <div v-for="movie in profile.like_movies" :key="movie.id">
            <MovieListItem 
            :movie="movie"
            />
          </div>
        </div>
  </div>
</div>

</template>

<script>
import MovieListItem from '@/components/home/MovieListItem'
import { mapGetters, mapActions } from 'vuex'


export default {
  name: 'ProfileView',
  components: {
    MovieListItem
  },
  computed: {
    ...mapGetters(['profile'])
  },
  methods: {
    ...mapActions(['fetchProfile']),
  },
  created() {
    const payload = { username: this.$route.params.username }
    this.fetchProfile(payload)
  },
}
</script>

<style scoped>
div {
  background-color: black;
  /* color: white; */
}
li a {
  text-decoration-line: none;
}
ul {
  list-style:none;
}
img {
  width: 8rem;
}

.text-end :hover{
  cursor: pointer;
  transform: scale(1.1);
  transition: 300ms ease-in;
}
</style>
