const HOST = 'http://127.0.0.1:8000/api/v1/'

const ACCOUNTS = 'accounts/'
const MOVIES = 'movies/'
const COMMENTS = 'comment/'
const REVIEWS = 'review/'
export default {
  accounts: {
    login: () => HOST + ACCOUNTS + 'login/',
    logout: () => HOST + ACCOUNTS + 'logout/',
    signup: () => HOST + ACCOUNTS + 'signup/',
    signout: () => HOST + ACCOUNTS + 'signout/',
    // Token 으로 현재 user 판단
    currentUserInfo: () => HOST + ACCOUNTS + 'user/',
    // username으로 프로필 제공
    profile: username => HOST + ACCOUNTS + 'profile/' + `${username}/`,
  },
  movies: {
    list: limit => HOST + MOVIES + 'limit/' + `${limit}/`,
    detail: movie_id => HOST + MOVIES + `${movie_id}/`,
    movie_like: movie_id => HOST + MOVIES + `${movie_id}/` + 'like/',
    search: search => HOST + MOVIES + 'search/' + `${search}/`,
    reviews: movie_id => HOST + MOVIES + `${movie_id}/` + REVIEWS,
    comments: review_id => HOST + MOVIES + `${review_id}/` + COMMENTS,
    review_like: review_id => HOST + MOVIES + REVIEWS + `${review_id}/` + 'like/',
    review_unlike: review_id => HOST + MOVIES + REVIEWS + `${review_id}/` + 'unlike/',
    recommended:() => HOST + MOVIES + 'recommended/',
    review_update_delete:(movie_id, review_id) => HOST + MOVIES + `${movie_id}/` + REVIEWS + `${review_id}/`,
    comment_update_or_delete:(review_id, comment_id) => HOST + MOVIES + `${review_id}/` + COMMENTS + `${comment_id}/`,
    rating_movie: movie_id => HOST + MOVIES + `${movie_id}/` + 'rating/',
    rating_update_or_delete: (movie_id,rating_pk) => HOST + MOVIES + `${movie_id}/` + 'rating/' + `${rating_pk}/`
    // admin?
  }
}
