import Vue from 'vue'
import VueRouter, { RouteConfig } from 'vue-router'
import Home from '../views/Home.vue'
//IMPORTANT: Remember to import your components
import LayoutView from '@/views/LayoutView.vue'
import EventView from '@/views/EventsView.vue'
import DynamicView from '@/views/DynamicView.vue'
import WebServicesView from '@/views/WebServicesView.vue'

Vue.use(VueRouter)

const routes: Array<RouteConfig> = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  },
  {
    path: '/designer',
    name: 'BallotDesigner',
    component: () => import(/* webpackChunkName: "state" */ '../views/BallotDesigner.vue')
  },
  {
    path: '/voting',
    name: 'VotingSimulator',
    component: () => import(/* webpackChunkName: "state" */ '../views/Voting.vue')
  },
  {
    path: '/register',
    name: 'Register',
    component: () => import(/* webpackChunkName: "state" */ '../views/Register.vue')
  },
  {
    path: '/bcView',
    name: 'BCView',
    component: () => import(/* webpackChunkName: "state" */ '../views/BlockChain.vue')
  },
  {
    path: '/results',
    name: 'results',
    component: () => import(/* webpackChunkName: "state" */ '../views/Results.vue')
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
