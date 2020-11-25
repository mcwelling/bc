<template>
  <div>
    <b-container>
      <ballot-designer></ballot-designer>
    </b-container> 
  </div>
</template>
  

<script lang="ts">
import { Component, Prop, Vue } from "vue-property-decorator";
import PollingParent from "@/components/BallotDesigner/bd-parent.vue"

@Component({
  components: {"ballot-designer": PollingParent}
})
export default class BCView extends Vue {

}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
