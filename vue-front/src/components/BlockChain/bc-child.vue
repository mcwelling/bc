<template>
    <div>
        <b-card :bg-variant="valid ? 'success' : 'danger'" text-variant="white">
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
                        <b-col sm="9">
                        <b-form-textarea 
                        size="sm" 
                        rows="2" 
                        max-rows="3" 
                        v-model="cardData.parenthash" 
                        readonly></b-form-textarea>
                        </b-col>
                    </b-row>
                    <!-- Block ID -->
                    <b-row class="my-1">
                        <b-col sm="3" class="text-left">
                        <label>Block ID:</label>
                        </b-col>
                        <b-col sm="9">
                        <b-form-textarea 
                        size="sm" 
                        rows="2" 
                        max-rows="3" 
                        v-model="cardData.blockid" 
                        readonly></b-form-textarea>
                        </b-col>
                    </b-row>
                    <!-- Data -->
                    <b-row class="my-1">
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
                        <b-col sm="9">
                        <b-form-input 
                        size="sm" 
                        v-model="cardData.nonce"
                        readonly></b-form-input>
                        </b-col>
                    </b-row>
                    <!-- BlockHash -->
                    <b-row class="my-1">
                        <b-col sm="3" class="text-left">
                        <label>Block Hash:</label>
                        </b-col>
                        <b-col sm="9">
                        <b-form-textarea  
                        size="sm" 
                        rows="2" 
                        max-rows="3" 
                        v-model="cardData.blockhash" 
                        readonly></b-form-textarea>
                        </b-col>
                    </b-row>
                    <!-- Mine and Delete Buttons -->
                    <b-container>
                        <hr style="background-color:white"/>
                        <b-row>
                            <b-col >
                            <b-button
                                :disabled="valid"
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
    private valid = true; 
    //private cardDataChanged = false;
    private mined = false;
    private defaultServerAddress = "https://619egq74ea.execute-api.us-east-1.amazonaws.com/dev/api/";

    //@Emit('mine')
    mine() {
        //this.cardDataChanged = false
        this.valid = true
        this.cardData.blockhash = "mining...";
        this.mined = true;
        
        //return this.cardDat

        const voteData = encodeURI(JSON.stringify(this.cardData.data)) 
        //console.log(this.cardData.blockid)
        
        const suffix = "re-mine-block?voter_id=" + this.cardData.blockid + "&ballot=" + voteData + "&parent_hash=" + this.cardData.parenthash;
        //console.log(suffix);
        const endpoint = this.defaultServerAddress + suffix;
        console.log(endpoint)
        //const voteData = JSON.stringify(this.arrBallotData)
        this.$http.get<any>(endpoint)
        .then((response) =>{
          console.log("hash", response.data.blockHash)
          console.log("nonce", response.data.nonce)
          //this.cardDataChanged = false
           this.valid = true
           this.cardData.blockhash = response.data.blockHash;
           this.cardData.nonce = response.data.nonce; 
           this.mined = true;
        })
        .catch((err: AxiosError) =>{
            console.log(err)
        })
    }
    
    @Emit('delete')
    deleteClass() {
        return this.cardData
    }

    @Emit('changed')
    notifyParent(): updateMsg{
        return {index: this.cardIndex, blockhash: this.cardData.blockhash}
    }

    @Watch('cardData', {deep: true})
    onCardDataChanged(){
        
        if(this.mined === true){
            this.mined = false;
            //this.cardDataChanged = false;
        }
        else{
            //this.cardDataChanged = true;
            this.valid = false;
            this.cardData.blockhash = "Invalid"
        }
        this.notifyParent()
    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>

