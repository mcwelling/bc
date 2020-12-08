<template>
  <div>
    <div class="row">
      <b-container>
         <!-- Response Banner -->
         <b-card :title="statusSuccess ? 'Success' : 'Error'" class="mt-3" 
         :bg-variant="statusSuccess ? 'success' : 'danger'" text-variant="white" 
         v-show="showStatusBanner">
          <b-card-text>
            {{statusMsg}}
          </b-card-text>
         </b-card>
        <!-- Create Poll Card --> 
        <b-card title="Create a Ballot" class="col-12" bg-variant="dark" text-variant="white">
          <b-card-text>
            Creating a new ballot will overwrite any existing ballot and clear all blockchain data.
            <b-row class="mt-3">
              <b-col>
                  <b-button :variant="showHideConfig ? 'secondary' : 'primary'" class="ml-2" @click="showHideConfig = !showHideConfig"
                    >Create New Ballot</b-button>
              </b-col>
            </b-row>
          </b-card-text>
        </b-card>
        <!-- Hidden polling criteria Card --> 
        <b-card title="New Ballot Configuration" class="mt-3" bg-variant="dark" text-variant="white" v-show="showHideConfig">
          <b-card-text>
            <!-- Polling Cards --> 
            <b-row class="my-1">
                <b-col>
                    <hr style="background-color:grey"/>
                    <div class="row">
                        <div
                        class="col-sm-6 mb-2"
                        v-for="(block, index) in arrBallotConfigData" 
                        :key="index">
                            <poll-child
                            :card-data="block"
                            :card-index="index"
                            @delete="onDeleteClass"
                            ></poll-child>
                        </div>
                        <!-- New Proposal Button -->
                        <div class="col-sm-6 mb-2 mt-5">
                            <b-button variant="primary" class="ml-2" @click="createNewProposal()"
                            ><b>New Proposal</b></b-button>
                        </div>
                    </div>
                </b-col>
            </b-row>
            <!-- Create and Cancel -->
            <b-row class="mt-5">
              <b-col>
                  <b-button variant="primary" class="ml-2" @click="clearChain()">
                    <b-spinner small v-show="showSpinner"></b-spinner>
                    <b> Create</b></b-button>
              </b-col>
              <b-col>
                  <b-button variant="danger" class="ml-2" @click="deleteAll()"
                    ><b>Cancel</b></b-button>
              </b-col>  
            </b-row>
          </b-card-text>
        </b-card>
      </b-container>
    </div>
  </div>
</template>
  

<script lang="ts">

import { Component, Vue } from "vue-property-decorator";
import configBlock from "./config-child.vue";
import { BallotConfig, updateData } from "./BallotConfig";
import { AxiosError } from "axios";


@Component({ components: { "poll-child": configBlock } }) 
export default class BlockParent extends Vue {
    private arrBallotConfigData: BallotConfig[] = [];

    showHideConfig = false;
    showSpinner = false;
    
    private statusSuccess = true;
    private showStatusBanner = false;
    private statusMsg = "";
    
    private defaultServerAddress = "https://619egq74ea.execute-api.us-east-1.amazonaws.com/dev/api/"

    onDeleteClass(c: updateData) {
      const i = c.index;
      this.arrBallotConfigData.splice(i,1);
      //change the id to activate the child @watch
      for(const j in this.arrBallotConfigData){
        this.arrBallotConfigData[j].id = -1;
      }
    }

    deleteAll() {
    this.arrBallotConfigData = [];
    this.showHideConfig = false; 
    }

    clearChain(){
      console.log("Clearing blockchain...")
      this.showSpinner = true;
      const endpoint = this.defaultServerAddress + "reset-chain";
      this.$http.get(endpoint)
      .then(() =>{
        this.createBallot();
      })
      .catch((err: AxiosError) =>{
        console.log(err);
        this.statusSuccess = false;
        this.showStatusBanner = true;
        this.statusMsg = "Unable to clear chain. Please check network connection";
      })
    }

    createBallot() {
      //update UI
      this.showSpinner = true;
      const deleteEndpoint = this.defaultServerAddress + "delete-ballot"
      const sendEndpoint = this.defaultServerAddress + "set-ballot?data=" + encodeURI(JSON.stringify(this.arrBallotConfigData)) //this.arrBallotConfigData

      console.log("Deleting old ballot...")

      this.$http
      .get(deleteEndpoint) 
      .finally(() => { 
          console.log("Sending Ballot...")
          this.$http.get(sendEndpoint)
          .then((response) => {
            console.log(response)

            this.showSpinner = false;
            this.showHideConfig = false;
            
            this.statusSuccess = true;
            this.showStatusBanner = true;
            this.statusMsg = "Ballot created. All blockchain data has been cleared";
          })
          .catch((err: AxiosError)=> {
            console.log(err)

            this.showHideConfig = false;
            this.showSpinner = false;
            
            this.statusSuccess = false;
            this.showStatusBanner = true;
            this.statusMsg = "Unable to create ballot. Please check network connection";
          })
      }) 
    }


    createNewProposal(){
        const empty: string[] = [];
        const newCard = {
            id: this.arrBallotConfigData.length + 1,
            proposal: "",
            options: empty,
            selected: "" 
        }  
        this.arrBallotConfigData.push(newCard);
    }

    reset() {
        this.showHideConfig = false;
        this.arrBallotConfigData = []; 
    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  
</style>
