<template>
  <div>
    <div class="row">
      <b-container>
         <!-- Block Data -->
        <b-card class="mt-3" bg-variant="dark" text-variant="white">
          <b-card-header header-tag="header" class="p-1" role="tab">
            <b-button block v-b-toggle.accordion-1 variant="dark"><strong>Blocks</strong></b-button>
          </b-card-header>
        <b-collapse id="accordion-1"  accordion="my-accordion" role="tabpanel">
          <hr style="background-color:grey"/>
          <!-- Block Chain -->
          <div class="row">
            <!--This loop handles the actual display of the updated array "arrBlockData: BlockData[] = []"-->
            <!-- block is defined here as an element in the array -->
            <div
              class="col-sm-6 mb-2"
              v-for="(block2, index2) in arrBlockData" 
              :key="index2"
            >
            <!-- Pass in cards to display and give each child an event called update-class-info
            call "onUpdateClass" if this event occurs-->
            <!-- note: the custom element "bc-child" directly corresponds with the element defined in the ts script-->
              <bc-child
                :card-data="block2"
                @mine="mineBlock"
                @delete="deleteBlock"
              ></bc-child> 
            </div>
          </div>
            </b-collapse>
        </b-card>
       
      </b-container>
    </div>
  </div>
</template>
  





<script lang="ts">
//Note: Prop and Emit are not used and can be removed if not used before generating the production build
import { Component, Prop, Emit, Vue } from "vue-property-decorator";
import votingBlock from "./voting-child.vue";

import { BlockData } from "./BlockData";
import blocks from "./bc-child.vue"

import { AxiosError } from "axios";

//Response data types

@Component({ components: { "bc-child": blocks } }) //define the element that will be used in the html above
export default class VoteParent extends Vue {

    //Backend Server
    private defaultServerAddress = "https://619egq74ea.execute-api.us-east-1.amazonaws.com/dev/api/";

    private arrBlockData: BlockData[] = [
      {
      id: 0,
      parenthash: "0000000000000000",
      data: "Root Block",
      nonce: 0,
      blockhash: "1111111111111111",
      valid: true
      }  
    ]

    getBlocks(){
        //This will get the blocks from the backend
    }

    mineBlock(){
        //create block and send data to miner here
    }

    deleteBlock(){
        //create block and send data to miner here
    }



}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  
</style>
