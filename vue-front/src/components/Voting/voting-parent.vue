<template>
  <div>
    <div class="row">
      <b-container>
        <b-card bg-variant="dark" text-variant="white">
          <b-row class="my-3" align-h="center">
            <b-col  cols="8" >
              <b-form-input size="sm" v-model="uvid" placeholder="Please enter your Unique Voter ID" ></b-form-input>
            </b-col>
          </b-row>
          <b-button variant="primary" class="ml-2" @click="getAll()"
                    ><b>Get Ballot</b></b-button>
        </b-card>
        <!-- Ballots --> 
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
import { BallotData } from "./BallotData";

import { BlockData } from "./BlockData";
import blocks from "./bc-child.vue"


@Component({ components: { "vote-child": votingBlock, "bc-child": blocks } }) //define the element that will be used in the html above
export default class VoteParent extends Vue {
  /////////////////////////////VOTING////////////////////////////////////////////
    private arrBallotData: BallotData[] = [
         /* {
            id: 1,
            proposal: "Favorite Color?",
            options: ["red", "blue", "green"],
            selected: "" //"red"
          },
          {
            id: 2,
            proposal: "Favorite Number",
            options: ["1", "2", "3"],
            selected: "" //"3"
          }*/
    ];

    private uvid = ""; //unique voter ID
    private showBallot = false;

    //JSON
    private defaultServerAddress = "http://localhost:3000";

    validateKey(){
      //Validate the uvid key by making a get call to the backend
      /*
      const endpoint = this.defaultServerAddress + "/proposals";
      this.$http.get<any>(endpoint) // use any to make it easy to change and test the data structures
      .then((response) => {
        console.log("data:", result)
        this.getAll();
      })
      .catch((err: AxiosError) => {
          console.log("Failed")
          //Show a not found message here
        })
      */
    }

    getAll() {
      console.log("getall");

      const endpoint = this.defaultServerAddress + "/proposals";
      this.$http.get<any>(endpoint) // use any to make it easy to change and test the data structures
      .then((response) => {
        const result = response.data;
        //The data is packaged into a data structure to reduce the number of calls required
        //and give the ballot an easy to find id. see the ballot designer for details
        this.arrBallotData = result[0].data; 
        console.log("data:", result)

        this.showBallot = true;
      });
  }

    vote(){
        const voteData = JSON.stringify(this.arrBallotData)
        //create block 
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
    }

    reset() {
        for (const i of this.arrBallotData){
          //console.log(i.selected);
          i.selected = "";
        }
    }


/////////////////////Block Data/////////////////////////////////////////////////
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
