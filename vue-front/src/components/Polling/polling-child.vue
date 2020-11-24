<template>
    <div>
        <!--<b-card :title="'Proposal ' + cardData.id" bg-variant="secondary" text-variant="white"> -->
        <b-card bg-variant="secondary" text-variant="white">
            <b-row align-h="between">
                <b-col cols="auto" ><strong>Proposal {{cardData.id}}</strong></b-col>
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
                        <b-form-input size="sm" v-model="cardData[index]" placeholder="Option..."> </b-form-input>
                    </b-row>
                    <!--Add options button-->
                    <b-row class="my-1">
                        <b-button
                            variant="primary"
                            size="sm"
                            @click="addOption()"
                            >Add Option</b-button>
                    </b-row>
                    <!--
                    <b-container>
                    <hr style="background-color:white"/>
                    <b-row>
                        <b-col>
                        <b-button
                            variant="danger"
                            size="sm"
                            @click="deleteProposal()"
                            >Delete Proposal</b-button>
                        </b-col>
                    </b-row>
                </b-container>  Other Buttons-->
                </b-container>
            </b-card-text>
        </b-card>
    </div>
</template>
  

<script lang="ts">
import { Component, Prop, Emit, Watch, Vue } from "vue-property-decorator";
import { PollData } from "./PollData";

@Component
export default class EventsChild extends Vue {

    @Prop() private cardData!: PollData; //!: means can't be null
    private cardDataChanged = false

    @Emit('delete')
    deleteProposal() {
    return this.cardData
    }

    @Watch('cardData', {immediate: false, deep: true})
    onCardDataChanged(){
        this.cardDataChanged = true
    }

    //Option Creation
    private arrOptions: string[] = [];
    optionCountField = "0";
    optionCount = 0;

    addOption(){
        this.cardData.options.push("");
    }

    @Watch("optionCountField")
    onLoopCountFieldChanged() {
        if (this.optionCountField === "") this.optionCountField = "0";
        if (parseInt(this.optionCountField)<0) this.optionCountField = "0";
        this.optionCount = parseInt(this.optionCountField);
    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>

