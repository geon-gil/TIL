<template>
  <div>
    <li id="comment-item" class="mt-1">
      <div class="mt-3">
        <router-link class="text-decoration-none" :to="{ name: 'ProfileView', params: { username: comment.user.username } }">
          {{ comment.user.username }}
        </router-link>: 
        
        <span v-if="!isEditing" style="">{{ payload.content }}</span>

        <div v-if="isEditing" class="input-group mb-3">
          <input type="text" class="form-control d-flex col-4" v-model="payload.content" style="color: black !important;">
          <span @click="onUpdate" style="cursor: pointer; font-size: 30px;" class="m-1"><i class="fa-regular fa-pen-to-square"></i></span>
          <span @click="switchIsEditing" style="cursor: pointer; font-size: 30px;" class="m-1"><i class="fa-regular fa-xmark"></i></span>
        </div>

        <div class="">
          <span v-if="currentUser.username === comment.user.username && !isEditing">
            <span @click="switchIsEditing" style="cursor: pointer;"><i class="fa-regular fa-pen-to-square"></i></span> |
            <span @click.prevent="deleteComment(payload)" style="cursor: pointer;"><i class="fa-regular fa-trash-can"></i></span>
          </span>
        </div>
      </div>
    </li>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'CommentListItem',
  props: { 
    comment: {
      type: Object
    }
  },
  data() {
    return {
      isEditing: false,
      payload: {
        reviewPk: this.comment.review,
        commentPk: this.comment.id,
        content: this.comment.content
      },
    }
  },
  computed: {
    ...mapGetters(['currentUser']),
  },
  methods: {
    ...mapActions(['updateComment', 'deleteComment']),
    switchIsEditing() {
      this.isEditing = !this.isEditing
    },
    onUpdate() {
      this.updateComment(this.payload)
      this.isEditing = false
    }
  },
}
</script>

<style scoped>
#comment-item {
  background-color: rgba(173, 170, 170, 0.473);
  border-radius: 10px;
  overflow: hidden;
}
</style>
