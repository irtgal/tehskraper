<template>
  <div id="app">
  <router-view/>
  <navBar></navBar>
  </div>
</template>

<script>
import navBar from './components/navBar'
export default {
    name: 'App',
    components: {
        navBar,
    },
}
</script>

<style>
#app {
    padding: 50px 0 20px 0;
    background-color: #121212;
    min-height: 100vh;
    color: white;
}
.hover:hover {
    cursor: pointer;
    filter: brightness(90%);
}
.bg-green {
    background-color: #95d095;
}
.text-green {
    color: #71c171;
}
.text-blue {
   color: #80cde5;
}
.text-white {
    color: white;
}
.text-small {
    font-size: 10px;
}
.seen {
    opacity: 38%;
}
.hidden {
  display: none;
}
.h-opacity {
 opacity: 87%;
}
.m-opacity {
    opacity: 60%;
}
.thick {
    font-weight: bold;
}
</style>
