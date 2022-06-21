<template>
  <div class="review-list mb-5 container">
    <div class="row d-flex justify-content-center">
      <review-list-form></review-list-form>
    </div>
    <div class="row  justify-content-center">
      <ul>
        <review-list-item 
          v-for="review in reviews" 
          :review="review" 
          :key="review.pk">
        </review-list-item>        
      </ul>
    </div>

  </div>
</template>

<script>
import ReviewListItem from '@/components/detail/ReviewListItem.vue'
import ReviewListForm from '@/components/detail/ReviewListForm.vue'
//import { mapGetters, mapActions } from 'vuex'


export default {
  name: 'ReviewList',
  components: { ReviewListForm, ReviewListItem },
  props: { 
    reviews:{
      type: Array, 
    },
  },
  computed: {
  // ...mapGetters(['movie']),
  },

  created() {
    // console.log(this.reviews)
  }
}
</script>

<style scoped>
.comment-list {
  border: 1px solid blue;
}

.review-list-item {
  background-color: black;
}

</style>
