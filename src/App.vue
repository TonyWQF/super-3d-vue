<template>
  <div id="app">
    <title-header></title-header>
    <tab-selecter></tab-selecter>
    <!-- <h2 id="list-summary" ref="listSummary" tabindex="-1">{{listSummary}}</h2> -->
    <!-- <to-do-form @todo-added="addToDo"></to-do-form>
    
    <ul aria-labelledby="list-summary" class="stack-large">
      <li v-for="item in ToDoItems" :key="item.id">
        <to-do-item
          :label="item.label"
          :done="item.done"
          :id="item.id"
          @checkbox-changed="updateDoneStatus(item.id)"
          @item-deleted="deleteToDo(item.id)"
          @item-edited="editToDo(item.id, $event)">
        </to-do-item>
      </li>
    </ul> -->
  </div>
</template>

<script>
import uniqueId from "lodash.uniqueid";
import TitleHeader from "./components/TitleHeader.vue";
import TabSelecter from './components/TabSelecter.vue';
// import ToDoItem from './components/ToDoItem.vue';
// import ToDoForm from "./components/ToDoForm.vue";

export default {
  name: 'App',
  components:{
    TitleHeader,
    TabSelecter,
    // ToDoItem,
    // ToDoForm,
  },
  data(){
    return{
      ToDoItems:[
        {id:uniqueId("todo-"), label:"iphone", done:false},
        {id:uniqueId("todo-"), label:"huawei", done:false},
        {id:uniqueId("todo-"), label:"XiaoMi", done:true},
        {id:uniqueId("todo-"), label:"Oppo", done:true},
      ],
    };
  },
  methods:{
    addToDo(toDoLabel){
      console.log("To-do added:", toDoLabel);
      this.ToDoItems.push({id:uniqueId('todo-'), label:toDoLabel, done:false});
    },
    updateDoneStatus(toDoId) {
      const toDoToUpdate = this.ToDoItems.find((item) => item.id === toDoId)
      toDoToUpdate.done = !toDoToUpdate.done
    },
    deleteToDo(toDoId) {
      const itemIndex = this.ToDoItems.findIndex((item) => item.id === toDoId);
      this.ToDoItems.splice(itemIndex, 1);
      this.$refs.listSummary.focus();
    },
    editToDo(toDoId, newLabel) {
      const toDoToEdit = this.ToDoItems.find((item) => item.id === toDoId);
      toDoToEdit.label = newLabel;
    },
    send_get(url){
      var xhr = new XMLHttpRequest();
      xhr.open("GET", url, false);
      xhr.onreadystatechange = function() {
        if(xhr.readyState == 4) {
          if(xhr.status == 200) {
            console.log("status == 200");
          }
          else {
            console.log(xhr.status)
          }
        }
        console.log(xhr.responseText)
      }
      xhr.send();
    },
    request_status() {
      var url_get_status = "api/status/machine";
      setInterval(this.send_get(url_get_status),1000);
      // this.send_get(url_get_status);
    },
  },
  computed: {
    listSummary() {
      const numberFinishedItems = this.ToDoItems.filter((item) =>item.done).length
      return `${numberFinishedItems} out of ${this.ToDoItems.length} items completed`
    }
  },
  mounted(){
    this.request_status();
  }
}
</script>

<style>
  /* 全局样式 */
  .btn {
    padding: 0.8rem 1rem 0.7rem;
    border: 0.2rem solid #4d4d4d;
    cursor: pointer;
    text-transform: capitalize;
  }
  .btn__danger {
    color: #fff;
    background-color: #ca3c3c;
    border-color: #bd2130;
  }
  .btn__filter {
    border-color: lightgrey;
  }
  .btn__danger:focus {
    outline-color: #c82333; 
  }
  .btn__primary {
    color: #fff;
    background-color: #000;
  }
  .btn-group {
    display: flex;
    justify-content: space-between;
  }
  .btn-group > * {
    flex: 1 1 auto;
  }
  .btn-group > * + * {
    margin-left: 0.8rem;
  }
  .label-wrapper {
    margin: 0;
    flex: 0 0 100%;
    text-align: center;
  }
  [class*="__lg"] {
    display: inline-block;
    width: 100%;
    font-size: 1.9rem;
  }
  [class*="__lg"]:not(:last-child) {
    margin-bottom: 1rem;
  }
  @media screen and (min-width: 620px) {
    [class*="__lg"] {
      font-size: 2.4rem;
    }
  }
  .visually-hidden {
    position: absolute;
    height: 1px;
    width: 1px;
    overflow: hidden;
    clip: rect(1px 1px 1px 1px);
    clip: rect(1px, 1px, 1px, 1px);
    clip-path: rect(1px, 1px, 1px, 1px);
    white-space: nowrap;
  }
  [class*="stack"] > * {
    margin-top: 0;
    margin-bottom: 0;
  }
  .stack-small > * + * {
    margin-top: 1.25rem;
  }
  .stack-large > * + * {
    margin-top: 2.5rem;
  }
  @media screen and (min-width: 550px) {
    .stack-small > * + * {
      margin-top: 1.4rem;
    }
    .stack-large > * + * {
      margin-top: 2.8rem;
    }
  }
  /* 全局样式结束 */
  #app {
    height: 98%;
    background: #fff;
    margin: 2rem 0 4rem 0;
    padding: 1rem;
    padding-top: 0;
    position: relative;
    box-shadow:
      0 2px 4px 0 rgba(0, 0, 0, 0.2),
      0 2.5rem 5rem 0 rgba(0, 0, 0, 0.1);
  }
  @media screen and (min-width: 550px) {
    #app {
      padding: 4rem;
    }
  }
  #app > * {
    max-width: 100%;
    margin-left: auto;
    margin-right: auto;
  }
  #app > form {
    max-width: 100%;
    width: 100%;
  }
  #app h1 {
    display: block;
    min-width: 50%;
    width: 50%;
    text-align: left;
    float:left;
    margin: 0;
    margin-bottom: 1rem;
  }
</style>

