import { createStore } from 'vuex'

export default createStore({
  // 数据定义
  state: {
    ui_state:{
      now_tab:1,
      printer_status:"PRINT_STATE_IDLE",
      print_percent:0,
    },
    uploadList:[
      // {id: "upload-item-", filename:"xxx.gcode", upload_percentage:60},
    ],
    
  },
  // vuex 数据过滤，获取
  getters: {
    get_now_tab(state){
      return state.ui_state.now_tab;
    },
    get_now_printer_status(state){
      return state.ui_state.printer_status;
    },
    get_now_print_percent(state){
      return state.ui_state.print_percent;
    },
    get_now_uploadList(state){
      return state.uploadList;
    },
  },
  // 更改更新数据
  mutations: {
    change_tab(state, new_tab){
      state.ui_state.now_tab = new_tab;
    },
    change_printer_status(state, new_status){
      state.ui_state.printer_status = new_status;
    },
    change_print_percent(state, new_percent){
      state.ui_state.print_percent = new_percent;
    },
    change_uploadList(state, newlist){
      state.uploadList = newlist;
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
    update_now_percent({commit}, data) {
      commit("change_print_percent", data)
    },
    update_uploadList({commit}, data) {
      commit("change_uploadList", data)
    },
  },
  modules: {
  }
})
