<template>
  <div>
    <div class="row">
      <b-container>
        <b-card bg-variant="dark" text-variant="white">
          <b-button variant="success" class="ml-2" @click="getAll()"
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
            
            <!--Create and Cancel Buttons-->
            <b-row class="mt-5">
              <b-col>
                  <b-button variant="success" class="ml-2" @click="vote()"
                    ><b>Vote</b></b-button>
              </b-col>
              <b-col>
                  <b-button variant="danger" class="ml-2" @click="reset()"
                    ><b>Clear</b></b-button>
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
import votingBlock from "./voting-child.vue"
import { BallotData } from "./BallotData";


@Component({ components: { "vote-child": votingBlock } }) //define the element that will be used in the html above
export default class BlockParent extends Vue {
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

    private showBallot = false;

    //JSON
    private defaultServerAddress = "http://localhost:3000";

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
        //create block and send data to miner here
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
