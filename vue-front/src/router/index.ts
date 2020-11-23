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
    path: '/layout',
    name: 'Layout',
    component: LayoutView
  },
  {
    path: '/events',
    name: 'Events',
    //component: () => import(/* webpackChunkName: "events" */ '../views/EventsView.vue')
    component: EventView
  },
  {
    path: '/dynamic',
    name: 'Dynamic',
    //component: () => import(/* webpackChunkName: "events" */ '../views/EventsView.vue')
    component: DynamicView
  },
  {
    path: '/webservices',
    name: 'WebServices',
    component: WebServicesView
  },
  {
    path: '/simple_state',
    name: 'SimpleState',
    component: () => import(/* webpackChunkName: "state" */ '../views/AppSimpleState.vue')
  },
  {
    path: '/bc',
    name: 'BC',
    component: () => import(/* webpackChunkName: "state" */ '../views/BCView.vue')
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
