<template>
  <div>
    <div class="row">
      <b-container>
        <!-- Create Poll Card --> 
        <b-card title="Create a Ballot" class="col-12" bg-variant="dark" text-variant="white">
          <b-card-text>
            <b-row class="my-1">
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
                        <!-- This v-for handles the actual display of the data in the array, arrBallotConfigData -->
                        <!-- block is represents the value (type BallotConfig) in the array -->
                        <div
                        class="col-sm-6 mb-2"
                        v-for="(block, index) in arrBallotConfigData" 
                        :key="index"
                        >
                        <!-- :card-data="block" passes pollData from the above v-for into the poll-child
                        @delete tells the parent to look out for the @delete emit event from the child and calls the onDeleteClass method.
                        Note: the custom element "poll-child" directly corresponds with the definition in the ts script-->
                            <poll-child
                            :card-data="block"
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
            <!-- write-in toggle --> 
            <b-row class="mt-5">
              <b-col>
                    <b-form-checkbox v-model="writeInToggle" name="check-button" switch >
                        Write-in permitted?
                    </b-form-checkbox>
              </b-col>
              <b-col>
                  <!-- might look better if the color changed? -->
                  <b>{{ writeInToggle ? "yes" : "no" }}</b>
              </b-col>  
            </b-row>
            <!--Create and Cancel Buttons-->
            <b-row class="mt-5">
              <b-col>
                  <b-button variant="primary" class="ml-2" @click="createBallot()"
                    ><b>Create</b></b-button>
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
//Note: Prop and Emit are not used and can be removed if not used before generating the production build
import { Component, Prop, Emit, Vue } from "vue-property-decorator";
import configBlock from "./config-child.vue";
import { BallotConfig } from "./BallotConfig";
import { AxiosError } from "axios";


@Component({ components: { "poll-child": configBlock } }) //define the element that will be used in the html above
export default class BlockParent extends Vue {
    private arrBallotConfigData: BallotConfig[] = [];

    showHideConfig = false;
    writeInToggle = false;

    //JSON
    //private defaultServerAddress = "http://localhost:3000/proposals/";
      private defaultServerAddress = "https://619egq74ea.execute-api.us-east-1.amazonaws.com/dev/api/"

    onDeleteClass(c: BallotConfig) {
    const x = this.arrBallotConfigData.indexOf(c) //this line would not scale well, but is suitable for prototyping
    this.arrBallotConfigData.splice(x,1);
    }

    createBallot() {
      //cleanup UI
      this.showHideConfig = false;
      const deleteEndpoint = this.defaultServerAddress + "delete-ballot"
      const sendEndpoint = this.defaultServerAddress + "set-ballot?data=" + encodeURI(JSON.stringify(this.arrBallotConfigData)) //this.arrBallotConfigData
      /*
      this.$http.get(endpoint)
      .then((response) => {
        console.log(response)
      })
      .catch((err: AxiosError)=> {
        console.log(err)
      })
     */
      console.log("deleting...")
      //this.deleteAll(); // delete the last config
      this.$http
      .get(deleteEndpoint) 
      .finally(() => { //Placing the post inside finally is important. otherwise the post could overlap with delete
          console.log("Sending Ballot...")
          this.$http.get(sendEndpoint)
          .then((response) => {
            console.log(response)
          })
          .catch((err: AxiosError)=> {
            console.log(err)
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
            /*selected isn't actually used in this module but it makes it easier for the voting module to use the data 
            straight out of the json server. It may be more faithful to the idea of modularization to remove selected
            and handle it on the voting end*/
        }  
        this.arrBallotConfigData.push(newCard);
    }

    reset() {
        this.showHideConfig = false;
        this.writeInToggle = false;
        this.arrBallotConfigData = []; 
    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  
</style>
