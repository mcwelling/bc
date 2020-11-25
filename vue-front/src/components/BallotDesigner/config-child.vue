<template>
    <div>
        <b-card bg-variant="secondary" text-variant="white">
            <b-row align-h="between">
                <!-- Title -->
                <b-col cols="auto" ><strong>Proposal {{cardData.id}}</strong></b-col>
                <!-- Delete Button -->
                <b-col cols="auto" class="mb-2">
                    <b-button
                        variant="danger"
                        size="sm"
                        @click="deleteProposal()"
                        >X</b-button>
                </b-col>
            </b-row>
            <b-card-text>
                <b-container>
                    <!-- Description -->
                    <b-row class="my-1">
                        <b-form-textarea 
                        size="sm" v-model="cardData.description" 
                        placeholder="Enter a description of the proposal here."></b-form-textarea>
                    </b-row>
                    <hr style="background-color:white"/>
                    <!--Options list-->
                    <b-row v-for="(i,index) in cardData.options" :key="index">
                        <b-form-input size="sm" v-model="cardData.options[index]" placeholder="Option..."> </b-form-input>
                    </b-row>
                    <!--Add options button-->
                    <b-row class="my-1">
                        <b-button
                            variant="primary"
                            size="sm"
                            @click="addOption()"
                            >Add Option</b-button>
                    </b-row>
                </b-container>
            </b-card-text>
        </b-card>
    </div>
</template>
  

<script lang="ts">
import { Component, Prop, Emit, Watch, Vue } from "vue-property-decorator";
import { BallotData } from "./BallotData";

@Component
export default class EventsChild extends Vue {

    @Prop() private cardData!: BallotData; //!: means can't be null
    private cardDataChanged = false

    @Emit('delete')
    deleteProposal() {
        return this.cardData
    }

    /*@Watch('cardData', {immediate: false, deep: true})
    onCardDataChanged(){
        this.cardDataChanged = true
    }*/

    addOption(){
        this.cardData.options.push("");
    }

}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>

