<template>

  <form class="input-group my-3" @submit.prevent="onSubmit">
    <span class="input-group-text" id="basic-addon3">내용:</span>
    <input 
      type="text" 
      class="form-control" 
      id="comment" 
      aria-describedby="basic-addon3" 
      v-model="content" 
      required
      style="color: black;"
      >
    <button class="btn btn-primary">댓글작성</button>
  </form>
</template>




<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'CommentListForm',
  data() {
    return {
      content: ''
    }
  },
  computed: {
    ...mapGetters(['review']),
  },
  methods: {
    ...mapActions(['createComment']),
    onSubmit() {
      this.createComment({ reviewPk: this.review.pk, content: this.content, })
      this.content = ''
    }
  },
  created() {
  }
}
</script>

