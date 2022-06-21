<template>
  <div class=" d-flex justify-content-center mb-5">
    <div class="card row-6 ">
      <div class="card-body">
        <h5 class="card-title">{{ movie.title }}</h5>
        <img :src="`https://image.tmdb.org/t/p/w300${this.movie.poster_path}`" class="card-img-top img-fluid" alt="..." id="poster">
        <p class="mt-3 fs-2">title : {{ review.title }}</p>
        <p class="fs-2">content : {{ review.content }}</p>
      </div>
      <div class="card-text" v-if="isAuthor">
      </div>

      <!-- review like & unlike UI -->
      <div class="d-flex justify-content-end" >
        <div @click="likeReview(reviewPk)" class="m-2"><i class="fa-regular fa-thumbs-up"></i></div>
        <span class="m-2">{{ likeCount }} 명이 이 리뷰를 좋아합니다.</span>
      </div>
      <div class="d-flex justify-content-end">
        <span @click="unLikeReview(reviewPk)" class="m-2"><i class="fa-regular fa-thumbs-down"></i></span>
        <span class="m-2">{{ unLikeCount }} 명이 이 리뷰를 싫어합니다.</span>
      </div>
      <CommentList :comments="review.comment_set"></CommentList>
    </div>
  </div>
</template>

<script>
import CommentList from '@/components/detail/CommentList'
import { mapGetters } from 'vuex'
import { mapActions } from 'vuex'

export default {
name: 'ReviewView',
  components: { CommentList,},
  data() {
    return {
      reviewPk: this.$route.params.reviewPk,
      moviePk: this.$route.params.moviePk
    }
  },
  computed: {
    ...mapGetters(['isAuthor', 'movie', 'review']),
    likeCount() {
      return this.review.like_users?.length
    },
    unLikeCount() {
      return this.review.not_like_users?.length
    }
  },
  methods: {
    ...mapActions([
      'fetchMovie',
      'fetchReviews',
      'deleteReview',
      'likeReview',
      'unLikeReview',
    ])
  },
  created() {
    const payload = { moviePk: this.moviePk, reviewPk: this.reviewPk }
    
    this.fetchReviews(payload)
    this.fetchMovie(this.moviePk)

  },
}
</script>

<style scoped>

.card {
  background-color: black !important;
  color: white;
}

.card-body {
  background-color: black;
  color: white;
}

.fa-thumbs-down {
  cursor: pointer;
  color: red;
  font-size: 20px;
}

.fa-thumbs-up {
  cursor: pointer;
  color: blue;
  font-size: 20px;
}

.container {
  margin: 30px;
}
</style>
