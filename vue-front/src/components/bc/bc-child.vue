<template>
  <div>
    <b-card title="Block">
      <!--<b-card-text> Details </b-card-text> -->
      <b-card-text>
        <b-container>
          <!-- ID -->
          <b-row class="my-1">
            <b-col sm="3" class="offset-sm-2 text-left">
              <label>ID:</label>
            </b-col>
            <b-col sm="6">
              <b-form-input
                size="sm"
                v-model="cardData.id"
                readonly
              ></b-form-input>
            </b-col>
          </b-row>
          <!-- ParentHash -->
          <b-row class="my-1">
            <b-col sm="3" class="offset-sm-2 text-left">
              <label>ParentHash:</label>
            </b-col>
            <b-col sm="6">
              <b-form-input size="sm" v-model="cardData.parenthash"></b-form-input>
            </b-col>
          </b-row>
          <!-- Data -->
          <b-row class="my-1">
            <b-col sm="3" class="offset-sm-2 text-left">
              <label>Data:</label>
            </b-col>
            <b-col sm="6">
              <b-form-input size="sm" v-model="cardData.data"></b-form-input>
            </b-col>
          </b-row>
          <!-- Nonce -->
          <b-row class="my-1">
            <b-col sm="3" class="offset-sm-2 text-left">
              <label>Title:</label>
            </b-col>
            <b-col sm="6">
              <b-form-input size="sm" v-model="cardData.nonce"></b-form-input>
            </b-col>
          </b-row>
          <!-- BlockHash -->
          <b-row class="my-1">
            <b-col sm="3" class="offset-sm-2 text-left">
              <label>Title:</label>
            </b-col>
            <b-col sm="6">
              <b-form-input size="sm" v-model="cardData.blockhash"></b-form-input>
            </b-col>
          </b-row>
          <b-row class="my-2">
            <b-col sm="2" class="offset-sm-2">
              <b-button
                :disabled="!cardDataChanged"
                variant="primary"
                size="sm"
                @click="updateClass()"
                >Update</b-button
              >
            </b-col>
          </b-row>
        </b-container>
      </b-card-text>
    </b-card>
  </div>
</template>
  

<script lang="ts">
import { Component, Prop, Emit, Watch, Vue } from "vue-property-decorator";
import { BlockData } from "./BlockData";

@Component
export default class EventsChild extends Vue {
  @Prop() private cardData!: BlockData;
  private cardDataChanged = false

  @Emit('update-class-info')
  updateClass() {
    this.cardDataChanged = false
    return this.cardData
  }

  @Watch('cardData', {immediate: false, deep: true})
  onCardDataChanged(){
      this.cardDataChanged = true
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>

