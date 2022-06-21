import Vue from 'vue'
import Vuex from 'vuex'
import movies from './modules/movies'
import accounts from './modules/accounts'
Vue.use(Vuex)
// import createPersistedState from 'vuex-persistedstate';



export default new Vuex.Store({
  modules: { accounts, movies },
//   plugins: [
//     createPersistedState({
//         paths: ["movies","accounts"],
//     }),
// ],
})
