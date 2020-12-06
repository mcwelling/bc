<template>
  <div>
    <div class="row">
      <b-container>
          <!-- Failed to find UVID -->
         <b-card title="UVID Lookup Failed" class="mt-3" bg-variant="danger" text-variant="white" v-show="showUvidFail">
          <b-card-text>
            Unable to locate UVID {{uvid}}. <br/> Please check the entered UVID or register to vote.
          </b-card-text>
         </b-card>
          <!-- UVID Found -->
         <b-card title="UVID Lookup Success" class="mt-3" bg-variant="success" text-variant="white" v-show="showUvidSuccess">
          <b-card-text>
            Welcome {{voterName}}.
          </b-card-text>
         </b-card>
         <!-- Enter UVID and Get Ballot -->
        <b-card bg-variant="dark" text-variant="white">
          <b-row class="my-3" align-h="center">
            <b-col  cols="8" >
              <b-form-input size="sm" v-model="uvid" placeholder="Please enter your Unique Voter ID" ></b-form-input>
            </b-col>
          </b-row>
          <b-button variant="primary" class="ml-2" @click="validateKey()"
                    ><b>Get Ballot</b></b-button>
        </b-card>
        <!-- Load in Ballot Data --> 
        <b-card title="New Ballot Block" class="mt-3" bg-variant="dark" text-variant="white" v-show="showBallot">
          <b-card-text>

            <!-- Ballot Cards --> 
            <b-row class="my-1">
                <b-col>
                    <hr style="background-color:grey"/>
                    <div class="row">
                        <!-- This v-for handles the actual display of the data in the array, arrBallotData -->
                        <!-- block is represents the value (type BallotData) in the array -->
                        <div
                        class="col-sm-6 mb-2"
                        v-for="(block, index) in arrBallotData" 
                        :key="index"
                        >
                        <!-- :card-data="block" passes pollData from the above v-for into the vote-child
                        @delete tells the parent to look out for the @delete emit event from the child and calls the onDeleteClass method.
                        Note: the custom element "vote-child" directly corresponds with the definition in the ts script-->
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
                  <b-button variant="primary" class="ml-2" @click="vote()"
                    ><b>Vote</b></b-button>
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
//Note: Prop and Emit are not used and can be removed if not used before generating the production build
import { Component, Prop, Emit, Vue } from "vue-property-decorator";
import votingBlock from "./voting-child.vue";
import { BallotData } from "./BallotData";
import { AxiosError } from "axios";

//Response data types
import { regResponse } from "./regResponse"

@Component({ components: { "vote-child": votingBlock} }) //define the element that will be used in the html above
export default class VoteParent extends Vue {
  /////////////////////////////VOTING////////////////////////////////////////////
    private arrBallotData: BallotData[] = [
        //Array of proposals on the ballot
    ];

    private uvid = ""; //unique voter ID
    private showBallot = false;
    private showUvidFail = false;
    private showUvidSuccess = false;
    private voterName = "";

    //Backend Server
    private defaultServerAddress = "https://619egq74ea.execute-api.us-east-1.amazonaws.com/dev/api/";

    validateKey(){
      //Validate the uvid key by making a get call to the backend
      
      const endpoint = this.defaultServerAddress + "check-reg?voter_id=" + this.uvid;
      this.$http.get<regResponse>(endpoint)
      .then((response) => {
        //console.log("data:", response.data.Item)
        if(response.data.Item === undefined){
          console.log("Null")
          this.showUvidFail = true;
          this.showUvidSuccess = false;
        }
        else{
          console.log(response.data.Item)
          this.voterName = response.data.Item.voter_fname + " " + response.data.Item.voter_lname
          this.showUvidFail = false;
          this.showUvidSuccess = true;
          this.getAll();
        }
      })
      .catch((err: AxiosError) => {
          console.log("Failed")
          console.log(err.response)
          //Show a not found message here
        })

    }

    getAll() {
      //console.log("getall");

      const endpoint = this.defaultServerAddress + "get-ballot";
      this.$http.get<any>(endpoint) // use any to make it easy to change and test the data structures
      .then((response) => {
        console.log(JSON.parse(response.data.Item.info.data))
        this.arrBallotData = JSON.parse(response.data.Item.info.data)
        this.showBallot = true;
      });
  }

    vote(){
        const voteData = encodeURI(JSON.stringify(this.arrBallotData))
        //const voteData = JSON.stringify(this.arrBallotData)
        //create block 
        /*
        const newBlock = {
          //id: this.arrBlocks[this.arrBlocks.length-1].,
          id: this.arrBlockData.length,
          parenthash: this.arrBlockData[this.arrBlockData.length-1].blockhash, //"1111111111111111",
          data: voteData, //"New Block",
          nonce: 0,
          blockhash:  "0000000000000000",
          valid: false
          }  
        
        this.arrBlockData.push(newBlock);
        //send data to miner here
        */
    }

    reset() {
        for (const i of this.arrBallotData){
          //console.log(i.selected);
          i.selected = "";
        }
    }

}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  
</style>
