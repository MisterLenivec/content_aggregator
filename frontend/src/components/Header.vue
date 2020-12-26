<template>
  <div class="container-fluid">
    <div class="row">
      <div class="col-12 mx-auto no-gutters">
        <nav class="navbar navbar-expand-sm navbar-light head-foot-back">
          <div id="logo" class="navbar-brand" >LenivaTech</div>
          <button class="navbar-toggler" type="button" data-toggle="collapse"
                  data-target="#navbarTogglerDemo02" aria-controls="navbarTogglerDemo02"
                  aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse" id="navbarTogglerDemo02">
            <ul class="navbar-nav mr-auto mt-2 mt-sm-0 px-3">
              <li class="nav-item px-1">
                <router-link class="nav-link invisible-border"
                             exact-active-class="active active-border" to="/">
                  Home
                </router-link>
              </li>
              <li class="nav-item px-1">
                <router-link class="nav-link invisible-border"
                             exact-active-class="active active-border" to="/about">
                  About
                </router-link>
              </li>
            </ul>
            <ul class="navbar-nav mt-2 mt-sm-0">
              <li class="nav-item">
                <a class="nav-link" href="#">Log in</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="#">Sign up</a>
              </li>
            </ul>
          </div>
        </nav>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Header"
};
</script>

<style scoped>
  .navbar-brand {
    cursor: default;
  }
  #logo {
    font-size: 200%;
    font-family: 'Satisfy', cursive;
    color: #ffddba;
  }
  .invisible-border {
    border: 1px solid transparent;
  }
  .active-border {
    border-color: #ffddba;
  }
</style>
