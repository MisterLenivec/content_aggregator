<template>
  <Header />
  <router-view />
  <Footer />
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
