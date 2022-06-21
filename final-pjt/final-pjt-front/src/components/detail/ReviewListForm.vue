<template>
  <div class="row-6">
    <form @submit.prevent="onSubmit" class="review-list-form">
      <div class="input-group mb-3">
        <span class="input-group-text" id="basic-addon1">제목</span>
        <input 
          type="text" 
          class="form-control" 
          placeholder="리뷰 제목을 입력하세요." 
          aria-label="Title" 
          aria-describedby="basic-addon1" 
          v-model="title" 
          required 
          style="color: black !important;"
        >
      </div>
      <div class="input-group">
        <span class="input-group-text">내용</span>
        <textarea class="form-control" placeholder="내용을 입력하세요." aria-label="With textarea" v-model="content" required style="color: black !important;"></textarea>
      </div>
      <button class="btn btn-primary m-3">리뷰작성</button>
    </form>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'ReviewListForm',
  data() {
    return {
      title: '',
      content: ''
    }
  },
  props: {
    review: {
      type: Object,
    },
  },
  computed: {
    ...mapGetters(['movie']),
  },
  methods: {
    ...mapActions(['createReview']),
    onSubmit() {
      this.createReview({ moviePk: this.movie.id, title: this.title, content: this.content,})
      this.title = ''
      this.content = ''
    }
  },
  created() {

  }
}
</script>

<style scoped>
.comment-list-form {
  border: 1px solid black;
  margin: 1rem;
  padding: 1rem;
}

</style>
