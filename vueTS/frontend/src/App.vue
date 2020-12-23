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
body {
    margin: 0 10%;
    background-color: rgb(237,240,244);
    font-family: Arial, Helvetica, sans-serif;
}

.hover:hover {
    cursor: pointer;
    filter: brightness(90%);
}
.bg-green {
    background-color: #95d095;
}
.text-green {
    color: #95d095;
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
    color: #95d6e9;
}
</style>
