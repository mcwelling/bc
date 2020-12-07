<template>
    <div>
        
        <b-card bg-variant="secondary" text-variant="white">
            <b-row align-h="between">
                <!-- Title -->
                <b-col cols="auto"><strong>Proposal {{cardData.id}} Results</strong></b-col>
            </b-row>
            <b-card-text>
                <b-container>
                    <!-- Description -->
                    <b-row class="my-1">
                        {{cardData.proposal}}
                    </b-row>
                    <hr style="background-color:white"/>
                    <!--Options list-->
                    <b-row v-for="(item, index) in cardResults" :key="index.value">
                        <b-col>
                                {{index}}
                        </b-col>
                        <b-col>
                                {{cardResults[index]}}
                        </b-col>
                    </b-row>
                </b-container>
            </b-card-text>
        </b-card>
    </div>
</template>
  

<script lang="ts">
import { Component, Prop, Emit, Watch, Vue } from "vue-property-decorator";
import { BallotData, BallotResults } from "./BallotData";

@Component
export default class EventsChild extends Vue {

    @Prop() private cardData!: BallotData; 
    @Prop() private cardResults!: [];

    private arrResults = [];

    test(){
        console.log(this.cardResults)
    }
    private cardDataChanged = false
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>

