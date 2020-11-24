<template>
  <div>
    <div class="row">
      <b-container>
        <b-card title="Polling Simulator" class="col-12" bg-variant="dark" text-variant="white">
          <b-card-text>
            <b-row class="my-1">
              <b-col>
                  <b-button :variant="showHideConfig ? 'secondary' : 'success'" class="ml-2" @click="showHideConfig = !showHideConfig"
                    >Create New Poll</b-button>
              </b-col>
            </b-row>
          </b-card-text>
        </b-card>
        <!-- Hidden polling criteria Card --> 
        <b-card title="New Poll Configuration" class="mt-3" bg-variant="dark" text-variant="white" v-show="showHideConfig">
          <b-card-text>
            <!-- Polling Cards --> 
            <b-row class="my-1">
                <b-col>
                    <hr style="background-color:grey"/>
                    <div class="row">
                        <!--This loop handles the actual display of the updated array "arrBlocks: BlockData[] = []"-->
                        <!-- block is defined here as an element in the array-->
                        <div
                        class="col-sm-6 mb-2"
                        v-for="(block, index) in arrBlocks" 
                        :key="index"
                        >
                        <!-- Pass in cards to display and give each child an event called update-class-info
                        call "onUpdateClass" if this event occurs-->
                        <!-- note: the custom element "bc-child" directly corresponds with the element defined in the ts script-->
                            <bc-child
                            :card-data="block"
                            @mine="onUpdateClass"
                            @delete="onDeleteClass"
                            ></bc-child>
                        </div>
                        <!-- May want to create a dummy card with this in it to make it look right -->
                        <div class="col-sm-6 mb-2">
                            <b-button variant="primary" class="ml-2" @click="createNewCard()"
                            ><b>New Card</b></b-button>
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
import { Component, Prop, Emit, Vue } from "vue-property-decorator";
import Block from "./polling-child.vue";
import { BlockData } from "./BlockData";


@Component({ components: { "bc-child": Block } }) //define the element that will be used in the html above
export default class BlockParent extends Vue {
    private arrBlocks: BlockData[] = [];


    onUpdateClass(n: BlockData){
    //Mining code goes here
    }

    onDeleteClass(c: BlockData) {
    const x = this.arrBlocks.indexOf(c) //this line would not scale well, but is suitable for prototyping
    this.arrBlocks.splice(x,1);
    }


    showHideConfig = false;
    writeInToggle = false;

    createNewPoll() {
    //something goes here later
    }

    createNewCard(){
        const newCard = {
            id: this.arrBlocks.length,
            parenthash: "0",
            data: "New Block",
            nonce: 0,
            blockhash: "0",
        }  
        this.arrBlocks.push(newCard);
    }

    reset() {
    //something goes here later
        this.showHideConfig = false;
        this.writeInToggle = false;
        this.arrBlocks = []; 
    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  
</style>
