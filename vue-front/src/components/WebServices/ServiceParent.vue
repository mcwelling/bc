<template>
  <div>
    <div class="row">
      <b-container>
        <b-card class="col-12" bg-variant="dark" text-variant="white">
          <b-card-text>
            Before you start this demo make sure you have
            <code>json-server</code> installed via <br />
            <code>yarn global add json-server</code> or
            <code>npm install -g json-server</code>
            <br />
            After that run the server from the <code>/server</code> directory
            via
            <br />
            <code>start-test-server.sh</code>
          </b-card-text>
          <b-card-text>
            <b-row class="my-1">
              <b-col sm="2" class="offset-sm-2">
                <label for="server-address">Server Address:</label>
              </b-col>
              <b-col sm="6">
                <b-form-input
                  id="server-address"
                  v-model="defaultServerAddress"
                ></b-form-input>
              </b-col>
            </b-row>
            <b-row class="my-1">
              <b-col sm="2" class="offset-sm-2">
                <label for="pub-id">Pub API:</label>
              </b-col>
              <b-col sm="6">
                <b-input-group prepend="ID:">
                  <b-form-input
                    id="pub-id"
                    type="number"
                    v-model="searchPubId"
                  ></b-form-input>
                  <b-button variant="info" @click="searchById()"
                    >Search</b-button
                  >
                  <b-button variant="primary" class="ml-2" @click="getAll()"
                    >Get All</b-button
                  >
                  <b-button variant="success" class="ml-2" @click="createNew()"
                    >Create Pub</b-button
                  >
                </b-input-group>
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
      </b-container>
    </div>
    <hr />
    <div class="row">
      <!--This loop handles the actual display of the updated array "courseList: CourseType[] = []"-->
      <div
        class="col-sm-6 mb-2"
        v-for="(course, index) in courseList" 
        :key="index"
      >
      <!-- Pass in cards to display and give each child an event called update-class-info
      call "onUpdateClass" if this event occurs-->
        <pub-child
          :card-data="course" 
          @update-class-info="onUpdateClass"
        ></pub-child>
      </div>
    </div>
  </div>
</template>
  

<script lang="ts">
import { Component, Prop, Emit, Vue } from "vue-property-decorator";
import Pub from "./Pub.vue";
import { AxiosResponse, AxiosError } from "axios";
import { CourseType } from "./CoursesType";

@Component({ components: { "pub-child": Pub } })
export default class ServiceParent extends Vue {
  private courseList: CourseType[] = [];
  private defaultServerAddress = "http://localhost:3000";
  private searchPubId = "1";
  private showErrorBanner = false;
  private errorMessage = "";
  private showOkBanner = false;
  private okMessage = "";

  searchById() {
    console.log("searchbyid");
    this.showErrorBanner =  false; //cleanup
    this.showOkBanner =  false; //cleanup
    this.courseList = []; //cleanup
    const endpoint = this.defaultServerAddress + "/courses/" + this.searchPubId; //get data from web server
    //The code below is asynchronous
    this.$http //$ means it's associated with a view, http says it's web based
      .get<CourseType>(endpoint) // CourseTyoe is a stereotype defined in CourseType.ts
      .then((response) => { //runs if the get is successful. Don't have to know when it will finish
        this.okMessage = "Fetched Course with ID: " + this.searchPubId;
        this.showOkBanner = true;
        const result = response.data;
        this.courseList = [result];
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
    this.courseList = [];
    const endpoint = this.defaultServerAddress + "/courses";
    this.$http.get<CourseType[]>(endpoint).then((response) => {
      const result = response.data;
      this.courseList = result;
      this.okMessage = "Fetched All Courses - Total Received: " + this.courseList.length ;
      this.showOkBanner = true;
      console.log(result);
    });
  }

  onUpdateClass(c: CourseType) {
    this.showErrorBanner = false;
    this.showOkBanner =  false;
    this.courseList = [];
    const endpoint = this.defaultServerAddress + "/courses/" + c.id;
    //Same idea as get but it overrides existing data
    //remember c is the argument passed into this function
    this.$http.put<CourseType>(endpoint, c).then((response) => {
      const result = response.data;
      console.log("Updated ", result);
      this.okMessage = "Updated Course with ID: " + c.id + " successfully";
      this.showOkBanner = true;
    });
  }
  createNew() {
    this.showOkBanner =  false;
    this.courseList = [];
    this.errorMessage = "Not Imnplemented Yet";
    this.showErrorBanner = true;
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
