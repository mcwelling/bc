<template>
  <div>
    <div class="row">
      <b-container>
          <!-- Response Banner -->
         <b-card :title="statusSuccess ? 'Success' : 'Error'" class="mt-3" :bg-variant="statusSuccess ? 'success' : 'danger'" text-variant="white" v-show="showStatusBanner">
          <b-card-text>
            {{statusMsg}}
          </b-card-text>
         </b-card>
         <!-- Enter UVID and Get Ballot -->
        <b-card title="Voting Simulator" bg-variant="dark" text-variant="white">
          The following voters have been pre-registered:
          <br/>049fc8808dcf9f083c01040f76ab20c8e9b07a033242192c4381f3c82e663c0b
          <br/>b5c01a531981eddadc42af2f744a08a6cd9d9024d7be6dae6b5f6d4a5f0513a9
          <br/>eeafd6e402aeaef1b1f3367a14bd615085bfe91d68654d64e0f9968daf0c0217
          
          <b-row class="my-3" align-h="center">
            <b-col  cols="8" >
              <b-form-input size="sm" v-model="uvid" placeholder="Please enter your Unique Voter ID" ></b-form-input>
            </b-col>
          </b-row>
          <b-button variant="primary" class="ml-2" @click="validateKey()">
            <b-spinner small v-show="showSpinner1"></b-spinner>
            <b> Get Ballot</b></b-button>
        </b-card>
        <!-- Load in Ballot Data --> 
        <b-card title="New Ballot Block" class="mt-3" bg-variant="dark" text-variant="white" v-show="showBallot">
          <b-card-text>

            <!-- Ballot Cards --> 
            <b-row class="my-1">
                <b-col>
                    <hr style="background-color:grey"/>
                    <div class="row">
                        <div
                        class="col-sm-6 mb-2"
                        v-for="(block, index) in arrBallotData" 
                        :key="index">
                            <vote-child
                            :card-data="block"
                            ></vote-child>
                        </div>
                    </div>
                </b-col>
            </b-row>

            <!--Vote and Clear Buttons-->
            <b-row class="mt-5">
              <b-col>
                  <b-button variant="primary" class="ml-2" :disabled="!canVote" @click="setVoteProcessing()">
                    <b-spinner small v-show="showSpinner2"></b-spinner>
                    <b> Vote</b></b-button>
              </b-col>
              <b-col>
                  <b-button variant="danger" class="ml-2" @click="reset()"
                    ><b>Clear Selected</b></b-button>
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
import votingBlock from "./voting-child.vue";
import { BallotData } from "./BallotData";
import { AxiosError } from "axios";

//Response data types
import { regResponse } from "./regResponse"

@Component({ components: { "vote-child": votingBlock} }) 
export default class VoteParent extends Vue {
    private arrBallotData: BallotData[] = [
        //Array of proposals on the ballot
    ];

    private uvid = ""; //unique voter ID
    private showBallot = false;
    private showStatusBanner = false;
    private statusSuccess = false;
    private statusMsg = "";
    private canVote = true;
    private voterName = "";
    private showSpinner1 = false;
    private showSpinner2 = false;

    //Backend Server
    private defaultServerAddress = "https://619egq74ea.execute-api.us-east-1.amazonaws.com/dev/api/";

    validateKey(){
      
      this.showSpinner1 = true;

      //Validate the uvid key by making a get call to the backend
      const endpoint = this.defaultServerAddress + "check-reg?voter_id=" + this.uvid;
      this.$http.get<regResponse>(endpoint)
      .then((response) => {
        //No user registered
        if(response.data.Item === undefined){
          console.log("Null")
          this.statusMsg = "A user with the UVID '" + this.uvid + "' has not been registered."
          this.statusSuccess = false;
          this.showStatusBanner = true;
          this.uvid = "";
          this.showSpinner1 = false;
        }
        //user found
        else{
          console.log(response.data.Item)
          this.voterName = response.data.Item.voter_fname + " " + response.data.Item.voter_lname
          this.statusMsg = "Welcome " + this.voterName + ".";
          this.statusSuccess = true;
          this.showStatusBanner = true;

          console.log("voted", response.data.Item.voted_yn)
          //check if the user voted yet
          if(response.data.Item.voted_yn === "N"){
              this.getAll();
          }
          else{
            this.statusMsg = this.statusMsg + " Our records show that you have already voted!"
            this.showSpinner1 = false;
            this.uvid = "";
          }
          
        }
      })
      .catch((err: AxiosError) => {
          this.showSpinner1 = false;
          console.log(err.response);
          this.statusMsg = "Please enter a valid UVID.";
          this.statusSuccess = false;
          this.showStatusBanner = true;
        })

    }

    //
    setVoteProcessing(){
      this.showSpinner2 = true;
      const endpoint = this.defaultServerAddress + "set-reg-status?voter_id=" + this.uvid;
      this.$http.get(endpoint)
      .then(() => {
          this.canVote = true;
          this.vote();
      })
      .catch((err: AxiosError) => {
        console.log(err)
      })
    }


    getAll() {
      const endpoint = this.defaultServerAddress + "get-ballot";
      this.$http.get(endpoint)
      .then((response) => {
        console.log(JSON.parse(response.data.Item.info.data))
        this.arrBallotData = JSON.parse(response.data.Item.info.data)
        this.showBallot = true;
        this.showSpinner1 = false;
      })
      .catch((err: AxiosError) => {
          this.showSpinner1 = false;
          console.log("Failed")
          console.log(err.response)
        });
      }
      

    vote(){
        const voteData = encodeURI(JSON.stringify(this.arrBallotData)) 
        const suffix = "queue-vote?voter_id=" + this.uvid + "&payload=" + voteData;
        const endpoint = this.defaultServerAddress + suffix;

        this.$http.get(endpoint)
        .then((response) =>{
          console.log(response)
          this.showBallot = false;
          this.statusMsg = "Vote submitted.";
          this.statusSuccess = true;
        })
        .catch((err: AxiosError) => {
          console.log(err);
          this.statusMsg = "Networking Error.";
          this.statusSuccess = false;
          this.canVote = true;
        })
        .finally(() => {
          this.showStatusBanner = true;
          this.showSpinner2 = false;
          this.uvid = "";
        })
    }

    reset() {
        for (const i of this.arrBallotData){
          i.selected = "";
        }
    }

}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  
</style>
