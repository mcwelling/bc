<template>
    <div>
        <b-card bg-variant="secondary" text-variant="white">
            <b-row align-h="between">
                <!-- Title -->
                <b-col cols="auto"><strong>Proposal {{cardData.id}}</strong></b-col>
            </b-row>
            <b-card-text>
                <b-container>
                    <!-- Description -->
                    <b-row class="my-1">
                        {{cardData.proposal}}
                    </b-row>
                    <hr style="background-color:white"/>
                    <!--Options list-->
                    <b-row>
                            <b-form-radio-group style="text-align:left" 
                            v-model="cardData.selected"
                            :options="cardData.options"
                            stacked>
                            </b-form-radio-group>
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

    /*
    @Emit('delete')
    deleteProposal() {
        return this.cardData
    }

    @Watch('cardData', {immediate: false, deep: true})
    onCardDataChanged(){
        this.cardDataChanged = true
    }
    */

}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>

