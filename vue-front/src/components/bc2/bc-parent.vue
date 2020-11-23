<template>
  <div>
    <div class="row">
      <b-container>
        <b-card title="Blockchain Simulator" class="col-12" bg-variant="dark" text-variant="white">
          <b-card-text>
            <b-row class="my-1">
              <b-col>
                  <b-button variant="success" class="ml-2" @click="createNew()"
                    >New Block</b-button
                  >
              </b-col>
            </b-row>
          </b-card-text>
        </b-card>
      </b-container>
    </div>
    <hr />
    <div class="row">
      <!--This loop handles the actual display of the updated array "arrBlocks: BlockData[] = []"-->
      <!-- block is defined here as an element in the array-->
      <div
        class="col-sm-6 mb-2"
        v-for="(block, index) in arrBlocks" 
        :key="index"
      >
      <!-- Pass in cards to display and give each child an event called update-class-info
      call "onUpdateClass" if this event occurs-->
      <!-- note: the custom element "bc-child" directly corresponds with the element defined in the ts script-->
        <bc-child
          :card-data="block"
          @mine="onUpdateClass"
          @delete="onDeleteClass"
        ></bc-child>
      </div>
    </div>
  </div>
</template>
  

<script lang="ts">
import { Component, Prop, Emit, Vue } from "vue-property-decorator";
import Block from "./bc-child.vue";
import { BlockData } from "./BlockData";


@Component({ components: { "bc-child": Block } }) //define the element that will be used in the html above
export default class BlockParent extends Vue {
  private arrBlocks: BlockData[] = [
      {
      id: 0,
      parenthash: "0000000000000000",
      data: "New Block",
      nonce: 0,
      blockhash: "1111111111111111"
      }  

  ];


  //used to increment the default card id when creating new cards
  updateId(n: number){
    //this.defaultCard.id += n;
  }

  onUpdateClass(n: BlockData){
    //Mining code goes here
  }

 onDeleteClass(c: BlockData) {
   const x = this.arrBlocks.indexOf(c) //this line would not scale well, but is suitable for prototyping
   this.arrBlocks.splice(x,1);
  }

  createNew() {
    const num = Math.random()*10e16;
    const hex = num.toString(16);
    const newCard = {
      //id: this.arrBlocks[this.arrBlocks.length-1].,
      id: this.arrBlocks.length,
      parenthash: this.arrBlocks[this.arrBlocks.length-1].blockhash, //"1111111111111111",
      data: "New Block",
      nonce: 0,
      blockhash:  hex//String(Math.random()*10e16) //"0000000000000000"
      }  

    this.arrBlocks.push(newCard);
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  
</style>
