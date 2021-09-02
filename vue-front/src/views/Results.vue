<template>
  <div>
    <b-container>
      <results></results>
    </b-container> 
  </div>
</template>
  

<script lang="ts">
import { Component, Prop, Vue } from "vue-property-decorator";
import ResultsParent from "@/components/Results/results-parent.vue"

@Component({
  components: {"results": ResultsParent}
})
export default class BCView extends Vue {

}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
