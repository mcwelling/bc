<template>
  <div>
    <div class="row">
      <b-container>
        <!-- Create Poll Card --> 
        <b-card title="Create a Ballot" class="col-12" bg-variant="dark" text-variant="white" v-show="showHideCreate">
          <b-card-text>
            <b-row class="my-1">
              <b-col>
                  <b-button :variant="showHideConfig ? 'secondary' : 'success'" class="ml-2" @click="showHideConfig = !showHideConfig"
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
                        <!-- This v-for handles the actual display of the data in the array, arrPollData -->
                        <!-- block is represents the value (type PollData) in the array -->
                        <div
                        class="col-sm-6 mb-2"
                        v-for="(block, index) in arrPollData" 
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
                            <b-button variant="primary" class="ml-2" @click="createNewCard()"
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
                  <b-button variant="success" class="ml-2" @click="createNewPoll()"
                    ><b>Create</b></b-button>
              </b-col>
              <b-col>
                  <b-button variant="danger" class="ml-2" @click="reset()"
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
import { PollData } from "./PollData";


@Component({ components: { "poll-child": configBlock } }) //define the element that will be used in the html above
export default class BlockParent extends Vue {
    private arrPollData: PollData[] = [];


    onUpdateClass(n: PollData){
    //Mining code goes here
    }

    onDeleteClass(c: PollData) {
    const x = this.arrPollData.indexOf(c) //this line would not scale well, but is suitable for prototyping
    this.arrPollData.splice(x,1);
    }

    showHideCreate = true;
    showHideConfig = false;
    writeInToggle = false;
    showHideVote = false;

    createNewPoll() {
      //cleanup
      this.showHideCreate= false;
      this.showHideConfig = false;
     // this.arrPollData = []; 
      this.showHideVote = true;

    }

    createNewCard(){
        const empty: string[] = [];
        const newCard = {
            id: this.arrPollData.length + 1,
            description: "",
            options: empty,
        }  
        this.arrPollData.push(newCard);
    }

    reset() {
        this.showHideConfig = false;
        this.writeInToggle = false;
        this.arrPollData = []; 
    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  
</style>
