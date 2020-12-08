<template>
    <div>
        <b-card :bg-variant="cardData.valid ? 'success' : 'danger'" text-variant="white">
            <b-row class="mb-3" align-h="between">
                <!-- Title -->
                <b-col cols="auto"><strong>Block {{cardData.id}}</strong></b-col>
            </b-row>
            <b-card-text>
                <b-container>
                    <!-- ParentHash -->
                    <b-row class="my-1">
                        <b-col sm="3" class="text-left">
                        <label>Parent Hash:</label>
                        </b-col>
                        <b-col sm="9" class="text-left">
                        {{cardData.parenthash}}
                        </b-col>
                    </b-row>
                    <!-- Block ID -->
                    <b-row class="my-3">
                        <b-col sm="3" class="text-left">
                        <label>Block ID:</label>
                        </b-col>
                        <b-col sm="9" class="text-left">
                        {{cardData.blockid}}
                        </b-col>
                    </b-row>
                    <!-- Data -->
                    <b-row class="my-3">
                        <b-col sm="3" class="text-left">
                        <label>Data:</label>
                        </b-col>
                        <b-col sm="9">
                        <b-form-textarea  
                        size="sm" 
                        rows="2" 
                        max-rows="10" 
                        v-model="cardData.data"></b-form-textarea>
                        </b-col>
                    </b-row>
                    <!-- Nonce -->
                    <b-row class="my-1">
                        <b-col sm="3" class="text-left">
                        <label>Nonce:</label>
                        </b-col>
                        <b-col sm="9" class="text-left">
                        {{cardData.nonce}}
                        </b-col>
                    </b-row>
                    <!-- BlockHash -->
                    <b-row class="my-2" >
                        <b-col sm="3" class="text-left">
                        <label>Block Hash:</label>
                        </b-col>
                        <b-col sm="9" class="text-left">
                        {{cardData.blockhash}}
                        </b-col>
                    </b-row>
                    <!-- Mine and Delete Buttons -->
                    <b-container>
                        <hr style="background-color:white"/>
                        <b-row>
                            <b-col >
                            <b-button
                                :disabled="!minable"
                                variant="primary"
                                size="sm"
                                @click="mine()"
                                >Mine</b-button>
                            </b-col>
                        </b-row>
                    </b-container>  
                </b-container>
            </b-card-text>
        </b-card>
    </div>
</template>
  

<script lang="ts">
import { AxiosError } from "axios";
import { Component, Prop, Emit, Watch, Vue } from "vue-property-decorator";
import { BlockData } from "./BlockData";
import { updateMsg } from "./BlockData";

@Component
export default class EventsChild extends Vue {

    @Prop() private cardData!: BlockData; 
    @Prop() private cardIndex!: number;

    private minable = false;
    private mined = false;
    private defaultServerAddress = "https://619egq74ea.execute-api.us-east-1.amazonaws.com/dev/api/";

    mine() {
        this.cardData.blockhash = "mining...";
        this.mined = true;
        
        const voteData = encodeURI(JSON.stringify(this.cardData.data)) 
        const suffix = "re-mine-block?voter_id=" + this.cardData.blockid + "&ballot=" + voteData + "&parent_hash=" + this.cardData.parenthash;
        const endpoint = this.defaultServerAddress + suffix;

        //get new blockhash 
        this.$http.get(endpoint)
        .then((response) =>{
           this.cardData.valid = true
           this.cardData.blockhash = response.data.blockHash;
           this.cardData.nonce = response.data.nonce; 
           this.mined = true;
        })
        .catch((err: AxiosError) =>{
            console.log(err)
        })
    }
    
    @Emit('changed')
    notifyParent(): updateMsg{
        return {index: this.cardIndex, blockhash: this.cardData.blockhash, valid: this.cardData.valid}
    }

    @Watch('cardData', {deep: true})
    onCardDataChanged(){

        if(this.mined === true){
            this.mined = false;
            this.minable = false;
        }
        else{
            if(this.cardData.parentValid === false){
                this.minable = false
            }
            else{
                this.minable = true;
            }
            this.cardData.valid = false;
            this.cardData.blockhash = "Invalid"
        }
        this.notifyParent()
    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>

