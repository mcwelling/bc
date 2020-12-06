<template>
  <div>
    <div class="row">
      <b-container>
        <!-- Failed to retrieve blocks-->
         <b-card title="Error" class="mt-3" bg-variant="danger" text-variant="white" v-show="showFail">
          <b-card-text>
            Unable to retrieve blocks. <br/> Please ensure that you are connected to the internet.
          </b-card-text>
         </b-card>
          <!-- UVID Found -->
         <b-card title="Success" class="mt-3" bg-variant="success" text-variant="white" v-show="showSuccess">
          <b-card-text>
            Blocks retrieved.
          </b-card-text>
         </b-card>
         <!-- Get Blocks -->
        <b-card bg-variant="dark" text-variant="white">
          <b-button variant="primary" class="ml-2" @click="getBlocks()">
            <b-spinner small v-show="showSpinner"></b-spinner>
            <b> Get Blocks</b></b-button>
        </b-card>
         <!-- Block Data -->
        <b-card class="mt-3" bg-variant="dark" text-variant="white">
          <b-card-header header-tag="header" class="p-1" role="tab">
            <b-button block v-b-toggle.accordion-1 variant="dark"><strong>Blocks</strong></b-button>
          </b-card-header>
        <b-collapse id="accordion-1"  accordion="my-accordion" role="tabpanel">
          <hr style="background-color:grey"/>
          <!-- Block Chain -->
          <div class="row">
            <div
              class="col-sm-6 mb-2"
              v-for="(block, index) in arrBlockData" 
              :key="index">
              <bc-child
                :card-data="block"
                :card-index="index"
                @changed="updateBlocks"
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
import { updateMsg } from "./BlockData";
import blocks from "./bc-child.vue"

import { AxiosError } from "axios";

//Response data types

@Component({ components: { "bc-child": blocks } }) //define the element that will be used in the html above
export default class VoteParent extends Vue {

    //UI
    private showSpinner = false;
    private showSuccess = false;
    private showFail = false;

    //Backend Server
    private defaultServerAddress = "https://619egq74ea.execute-api.us-east-1.amazonaws.com/dev/api/get-blocks";

    private arrBlockData: BlockData[] = [
      {
      id: 0,
      blockid: "ef59ccef9c4e259478446a5458f315e1da2afa028e1e6ebfe9b46c33f42c232a",
      parenthash: "0000000000000000000000000000000000000000000000000000000000000000",
      data: "Root Block",
      nonce: "0",
      blockhash: "11111111111111111111111111111111111111111111111111111111111111111",
      valid: true
      },  
      {
      id: 1,
      blockid: "ef59ccef9c4e259478446a5458f315e1da2afa028e1e6ebfe9b46c33f42c232b",
      parenthash: "wating",
      data: "b1",
      nonce: "0",
      blockhash: "waiting",
      valid: true
      },
      {
      id: 2,
      blockid: "ef59ccef9c4e259478446a5458f315e1da2afa028e1e6ebfe9b46c33f42c232c",
      parenthash: "waiting",
      data: "b2",
      nonce: "0",
      blockhash: "waiting",
      valid: true
      },
      {
      id: 3,
      blockid: "ef59ccef9c4e259478446a5458f315e1da2afa028e1e6ebfe9b46c33f42c232d",
      parenthash: "waiting",
      data: "b3",
      nonce: "0",
      blockhash: "waiting",
      valid: true
      }
    ]

    getBlocks(){
      this.showSpinner = true;
      const endpoint = this.defaultServerAddress;
      this.$http.get<any>(endpoint)
      .then((response) =>{
        this.arrBlockData = response.data;
        this.showSuccess = true;
        this.showFail = false;
      })
      .catch((err: AxiosError) =>{
        console.log(err);
        this.arrBlockData = [];
        this.showFail = true;
        this.showSuccess = false;
      })
      .finally(()=>{
        this.showSpinner = false;
      })
    }

    updateBlocks(msg: updateMsg){
        const i = msg.index;
        const hash = msg.blockhash;
        const bcLen = this.arrBlockData.length;

        if((bcLen > 0) && (i < bcLen-1)){
          this.arrBlockData[i+1].parenthash = hash;
        }
    }



}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  
</style>
