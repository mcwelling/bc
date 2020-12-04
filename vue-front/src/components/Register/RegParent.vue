<template>
  <div>
    <div class="row">
      <b-container>
        <!-- Register --> 
        <b-card title="Register to Vote" class="col-12" bg-variant="dark" text-variant="white">
          <b-card-text>
            <b-row class="my-1">
              <b-col>
                  <b-button :variant="showHideReg ? 'secondary' : 'primary'" class="ml-2" @click="showHideReg = !showHideReg"
                    >New Voter</b-button>
              </b-col>
            </b-row>
          </b-card-text>
        </b-card>
        <!-- Hidden Registration Card --> 
        <b-card title="New Voter Registration" class="mt-3" bg-variant="dark" text-variant="white" v-show="showHideReg">
          <b-card-text>
            <b-form @submit="onSubmit" @reset="onReset">
            <b-container>
              <b-row class="my-2">
                <b-col>
                  <!-- First Name -->
                  <b-form-input
                              id="input-1"
                              v-model="VoterInfo.first"
                              required
                              placeholder="First Name"
                            ></b-form-input>
                </b-col>
                <b-col>
                  <!-- Last Name -->
                    <b-form-input
                              id="input-2"
                              v-model="VoterInfo.last"
                              required
                              placeholder="Last Name"
                            ></b-form-input>
                </b-col>
                <b-col>
                  <!-- dob -->
                  <b-input-group prepend="Date of Birth:" class="mb-2 mr-sm-2 mb-sm-0">
                    <b-form-input
                              id="input-8"
                              v-model="VoterInfo.dob"
                              type="date"
                              required
                              placeholder="Date of Birth"
                            ></b-form-input>
                  </b-input-group>
                </b-col>
              </b-row>
              <b-row class="my-2">
                <b-col>
                    <!-- Street -->
                    <b-form-input
                            id="input-3"
                            v-model="VoterInfo.street"
                            required
                            placeholder="Street"
                          ></b-form-input>
                </b-col>
              </b-row>
              <b-row class="my-2">
                <b-col>
                  <!-- City -->
                  <b-form-input
                            id="input-4"
                            v-model="VoterInfo.city"
                            required
                            placeholder="City"
                          ></b-form-input>
                </b-col>
                <b-col>
                  <!-- State -->
                  <b-form-input
                            id="input-5"
                            v-model="VoterInfo.state"
                            required
                            placeholder="State"
                          ></b-form-input>
                </b-col>
                 <b-col>
                  <!-- Zip -->
                  <b-form-input
                            id="input-6"
                            v-model="VoterInfo.zip"
                            required
                            placeholder="Zip"
                          ></b-form-input>

                </b-col>
              </b-row>
              <b-row class="my-2">
                <b-col>
                  <!-- Email -->
                  <b-form-input
                            id="input-7"
                            v-model="VoterInfo.email"
                            type="email"
                            required
                            placeholder="Email"
                          ></b-form-input>
                </b-col>
              </b-row>
            </b-container>
            <!--Register and Cancel Buttons-->
            <b-row class="mt-5">
                <b-col>
                   <b-button type="submit" variant="primary">Submit</b-button>
                </b-col>
                <b-col>
                   <b-button type="reset" variant="danger">Reset</b-button>
              </b-col>  
            </b-row>
            </b-form>
          </b-card-text>
        </b-card>
        <b-card title="Unique Voter ID" class="mt-3" bg-variant="dark" text-variant="white" v-show="showHideID">
          <b-card-text>
            Your Unique Voter ID (UVID) is {{uvid}} 
          </b-card-text>
          <b-card-text>
            Do not share your UVID with anyone. This ID is unique to you and will be needed to submit your vote.
          </b-card-text>
        </b-card>
      </b-container>
    </div>
  </div>
</template>
  

<script lang="ts">
//Note: Prop and Emit are not used and can be removed if not used before generating the production build
import { AxiosError } from "axios";
import { Component, Prop, Emit, Vue } from "vue-property-decorator";
//import configBlock from "./config-child.vue";
import { RegData } from "./RegData";


@Component //({ components: { "poll-child": configBlock } }) //define the element that will be used in the html above
export default class RegParent extends Vue {
    private VoterInfo: RegData = {
        first: "", 
        last: "", 
        street: "",
        city: "",
        state: "",
        zip: "",
        dob: "",
        email: ""
    };

    uvid = ""; //unique voter ID
    showHideReg = false;
    showHideID = false;
    writeInToggle = false;

    //Backend Server
    //private defaultServerAddress = "https://cors-anywhere.herokuapp.com/https://619egq74ea.execute-api.us-east-1.amazonaws.com/dev/api/registration?";
    private defaultServerAddress = "https://619egq74ea.execute-api.us-east-1.amazonaws.com/dev/api/registration?"; //"http://localhost:3000";
    //private defaultServerAddress = "http://localhost:3000";


    onSubmit(evt: any) {
        evt.preventDefault()
        //create request
        //Last and DOB need to be added
        const suffix =
          "first=" + this.VoterInfo.first + "&" +
          "last=" +  this.VoterInfo.last + "&" +
          "street=" + this.VoterInfo.street + "&" +
          "city=" + this.VoterInfo.city + "&" +
          "state=" + this.VoterInfo.state + "&" +
          "zip=" + this.VoterInfo.zip + "&" +
          "dob=" + this.VoterInfo.dob + "&" +
          "email=" + this.VoterInfo.email;
        //alert(JSON.stringify(this.VoterInfo))
        const endpoint = this.defaultServerAddress + suffix + "/";
        //alert(this.defaultServerAddress + suffix)

        this.$http.get(endpoint)
        .then((response) => {
            console.log(response.data)
            this.uvid = response.data;
            this.showHideReg = false;
            this.showHideID = true;
        })
        .catch((err: AxiosError) => {
          console.log("Failed")

        })

        /*
        this.$http.get(endpoint)
        .then((response) => {
            console.log(response.data)
            this.uvid = response.data;
            this.showHideReg = false;
            this.showHideID = true;
        })
        .catch((err: AxiosError) => {
          console.log("Failed")

        })

        /*this.$http.get(endpoint)
        .then((response) => {
            console.log(response)
        })
        .catch((err: AxiosError) => {
          console.log("Failed")

        })*/
      }

    onReset(evt: any) {
        evt.preventDefault()
        // Reset our form values
        this.VoterInfo.first = "", 
        this.VoterInfo.last = "", 
        this.VoterInfo.street = "",
        this.VoterInfo.city = "",
        this.VoterInfo.state = "",
        this.VoterInfo.zip = "",
        this.VoterInfo.dob = "",
        this.VoterInfo.email = ""

        // Trick to reset/clear native browser form validation state
        this.showHideReg = false
        this.$nextTick(() => {
          this.showHideReg = true
        })
    }

    /*
    onDeleteClass(c: BallotConfig) {
    const x = this.arrBallotConfigData.indexOf(c) //this line would not scale well, but is suitable for prototyping
    this.arrBallotConfigData.splice(x,1);
    }

    createBallot() {
      //cleanup UI
      this.showHideConfig = false;

      const endpoint = this.defaultServerAddress + "/proposals/"
      //need to package the config in a data structure so that delete will always know the id of the json entry
      const ballot = { 
        id: 1,
        data: this.arrBallotConfigData
      }

      console.log("deleting...")
      //this.deleteAll(); // delete the last config
      this.$http
      .delete(endpoint + "1") 
      .finally(() => { //Placing the post inside finally is important. otherwise the post could overlap with delete
          console.log("posting...")
          this.$http
          .post<BallotConfig[]>(endpoint, ballot) 
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
    /*    }  
        this.arrBallotConfigData.push(newCard);
    }

    reset() {
        this.showHideConfig = false;
        this.writeInToggle = false;
        this.arrBallotConfigData = []; 
    }*/
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  
</style>
