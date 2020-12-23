<template>
    <div id="navbar">
        <div id="nav-expand" v-on:click="toggleNav();"><i class="fas fa-grip-lines"></i></div>
            <div class="topnav">
            <a class="nav-item"><router-link :to="{name: 'home'}" exact><i class="fas fa-home home text-light"></i></router-link></a>
            <section v-bind:class="{ hidden: navHidden }">
            <router-link to="/page/st/" class="nav-item" exact>Slo-tech</router-link>
           <router-link to="/page/mn/" class="nav-item" exact>Monitor</router-link>
            <input class="search-input" type="text" placeholder="Poišči.." name="search" >
            <div class="nav-item nav-saved hover"><i class="fas fa-bookmark text-green"></i></div>
            </section>
        </div>
    </div>
</template>

<script>
export default {
    name: 'Nav',
    data: function() {
        return {
          navHidden: false,
        };
    },
  methods: {
    toggleNav: function(){
      this.navHidden = !this.navHidden
    },
    displayResize: function() {
            if (screen.width < 760){this.navHidden = true} else {this.navHidden = false}
  }   
  },
    created () {
      this.displayResize()
      window.addEventListener("resize", this.displayResize)
      },
    components: {
    },
    
}
</script>

<style scoped>
#navbar {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    background-color: #333;
    z-index: 7000;
}

.topnav {
  margin: 0 10%;
  overflow: hidden;
}

.nav-item {
  float: left;
  display: block;
  text-align: center;
  padding: 14px 16px;
  text-decoration: none;
  font-size: 17px;
  color: white;
}
.nav-saved {
    float: right;
}
.home {
    font-size: 25px;
}
.nav-item:hover {
    color: rgb(210,210,210);
    text-decoration: none;
}

.topnav input[type=text] {
  padding: 6px;
  margin-top: 8px;
  font-size: 17px;
  border: none;
}
.search-input {
    margin-left: 15%;
}
#nav-expand {
    display: none;
    position: absolute;
    right: 20px;
    top: 10px;
    color: white;
    font-size: 25px;
}
@media screen and (max-width: 760px) {
    #nav-expand {
        display: block;
    }
  .topnav {
    float: none;
  }
  .nav-item, .nav-saved, .search-input {
    float: none;
    display: block;
    text-align: center;
    width: 100%;
    margin: 0;
    padding: 14px;
  }
}

</style>