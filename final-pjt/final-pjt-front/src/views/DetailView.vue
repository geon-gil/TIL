<template>
  <div id="Detail" class="container">
    <div class="row d-flex justify-content-center">
      <!-- moviedetail UI  -->
      <div class="mb-5 d-flex" >
        <img :src="`https://image.tmdb.org/t/p/w300${this.movie.poster_path}`" class="card-img-top img-fluid" alt="..." id="poster">
        <div class="card mx-1" >
          <div class="card-body" >
            <h2 id="movie-title" class="card-title d-flex">{{ movie.title }}</h2>
            <div
              v-if="movie.release_date"
              class="movie-release-date d-flex">
                개봉  :  {{ movie.release_date }}
            </div>          
            <div>
            <div class="d-flex">
              <i class="fa-solid fa-star"></i>
              <h3 id="vote-average">{{ movie.vote_average }}</h3>
            </div>
              <div class="d-flex text-bold">
                줄거리
              </div>
              <hr>
              <div
                v-if="movie.overview"
                class="movie-detail-overview-body">
                <p class="text-start">
                  {{ movie.overview }}  
                </p>
              </div>
              <div v-else
                class="movie-detail-overview-body">
                해당 영화는 줄거리가 제공되지 않습니다.
              </div>
            </div>
            <div class="movie-detail-lower">

              <!-- Like UI -->
              <div class="d-flex justify-content-end">
                <div>
                  <div @click="likeMovie(moviePk)">
                    <p v-if="this.movie.like_users.some(request => request === this.currentUser.pk)"  class="m-1"><i class="fa-solid fa-heart"></i></p>
                    <p v-else class="m-1"><i class="fa-regular fa-heart"></i></p>
                  </div>
                </div>
                <div class="m-1">{{ likeCount }}명이 이 영화를 좋아합니다.</div>
              </div>
              <hr>
              <div>
                회원평균점수 : {{ movie.user_rating }}
              </div>
              <div>
                {{ movie.rating_count }} 명이 참여하였습니다.
              </div>
              <div>
                <label for="rate">평점</label>
                <input v-model="num" id="rate" type="number" min="1" max="10" class="m-1" placeholder="'1'">
                <button class="btn btn-primary"  @click="inputNum">평가하기</button>
              </div>
            </div>    
          </div>
        </div>
        
      </div>

      <div id="movie-cast" class="text-white">
        <div id="directors"
          v-for="director in movie.directors"
          :key="director.pk"
          :director="director"
          class=""
        >
          <h4>감 독</h4>
          <div class="d-flex justify-content-center">
            <div>
              <div class="d-flex justify-content-center" style="margin: 20px; width: 150px; height: 150px; border-radius: 70%; overflow: hidden;">
                <img :src="`https://image.tmdb.org/t/p/w300${director.profile_path}`" alt="assets/default_profile.jpg" style="width: 100%; height: 100%; object-fit: cover;">
              </div>
              <h5 class="d-flex justify-content-center">{{ director.name }}</h5>
            </div>
          </div>
        <hr>
        </div>
        <h4>출연배우</h4>
        <div class="d-flex justify-content-center">
          <div
            v-for="actor in movie.actors"
            :key="actor.pk"
            :actor="actor"
            class=""
          >
            <div class="m-3">
              <div style="width: 150px; height: 150px; border-radius: 70%; overflow: hidden;">
                <img :src="`https://image.tmdb.org/t/p/w300${actor.profile_path}`" alt="assets/default_profile.jpg" style="width: 100%; height: 100%; object-fit: cover;">  
              </div>
              <div class="d-flex justify-content-center">{{ actor.name }}</div>
            </div>
          </div>
        </div>
      </div>
      <hr class="mb-5">
      

      <!-- Review UI -->
      <ReviewList :reviews="movie.reviews"></ReviewList>
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
import ReviewList from '@/components/detail/ReviewList.vue'

export default {
  name: 'DetailView',
  components: { ReviewList },
  data() {
    return {
      moviePk: this.$route.params.movie_id,
      num: null,
      flag: false,
    }
  },
  computed: {
    ...mapGetters(['isAuthor', 'movie', 'score', 'currentUser']),
    likeCount() {
      return this.movie.like_users?.length
    },
  },
  methods: {
    ...mapActions([
      'fetchMovie',
      'likeMovie',
      'ratingMovie',
    ]),
    inputNum() {
      this.ratingMovie({ moviePk: this.moviePk, score: this.num})
    },


  },
  created() {
    this.fetchMovie(this.moviePk)
  }
}
</script>

<style scoped>
#poster {
  width: 300px;
  height: auto;
  padding: 0;
}

#box {
    width: 150px;
    height: 150px; 
    border-radius: 70%;
    overflow: hidden;
}

#profile {
    width: 100%;
    height: 100%;
    object-fit: cover;
}


.fa-heart {
  color: red;
}

.fa-star {
  color: rgb(233, 217, 0);
  font-size: 23px;
  margin: 5px;
}

.card {
  background-color: black ;
  color: white;
}
</style>
