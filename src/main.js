import Vue from 'vue'
import App from './App.vue'
import router from './routes.js'
import VueMeta from 'vue-meta'
import 'bootstrap/dist/css/bootstrap.min.css'
import '@fortawesome/fontawesome-free/css/all.css'

Vue.config.productionTip = false

Vue.use(VueMeta)

new Vue({
  router,
  render: h => h(App),
}).$mount('#app')