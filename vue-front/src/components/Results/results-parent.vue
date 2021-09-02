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
         <!-- Get Results Button -->
        <b-card bg-variant="dark" text-variant="white">
          <b-button variant="primary" class="ml-2" @click="getCounts()">
            <b-spinner small v-show="showSpinner"></b-spinner>
            <b> Get Results</b></b-button>
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
                            <results-child
                            :card-data="block"
                            :card-results="arrBallotResults[index]"
                            ></results-child>
                        </div>
                    </div>
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
import resultsBlock from "./results-child.vue";
import { BallotData } from "./BallotData";
import { AxiosError } from "axios";


@Component({ components: { "results-child": resultsBlock} }) 
export default class VoteParent extends Vue {

    private arrBallotData: BallotData[] = [
        //Array of proposals on the ballot
    ];

    private arrBallotResults= [];

    private uvid = ""; //unique voter ID
    private showBallot = false;
    private showStatusBanner = false;
    private statusSuccess = false;
    private statusMsg = "";
    private showSpinner = false;

    //Backend Server
    private defaultServerAddress = "https://619egq74ea.execute-api.us-east-1.amazonaws.com/dev/api/";



    getCounts() {
      this.showSpinner = true;
      const endpoint = this.defaultServerAddress + "get-ballot";
      this.$http.get(endpoint) 
      .then((response) => {
        this.arrBallotData = JSON.parse(response.data.Item.info.data)
        this.getResults();
      })
      .catch((err: AxiosError) => {
          this.showSpinner = false;
          console.log("Failed")
          console.log(err.response)
          this.statusSuccess = false;
          this.showStatusBanner = true;
          this.statusMsg = "Failed to retrieve ballot data. Please check network connection";
        });
      }

    getResults(){
      const endpoint = this.defaultServerAddress + "count-votes";
      console.log(endpoint)
      this.$http.get(endpoint)
      .then((response) => {
        console.log(JSON.parse(response.data.body))
        this.arrBallotResults = JSON.parse(response.data.body)
        this.showBallot = true;
        this.showSpinner = false;

        this.statusSuccess = true;
        this.showStatusBanner = true;
        this.statusMsg = "Retrieved results.";
      })
      .catch((err: AxiosError) => {
          this.showSpinner = false;
          console.log("Get Results Failed")
          console.log(err.response)
          this.statusSuccess = false;
          this.showStatusBanner = true;
          this.statusMsg = "Failed to retrieve vote counts. Please check network connection";
        });
    }

}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  
</style>
