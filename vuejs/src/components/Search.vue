<template>
  <div class="hello s130">
    <form v-on:submit.once="startSearch">
      <div class="inner-form">
        <div class="input-field first-wrap">
          <div class="svg-wrapper">
            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24">
              <path d="M15.5 14h-.79l-.28-.27C15.41 12.59 16 11.11 16 9.5 16 5.91 13.09 3 9.5 3S3 5.91 3 9.5 5.91 16 9.5 16c1.61 0 3.09-.59 4.23-1.57l.27.28v.79l5 4.99L20.49 19l-4.99-5zm-6 0C7.01 14 5 11.99 5 9.5S7.01 5 9.5 5 14 7.01 14 9.5 11.99 14 9.5 14z"></path>
            </svg>
          </div>
          <input id="search" type="text" placeholder="Input the website url"  @change="startSearch()"/>
        </div>
        <div class="input-field second-wrap">
          <button class="btn-search" type="button">Start</button>
        </div>
      </div>
      <span class="info">ex: vnexpress.net</span>
    </form>


    <div class="d-center">
      <div class="table100 ver1 m-b-110" style="width:800px;">
        <div class="table100-head">
          <table>
            <thead>
              <tr>
                <th class="">WORD</th>
                <th class="">COUNT</th>
              </tr>
            </thead>
          </table>
        </div>

        <div class="table100-body">
          <table style="width: 102%;">
            <tbody id="table-content">
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {

  methods: {
    startSearch(){
      axios
      .get('http://127.0.0.1:8000/api/research/?url='+document.getElementById("search").value)
      .then(function(response){
        var data = response.data

        var content = ''
        for(var i=0; i<data['histogram'].length;i++)
            content+=
            `
                <tr>
                <td>${data['histogram'][i]['word']}</td>
                <td>${data['histogram'][i]['count']}</td>
                </tr>
            `

        document.getElementById( 'table-content' ).innerHTML        = content
      })
    },
  }
  
}
</script>

<style>
.d-center {
  display: flex;
  justify-content: center;
  max-height:455px;
  position:absolute;
  margin-top:200px;
}

td {
  text-align: center;
  width: 12%;
}

/* @import url(https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css); */
</style>