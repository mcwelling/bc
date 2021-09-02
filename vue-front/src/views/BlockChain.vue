<template>
  <div>
    <b-container>
      <voting></voting>
    </b-container> 
  </div>
</template>
  

<script lang="ts">
import { Component, Prop, Vue } from "vue-property-decorator";
import VotingParent from "@/components/BlockChain/bc-parent.vue"

@Component({
  components: {"voting": VotingParent}
})
export default class BCView extends Vue {

}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
