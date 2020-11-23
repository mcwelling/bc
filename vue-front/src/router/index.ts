import Vue from 'vue'
import VueRouter, { RouteConfig } from 'vue-router'
import Home from '../views/Home.vue'
//IMPORTANT: Remember to import your components
import LayoutView from '@/views/LayoutView.vue'
import EventView from '@/views/EventsView.vue'
import DynamicView from '@/views/DynamicView.vue'
import WebServiceView from '@/views/WebServicesView.vue'

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
    path: '/web',
    name: 'WebService',
    //component: () => import(/* webpackChunkName: "events" */ '../views/EventsView.vue')
    component: WebServiceView
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
