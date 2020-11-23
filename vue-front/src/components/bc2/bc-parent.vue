<template>
  <div>
    <div class="row">
      <b-container>
        <b-card title="Blockchain Simulator" class="col-12" bg-variant="dark" text-variant="white">
          <b-card-text>
            <b-row class="my-1">
              <b-col>
                  <b-button variant="success" class="ml-2" @click="createNew()"
                    >New Block</b-button
                  >
              </b-col>
            </b-row>
            <b-row>
              <b-col sm="8" class="offset-sm-2">
                <b-alert fade :show="showErrorBanner" dismissible variant="danger" @dismissed="showErrorBanner=false">
                  {{ errorMessage }}
                </b-alert>
              </b-col>
            </b-row>
            <b-row>
              <b-col sm="8" class="offset-sm-2">
                <b-alert fade :show="showOkBanner" dismissible variant="success" @dismissed="showOKBanner=false">
                  {{ okMessage }}
                </b-alert>
              </b-col>
            </b-row>
          </b-card-text>
        </b-card>
        <hr /> <!-- Add space-->
      </b-container>
      <!--
        
        TEST
        
        -->
       <b-container hidden="true">
         <b-card title="New Block" bg-variant="dark" text-variant="white">
          <b-card-text>
            <b-container>
              <b-row >
                <!-- label -->
                <b-col sm="3" class="offset-sm-2 text-left">
                  <label>Data:</label>
                </b-col>
                <!-- form -->
                <b-col sm="6">
                  <b-form-textarea size="sm"></b-form-textarea>
                  <!-- <b-form-textarea size="sm" v-model="data"></b-form-textarea> -->
                </b-col>
              </b-row>
            </b-container>
          </b-card-text>
        </b-card>
      </b-container>
       <!-- 
        
        TEST! 

        -->
    </div>
    <hr />
    <div class="row">
      <!--This loop handles the actual display of the updated array "showBlockData: BlockData[] = []"-->
      <div
        class="col-sm-6 mb-2"
        v-for="(block, index) in showBlockData" 
        :key="index"
      >
      <!-- Pass in cards to display and give each child an event called update-class-info
      call "onUpdateClass" if this event occurs-->
      <!-- note: the custom element "bc-child" directly corresponds with the element defined in the ts script-->
        <bc-child
          :card-data="block" 
          @update-class-info="onUpdateClass"
          @delete-class-info="onDeleteClass"
        ></bc-child>
      </div>
    </div>
  </div>
</template>
  

<script lang="ts">
import { Component, Prop, Emit, Vue } from "vue-property-decorator";
import Pub from "./bc-child.vue";
import { AxiosResponse, AxiosError } from "axios";
import { BlockData } from "./BlockData";

@Component({ components: { "bc-child": Pub } }) //define the element that will be used in the html above
export default class ServiceParent extends Vue {
  private showBlockData: BlockData[] = [];
  private defaultServerAddress = "http://localhost:3000";
  private searchPubId = "1";
  private showErrorBanner = false;
  private errorMessage = "";
  private showOkBanner = false;
  private okMessage = "";

  //define default data to be used to create new blocks
  private defaultCard = {
      id: 1,
      parenthash: "1111111111111111",
      data: "New Block",
      nonce: 0,
      blockhash: "0000000000000000"
    }

  //used to increment the default card id when creating new cards
  updateId(n: number){
    this.defaultCard.id += n;
  }

  searchById() {
    console.log("searchbyid");
    this.showErrorBanner =  false; //cleanup
    this.showOkBanner =  false; //cleanup
    this.showBlockData = []; //cleanup
    const endpoint = this.defaultServerAddress + "/blocks/" + this.searchPubId; //get data from web server
    //The code below is asynchronous
    this.$http //$ means it's associated with a view, http says it's web based
      .get<BlockData>(endpoint) // CourseTyoe is a stereotype defined in BlockData.ts
      .then((response) => { //runs if the get is successful. Don't have to know when it will finish
        this.okMessage = "Fetched Course with ID: " + this.searchPubId;
        this.showOkBanner = true;
        const result = response.data;
        this.showBlockData = [result];
        console.log(result);
      })
      .catch((err: AxiosError) => { //runs if the get errors
        console.log("ERROR ", err.response);
        this.errorMessage = "HTTP Error:" 
            + err.response!.status
            + "; Msg: "+ err.response!.statusText;
        this.showErrorBanner = true;
        this.showOkBanner =  false;
      });
  }
  getAll() {
    console.log("getall");
    this.showErrorBanner = false;
    this.showOkBanner =  false;
    this.showBlockData = [];
    const endpoint = this.defaultServerAddress + "/blocks";
    this.$http.get<BlockData[]>(endpoint)
    .then((response) => {
      const result = response.data;
      this.showBlockData = result;
      this.okMessage = "Fetched All Blocks - Total Received: " + this.showBlockData.length ;
      this.showOkBanner = true;
      console.log(result);
    });
  }

  onUpdateClass(c: BlockData) {
    this.showErrorBanner = false;
    this.showOkBanner =  false;
    this.showBlockData = [];
    //remember c is the argument passed into this function
    const endpoint = this.defaultServerAddress + "/blocks/" + c.id;
    //Same idea as get but it ovewrites existing data
    this.$http.put<BlockData>(endpoint, c)
    .then((response) => {
      const result = response.data;
      console.log("Updated ", result);
      this.okMessage = "Updated Course with ID: " + c.id + " successfully";
      this.showOkBanner = true;
    });
  }

 onDeleteClass(c: BlockData) {
    this.showErrorBanner = false;
    this.showOkBanner =  false;
    this.showBlockData = [];
    //remember c is the argument passed into this function
    const endpoint = this.defaultServerAddress + "/blocks/" + c.id;
    //Delete the entry
    this.$http.delete<BlockData>(endpoint, c)
    .then((response) => {
      const result = response.data;
      console.log("Updated ", result);
      this.okMessage = "Successfully deleted new block";
      this.showOkBanner = true;
      this.getAll();
      //this.updateId(-1); //This numbering will cause the numbering to be off if you don't delete the most recent block
    });
  }

  createNew() {
    this.showOkBanner =  false;
    this.showBlockData = [];
    //this.errorMessage = "Not Imnplemented Yet";
    //this.showErrorBanner = true;
    const endpoint = this.defaultServerAddress + "/blocks";
    //FIX ME: Post is not idempotent
    this.$http.post<BlockData>(endpoint, this.defaultCard)
    .then((response) => {
      const result = response.data;
      console.log("Updated ", result);
      this.okMessage = "Successfully created new block";
      this.showOkBanner = true;
      this.getAll();
      this.updateId(1);
    });
    
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  
</style>
