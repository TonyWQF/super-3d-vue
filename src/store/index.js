import { createStore } from 'vuex'

export default createStore({
  // 数据定义
  state: {
    ui_state:{
      now_tab:1,
    },
    
  },
  // vuex 数据过滤，获取
  getters: {
    get_now_tab(state){
      return state.ui_state.now_tab;
    },
  },
  // 更改更新数据
  mutations: {
    change_tab(state, new_tab){
      // state.ui_state.now_tab = new_tab;
      console.log("change_tab in mutations", new_tab);
      state.ui_state = { ...state, now_tab: new_tab }
    }
  },
  // 提交异步操作，提交mutation
  actions: {
    update_now_tab({commit}, data) {
      commit("change_tab", data)
    },

  },
  modules: {
  }
})
