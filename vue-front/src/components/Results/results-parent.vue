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
            <b-spinner small v-show="showSpinner1"></b-spinner>
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
//Note: Prop and Emit are not used and can be removed if not used before generating the production build
import { Component, Prop, Emit, Vue } from "vue-property-decorator";
import resultsBlock from "./results-child.vue";
import { BallotData } from "./BallotData";
import { AxiosError } from "axios";

//Response data types
import { regResponse } from "./regResponse"

@Component({ components: { "results-child": resultsBlock} }) //define the element that will be used in the html above
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
    private canVote = true;
    private voterName = "";
    private showSpinner1 = false;
    private showSpinner2 = false;

    //Backend Server
    private defaultServerAddress = "https://619egq74ea.execute-api.us-east-1.amazonaws.com/dev/api/";

    //count-votes

    getCounts() {
      const endpoint = this.defaultServerAddress + "get-ballot";
      this.$http.get<any>(endpoint) // use any to make it easy to change and test the data structures
      .then((response) => {
        //console.log(JSON.parse(response.data.Item.info.data))
        this.arrBallotData = JSON.parse(response.data.Item.info.data)
        this.getResults();
      })
      .catch((err: AxiosError) => {
          this.showSpinner1 = false;
          console.log("Failed")
          console.log(err.response)
          //Show a not found message here
        });
      }

    getResults(){
      const endpoint = this.defaultServerAddress + "count-votes";
      //console.log(endpoint)
      this.$http.get<any>(endpoint) // use any to make it easy to change and test the data structures
      .then((response) => {
        console.log(JSON.parse(response.data.body))
        this.arrBallotResults = JSON.parse(response.data.body)
        this.showBallot = true;
        this.showSpinner1 = false;
      })
      .catch((err: AxiosError) => {
          this.showSpinner1 = false;
          console.log("Get Results Failed")
          console.log(err.response)
          //Show a not found message here
        });
    }

}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  
</style>
