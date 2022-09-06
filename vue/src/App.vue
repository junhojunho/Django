<template>
  <div>
   <div>   
      <Header/>
      <Content/>
      <Footer/>
  </div>
  
    </div>
</template>

<script>
// import axios from "axios";
import Header from "./components/Header.vue";
import Content from "./components/Content.vue";
import Footer from "./components/Footer.vue";


export default {
  data: () => {
      return {

      };
  },
  components: {
      Header,
      Content,
      Footer,
  },

  mounted(){
  
  },

  methods:{

  }

  
  
};
</script>

<style></style>