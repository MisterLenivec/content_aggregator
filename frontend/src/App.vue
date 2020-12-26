<template>
  <div id="app">
    <Header />
    <div class="router-wrapper">
      <router-view />
    </div>
    <Footer />
  </div>
</template>

<style>
@import "assets/css/style.css";
</style>

<script>
import Header from "@/components/Header";
import Footer from "@/components/Footer";
export default {
  components: { Header, Footer }
};
</script>
