<template>
  <div>
    <comment-list-form></comment-list-form>
    
    <ul class="m-0 p-0">
      <comment-list-item 
        v-for="comment in comments" 
        :comment="comment" 
        :key="comment.id">
      </comment-list-item>        
    </ul>

  </div>
</template>

<script>
import CommentListItem from '@/components/detail/CommentListItem.vue'
import CommentListForm from '@/components/detail/CommentListForm.vue'


export default {
  name: 'CommentList',
  components: { CommentListForm, CommentListItem },
  props: { 
    comments: {
      type: [Array, Object, String] 
    }, 
  },
}
</script>

