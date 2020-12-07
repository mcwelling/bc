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
          <b-row align-h="center">
            <b-col cols="4">
              <b-button variant="primary" class="ml-2" @click="getBlocks()">
                <b-spinner small v-show="showSpinner"></b-spinner>
                <b> Get Blocks</b></b-button>
              </b-col>
            <b-col cols="4">
              <b-button variant="danger" class="ml-2" @click="clearChain()">
                <b-spinner small v-show="showSpinner2"></b-spinner>
                <b> Clear Chain</b></b-button>
              </b-col>
          </b-row>
        </b-card>
         <!-- Block Data -->
        <b-card class="mt-3" bg-variant="dark" text-variant="white">
          <b-card-header header-tag="header" class="p-1" role="tab">
            <b-button block v-b-toggle.accordion-1  variant="dark"><strong>Blocks</strong></b-button>
          </b-card-header>
        <b-collapse id="accordion-1" visible accordion="my-accordion" role="tabpanel">
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
import { getResponse } from "./BlockData";
import blocks from "./bc-child.vue"

import { AxiosError } from "axios";

//Response data types

@Component({ components: { "bc-child": blocks } }) //define the element that will be used in the html above
export default class VoteParent extends Vue {

    //UI
    private showSpinner = false;
    private showSpinner2 = false;
    private showSuccess = false;
    private showFail = false;

    //Backend Server
    private defaultServerAddress = "https://619egq74ea.execute-api.us-east-1.amazonaws.com/dev/api/";

    private arrBlockData: BlockData[] = []

    getBlocks(){
      this.arrBlockData = [];
      this.showSpinner = true;
      const endpoint = this.defaultServerAddress + "get-blocks";
      //console.log(endpoint)
      this.$http.get<any>(endpoint)
      .then((response) =>{
        //console.log(response.data.body)
        const arrTemp: getResponse[] = JSON.parse(response.data.body);
        for(const i in arrTemp){
          if(i === "0"){
            continue;
          }
          const temp: BlockData = {
              id: i,
              blockid: arrTemp[i].voter_id,
              parenthash: arrTemp[i].parent_hash,
              data: arrTemp[i].ballot,
              nonce: arrTemp[i].nonce,
              blockhash: arrTemp[i].block_hash,
              valid: true,
          }
         // console.log(temp)
          this.arrBlockData.push(temp)
        }
        //console.log(arrTemp);
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

    clearChain(){
      this.showSpinner2 = true;
      const endpoint = this.defaultServerAddress + "reset-chain";
      this.$http.get<any>(endpoint)
      .then((response) =>{
        this.arrBlockData = [];
        //this.showSuccess = true;
        //this.showFail = false;
      })
      .catch((err: AxiosError) =>{
        console.log(err);
        //this.arrBlockData = [];
        //this.showFail = true;
        //this.showSuccess = false;
      })
      .finally(()=>{
        this.showSpinner2 = false;
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
