<template>
  <div id="app">
    <div id="nav">
      <!--
      <router-link to="/">Home</router-link> |
      <router-link to="/about">About</router-link> |
      <router-link to="/layout">Layout</router-link> |
      <router-link to="/events">Events</router-link> |
      <router-link to="/dynamic">Dynamic</router-link> |
      <router-link to="/webservices">Web Services</router-link> |
      <router-link to="/simple_state">Simple State</router-link> | -->
      <router-link to="/bc">BC</router-link> |
      <router-link to="/bc2">BC2</router-link> |
      <router-link to="/designer">Ballot Designer</router-link> |
      <router-link to="/voting">Voting Simulator</router-link> |
    </div>
    <router-view/>
  </div>
</template>

<!-- if you change background change color here, change it in index.html too-->
<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #ffffff;
  background-color: #1a1f27; 
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #ffffff;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
