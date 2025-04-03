<template>
  <div class="mainbody">
    <h1 class="headtitle">遥感解译平台首页</h1>
    <div>
      <h2 class="">{{ demoStore.helloPinia}}</h2>
    </div>
    <el-button type="primary">你好,这里使用Elemet-Plus</el-button>
  </div>
</template>

<script setup lang="ts">
  import { mainStore} from '../store/index'
  /* 引入storeToRefs */
  import { storeToRefs } from 'pinia'
  //storeToRefs只会关注sotre中数据，不会对方法进行ref包裹

  /* 得到countStore */
  const demoStore =mainStore()
  import axios from 'axios'
  //进行测试接口调用
  const adduser=()=>{
    let formData = new FormData();
    formData.append("username","12345");
    formData.append("password","54321");
    let url = 'http://127.0.0.1:5000/adduser' //访问后端接口的url
    let method = 'post'
    axios({
      method,
      url,
      data: formData,
    }).then(res => {
      alert(res.data)
    });
  }
  adduser()
</script>

<style scoped>
.mainbody {
  height: 6em;
  padding: 1.5em;
  will-change: filter;
  transition: filter 300ms;
}
.headtitle {
    filter: drop-shadow(0 0 2em #646cffaa);
}
</style>

<style lang="scss" scoped>
/* 在此处编写代码 */
.mainbody {
  background: #76cfe5;
}
</style>