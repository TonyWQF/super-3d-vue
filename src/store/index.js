import { createStore } from 'vuex'

export default createStore({
  // 数据定义
  state: {
    ui_state:{

      now_tab:1,

      is_inited:false,
      movement_operable:true,

      isRemotePaused:false,
      isRemotePrinting:false,
      isGcodeInfoGet:false,


      printer_status:"PRINT_STATE_IDLE",
      print_percent:0,
      print_speed:100,
      print_flowrate:100,
      print_filename:"No Gcode is printing",
      print_preview:"data:image/png;base64,",

      fan:[0,0,0,0,0,0],
      nozzle_pos:[0,0,0,0],

    },
    uploadList:[
      // {id: "upload-item-", filename:"xxx.gcode", upload_percentage:"45"},
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
    isInited(state){
      return state.is_inited;
    },
    isMovementOprable(state){
      return state.movement_operable;
    },
    get_now_pos(state){
      return state.ui_state.nozzle_pos;
    },
    get_fan_speed(state){
      return state.ui_state.fan;
    },
    get_print_speed(state){
      return state.ui_state.print_speed;
    },
    get_print_preview(state){
      return state.ui_state.print_preview;
    },
    get_print_filename(state){
      return state.ui_state.print_filename;
    },
    isRemotePrinting(state){
      return state.ui_state.isRemotePrinting;
    },
    isRemotePaused(state){
      return state.ui_state.isRemotePaused;
    },
    isGcodeInfoGet(state){
      return state.ui_state.isGcodeInfoGet;
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
    change_is_inited(state, new_status){
      state.ui_state.is_inited = new_status;
    },
    change_movement_operable(state, new_status){
      state.ui_state.movement_operable = new_status;
    },
    change_position(state, new_status){
      state.ui_state.nozzle_pos = new_status;
    },
    change_print_speed(state, new_status){
      state.ui_state.print_speed = new_status;
    },
    change_fan_speed(state, new_status){
      state.ui_state.fan = new_status;
    },
    change_print_preview(state, new_status){
      state.ui_state.print_preview = new_status;
    },
    change_print_filename(state, new_status){
      state.ui_state.print_filename = new_status;
    },
    change_isRemotePrinting(state, new_status){
      state.ui_state.isRemotePrinting = new_status;
    },
    change_isRemotePaused(state, new_status){
      state.ui_state.isRemotePaused = new_status;
    },
    change_isGcodeInfoGet(state, new_status){
      state.ui_state.isGcodeInfoGet = new_status;
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
    update_print_percent({commit}, data) {
      commit("change_print_percent", data)
    },
    update_uploadList({commit}, data) {
      commit("change_uploadList", data)
    },
    update_is_inited({commit}, data){
      commit("change_is_inited", data)
    },
    update_movement_operable({commit}, data){
      commit("change_movement_operable", data)
    },
    update_position({commit},data){
      commit("change_position", data);
    },
    update_fan_speed({commit},data){
      commit("change_fan_speed", data);
    },
    update_print_speed({commit},data){
      commit("change_print_speed", data);
    },
    update_print_preview({commit},data){
      commit("change_print_preview", data);
    },
    update_print_filename({commit},data){
      commit("change_print_filename", data);
    },
    update_isRemotePrinting({commit},data){
      commit("change_isRemotePrinting", data);
    },
    update_isRemotePaused({commit},data){
      commit("change_isRemotePaused", data);
    },
    update_isGcodeInfoGet({commit},data){
      commit("change_isGcodeInfoGet", data);
    },
 
  },
  modules: {
  }
})
