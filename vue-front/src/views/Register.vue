<template>
  <div>
    <b-container>
      <register></register>
    </b-container> 
  </div>
</template>
  

<script lang="ts">
import { Component, Prop, Vue } from "vue-property-decorator";
import RegParent from "@/components/Register/RegParent.vue"

@Component({
  components: {"register": RegParent}
})
export default class BCView extends Vue {

}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
