<template>
  <div class="review-list">
    <li class="review-list-item list-group-item m-0 p-0" style="background-color: black;">
      <div class="form-control">
        <div>
          작성자:
          <router-link class="text-decoration-none" :to="{ name: 'ProfileView', params: { username: review.user.username } }">
            {{ review.user.username }}        
          </router-link>
        </div>
        <div>
          제목 :
          <router-link class="text-decoration-none" :to="{ name: 'ReviewView', params: { moviePk: review.movie ,reviewPk: review.pk } }">{{ payload.title }}</router-link> 
        </div>
        <div>
          <p v-if="!isEditing">{{ payload.content }}</p>
        </div>

        <span v-if="isEditing">
          <div class="input-group mb-3">
            <span class="input-group-text" id="inputGroup-sizing-default">title</span>
            <input 
              type="text" 
              class="form-control" 
              aria-label="Sizing example input" 
              aria-describedby="inputGroup-sizing-default"
              v-model="payload.title"
              style="color: white;"
              >
          </div>
          <div class="input-group mb-3">
            <span class="input-group-text" id="inputGroup-sizing-default">content</span>
            <input 
              type="text" 
              class="form-control" 
              aria-label="Sizing example input" 
              aria-describedby="inputGroup-sizing-default" 
              v-model="payload.content"
              style="color: white;"
              >
          </div>
          <span @click="onUpdate"><i class="fa-regular fa-pen-to-square"></i></span>   |
          <span @click="switchIsEditing"><i class="fa-regular fa-xmark"></i></span>
        </span>
        <span v-if="currentUser.username === review.user.username && !isEditing">
          <span @click="switchIsEditing"><i class="fa-regular fa-pen-to-square"></i></span>   |
          <span @click="deleteReview({moviePk: payload.moviePk, reviewPk: payload.reviewPk})"><i class="fa-regular fa-trash-can"></i></span>
        </span>
      </div>
    </li>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'ReviewListItem',
  props: { 
    review: {
      type: Object, 
    },
  },
  data() {
    return {
      isEditing: false,
      payload: {
        moviePk: this.review.movie,
        reviewPk: this.review.pk,
        title: this.review.title,
        content: this.review.content,
      },
    }
  },
  computed: {
    ...mapGetters(['currentUser']),
  },
  methods: {
    ...mapActions(['updateReview', 'deleteReview']),
    switchIsEditing() {
      this.isEditing = !this.isEditing
    },
    onUpdate() {
      this.updateReview(this.payload)
      this.isEditing = false
    }
  },
  created() {
    // console.log(this.review)
  },
} 
</script>

<style scoped>
.comment-list-item {
  border: 1px solid green;

}

.form-control {
  background-color: black !important;
  color: white;
}

.fa-pen-to-square {
  color: white;
}

.fa-trash-can {
  color: white;
}

.fa-xmark {
  color: white;
}

</style>
