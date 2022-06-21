import router from '@/router'
import axios from 'axios'
import drf from '@/api/drf'
import _ from 'lodash'

export default {

  state: {
    movies: [],
    movie: {},
    searchinput:'',
    searchlist: [],
    reclist: [],
    reviews: [null],
    review: {},
    score: 0,
  },
  getters: {
    movies: state => state.movies,
    movie: state => state.movie,
    isAuthor: (state, getters) => {
      return state.movie.user?.username === getters.currentUser.username
    },
    isMovie: state => !_.isEmpty(state.movie),
    isReview: state => !_.isEmpty(state.review),
    searchinput: state => state.searchinput,
    searchlist: state => state.searchlist,
    reclist: state => state.reclist,
    reviews: state => state.reviews,
    review: state => state.review,
    
    score: state => state.score,
  },
  mutations: {
    SET_MOVIES: (state, movies) => state.movies = movies,
    SET_MOVIE: (state, movie) => state.movie = movie,
    SET_INPUT: (state, searchinput) => state.searchinput = searchinput,
    SET_RESULT: (state, searchlist) => state.searchlist = searchlist,
    SET_RECOMMEND: (state, reclist) => state.reclist = reclist,
    SET_MOVIE_REVIEWS: (state, reviews) => (state.movie.reviews = reviews),
    SET_REVIEWS: (state, review) => (state.review = review),
    SET_REVIEW_COMMENTS: (state, comments) => (state.review.comment_set = comments),

    SET_RATING: (state, score) => (state.score = score),
  },
  actions: {
    fetchMovies({ commit ,getters}, limit) {

      axios({
        url: drf.movies.list(limit),
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res => commit('SET_MOVIES', res.data))
        .catch(err => console.error(err.response))
    },
    fetchMovie({ commit, getters }, movie_id) {

      axios({
        url: drf.movies.detail(movie_id),
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res => commit('SET_MOVIE', res.data))
        .catch(err => {
          console.error(err.response)
          if (err.response.status === 404) {
            router.push({ name: 'NotFound404' })
          }
        })
    },
    searchMovies({ commit, getters }, search) {
      axios({
        url: drf.movies.search(search),
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res => commit('SET_RESULT', res.data))
        .catch(err => {
          console.error(err.response)
          if (err.response.status === 404) {
            router.push({ name: 'NotFound404' })
          }
        })
    },
    recMovies({commit, getters}){

      axios({
        url: drf.movies.recommended(),
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res => commit('SET_RECOMMEND', res.data))
        .catch(err => {
          console.error(err.response)
          if (err.response.status === 404) {
            router.push({ name: 'NotFound404' })
          }
        })
    },

    ratingMovie({commit, getters}, {moviePk, score}){

      axios({
        url: drf.movies.rating_movie(moviePk),
        method: 'post',
        data: { score },
        headers: getters.authHeader,
      })
      .then(res => commit('SET_RATING', res.data))
        router.go({ name: 'DetailView' })
      .catch(err => {
        console.error(err.response)
        if (err.response.status === 404) {
          router.push({ name: 'NotFound404' })
        }
      })
    },

    createReview({ commit, getters }, { moviePk, title ,content }) {
      const review = { title, content }

      axios({
        url: drf.movies.reviews(moviePk),
        method: 'post',
        data: review,
        headers: getters.authHeader,
      })
        .then(res => {
          commit('SET_MOVIE_REVIEWS', res.data)
        })
        .catch(err => console.error(err.response))
    },

    fetchReviews({ commit, getters}, { moviePk, reviewPk }) {

      axios({
        url: drf.movies.review_update_delete(moviePk, reviewPk),
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res => commit('SET_REVIEWS', res.data))
        .catch(err => console.error(err.response))
    },

    updateReview({ commit, getters }, { moviePk, reviewPk, title, content }) {

      axios({
        url: drf.movies.review_update_delete(moviePk, reviewPk),
        method: 'put',
        data: { title, content },
        headers: getters.authHeader,
      })
        .then(res => {
          commit('SET_MOVIE_REVIEWS', res.data)
          router.go({ name: 'DetailView' })
        })
        .catch(err => console.error(err.response))
    },

    deleteReview({ commit, getters }, { moviePk, reviewPk }) {
        if (confirm('정말 삭제하시겠습니까?')) {
          axios({
            url: drf.movies.review_update_delete(moviePk, reviewPk),
            method: 'delete',
            data: {},
            headers: getters.authHeader,
          })
            .then(res => {
              commit('SET_MOVIE_REVIEWS', res.data)
              router.go({ name: 'DetailView' })
            })
            .catch(err => console.error(err.response))
        }
    },
    
    likeMovie({ commit, getters }, moviePk) {
      axios({
        url: drf.movies.movie_like(moviePk),
        method: 'post',
        headers: getters.authHeader,
      })
        .then(res => commit('SET_MOVIE', res.data))
        .catch(err => console.error(err.response))
    },
    
    createComment({ commit, getters }, { reviewPk, content }) {

      const comment = { content }

      axios({
        url: drf.movies.comments(reviewPk),
        method: 'post',
        data: comment,
        headers: getters.authHeader,
      })
        .then(res => {
          commit('SET_REVIEW_COMMENTS', res.data)
        })
        .catch(err => console.error(err.response))
    },

    updateComment({ commit, getters }, { reviewPk, commentPk, content }) {
      const comment = { content }

      axios({
        url: drf.movies.comment_update_or_delete(reviewPk, commentPk),
        method: 'put',
        data: comment,
        headers: getters.authHeader,
      })
        .then(res => {
          commit('SET_REVIEW_COMMENTS', res.data)
        })
        .catch(err => console.error(err.response))
    },

    deleteComment({ commit, getters }, { reviewPk, commentPk }) {
      if (confirm('정말 삭제하시겠습니까?')) {
        axios({
          url: drf.movies.comment_update_or_delete(reviewPk, commentPk),
          method: 'delete',
          data: {},
          headers: getters.authHeader,
        })
          .then(res => {
            commit('SET_REVIEW_COMMENTS', res.data)
            router.go({name: 'ReviewView'})
          })
          .catch(err => console.error(err.response))
      }
    },
    likeReview({ commit, getters }, reviewPk) {
      axios({
        url: drf.movies.review_like(reviewPk),
        method: 'post',
        headers: getters.authHeader,
      })
        .then(res => commit('SET_REVIEWS', res.data))
        .catch(err => console.error(err.response))
    },
    unLikeReview({ commit, getters }, reviewPk) {
      axios({
        url: drf.movies.review_unlike(reviewPk),
        method: 'post',
        headers: getters.authHeader,
      })
        .then(res => commit('SET_REVIEWS', res.data))
        .catch(err => console.error(err.response))
    },
  }
}

