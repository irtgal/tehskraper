<template>
  <div id="app">
  <router-view/>
  </div>
</template>

<script>

export default {
  name: 'App',
}
</script>

<style>
#app {
    padding: 50px 0 20px 0;
    background-color: rgb(237,240,244);
    min-height: 100vh;
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
    color: #b3b3b3;
}
.hidden {
  display: none;
}

</style>
