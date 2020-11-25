<template>
  <div>
    <div class="row">
      <b-container>
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
                  <b-button variant="success" class="ml-2" @click="createBallot()"
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