import { createStore } from 'vuex'

export default createStore({
  // 数据定义
  state: {
    ui_state:{
      now_tab:1,
      printer_status:"PRINT_STATE_IDLE",
    },
    
  },
  // vuex 数据过滤，获取
  getters: {
    get_now_tab(state){
      return state.ui_state.now_tab;
    },
    get_now_printer_status(state){
      return state.ui_state.printer_status;
    },
  },
  // 更改更新数据
  mutations: {
    change_tab(state, new_tab){
      state.ui_state.now_tab = new_tab;
      console.log("change_tab in mutations", new_tab);
    },
    change_printer_status(state, new_status){
      state.ui_state.printer_status = new_status;
      console.log("change_printer_status in mutations", new_status);
    },

  },
  // 提交异步操作，提交mutation
  actions: {
    update_now_tab({commit}, data) {
      commit("change_tab", data)
    },
    update_now_status({commit}, data) {
      commit("change_printer_status", data)
    },
  },
  modules: {
  }
})
