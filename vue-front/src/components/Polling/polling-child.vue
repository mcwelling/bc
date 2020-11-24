<template>
  <div>
    <b-card :title="'Option ' + cardData.id" bg-variant="secondary" text-variant="white">
      <!--<b-card-text> Details </b-card-text> -->
      <b-card-text>
        <b-container>
          <!-- ParentHash -->
          <b-row class="my-1">
            <b-col sm="3" class="offset-sm-2 text-left">
              <label>Parent Hash:</label>
            </b-col>
            <b-col sm="6">
              <b-form-input size="sm" v-model="cardData.parenthash" readonly></b-form-input>
            </b-col>
          </b-row>
          <!-- Data -->
          <b-row class="my-1">
            <b-col sm="3" class="offset-sm-2 text-left">
              <label>Data:</label>
            </b-col>
            <b-col sm="6">
              <b-form-textarea size="sm" v-model="cardData.data"></b-form-textarea>
            </b-col>
          </b-row>
          <!-- Nonce -->
          <b-row class="my-1">
            <b-col sm="3" class="offset-sm-2 text-left">
              <label>Nonce:</label>
            </b-col>
            <b-col sm="6">
              <b-form-input size="sm" v-model="cardData.nonce" readonly></b-form-input>
            </b-col>
          </b-row>
          <!-- BlockHash -->
          <b-row class="my-1">
            <b-col sm="3" class="offset-sm-2 text-left">
              <label>Block Hash:</label>
            </b-col>
            <b-col sm="6">
              <b-form-input size="sm" v-model="cardData.blockhash" readonly></b-form-input>
            </b-col>
          </b-row>
            <b-container>
              <hr style="background-color:white"/>
              <b-row>
                <b-col>
                  <b-button
                    variant="danger"
                    size="sm"
                    @click="deleteClass()"
                    >Delete Block</b-button
                  >
                </b-col>
                <b-col >
                  <b-button
                    :disabled="!cardDataChanged"
                    variant="primary"
                    size="sm"
                    @click="mine()"
                    >Mine</b-button
                  >
                </b-col>
              </b-row>
          </b-container>  
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

  @Prop() private cardData!: BlockData; //!: means can't be null
  private cardDataChanged = false

  @Emit('mine')
  mine() {
    this.cardDataChanged = false
    return this.cardData
  }

  @Emit('delete')
  deleteClass() {
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

