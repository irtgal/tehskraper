import Vue from 'vue'
import VueRouter from 'vue-router'
import Stories from './views/Stories'


Vue.use(VueRouter)


export default new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes: [
        {path: '/', name:'home', component: Stories},
        {path: '/page/:page_name/', component: Stories},
        {path: '/saved/', component: Stories},
        {path: '/search/:query/', component: Stories},
    ]
})


