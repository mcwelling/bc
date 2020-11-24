<template>
  <div>
    <b-container>
      <web-services-demo></web-services-demo>
    </b-container> 
  </div>
</template>
  

<script lang="ts">
import { Component, Prop, Vue } from "vue-property-decorator";
import BlockParent from '@/components/polling/bc-parent.vue'

@Component({
  components: {"web-services-demo": BlockParent}
})
export default class BCView extends Vue {

}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
