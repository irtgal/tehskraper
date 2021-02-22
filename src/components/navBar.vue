<template>
    <div id="navbar">
        <div id="nav-expand" v-on:click="toggleNav()"><i class="fas fa-grip-lines"></i></div>
            <div class="topnav h-opacity">
            <router-link :to="{name: 'home'}" class="nav-item" exact v-on:click.native="closeNav()"><i class="far fa-newspaper home text-light"></i></router-link>

            <section v-bind:class="{ hidden: navHidden }">
            
            <div id="more" class="nav-item">
              <i class="fas fa-ellipsis-v px-2"></i>
              <div id="more-content" style="float: left;">
                <router-link to="/stats" class="nav-item px-3 thick" exact v-on:click.native="closeNav()">Statistika <i class="fas fa-chart-pie"></i></router-link>
                <router-link to="/saved/"  class="nav-item nav-saved hover thick"  exact v-on:click.native="closeNav()">
                  Shranjeno <i  class="fas fa-bookmark "></i>
                </router-link>
              </div>
            </div>

            <input @keyup.enter="search()" v-model="searchQuery" class="search-input" v-on:click="preventResize()" @blur="listenResize()" type="text" placeholder="Poišči.." name="search" required>
            <router-link to="/page/st/" class="nav-item px-3 thick" exact v-on:click.native="closeNav()">st</router-link>
            <router-link to="/page/mn/" class="nav-item px-3 thick" exact v-on:click.native="closeNav()">mn</router-link>
            <router-link to="/page/rn/" class="nav-item px-3 thick" exact v-on:click.native="closeNav()">rn</router-link>



            </section>

        </div>
    </div>
</template>

<script>
export default {
    name: 'navBar',
    data: function() {
        return {
          navHidden: false,
          searchQuery: '',
        };
    },
  methods: {
    closeNav: function() {
      document.body.scrollTop = document.documentElement.scrollTop = 0
      if (screen.width < 895){ this.navHidden = true }
    },
    toggleNav: function() {
      this.navHidden = !this.navHidden
    },
    search: function() {
      if (this.searchQuery.length > 0 && ! /(#|\/|\?)+/.test(this.searchQuery)){
        this.$router.push('/search/'+this.searchQuery+'/')
        this.closeNav()
        this.searchQuery = ''
      }
    },
    displayResize: function() {
            if (screen.width < 895){this.navHidden = true} else {this.navHidden = false}
  },
    preventResize: function() {
      window.removeEventListener("resize", this.displayResize)
    },
    listenResize: function() {
      window.addEventListener("resize", this.displayResize)
    }
    },

    created () {
      this.displayResize()
      this.listenResize()
      
      },


}
</script>

<style scoped>
#navbar {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    background-color: #66AE66;
    z-index: 6000;
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
.home {
    font-size: 25px;
}
.nav-item:hover {
    opacity: 80%;
    text-decoration: none;
}
.topnav input[type=text] {
  padding: 6px;
  margin-top: 8px;
  font-size: 17px;
  border: none;
}
.search-input {
  float: right;
  margin-right: 10px;
}
#nav-expand {
    display: none;
    position: absolute;
    right: 20px;
    top: 8px;
    color: white;
    font-size: 25px;
}

#more {
    float: right;
    color: #1E1E1E;
    cursor: pointer;
    position: relative;
    display: inline-block;
    z-index: 7000;
}
#more-content {
  display: none;
  position: absolute;
  right: 0;
  background-color: red;
  min-width: 160px;
  z-index: 7000;
}
#more:hover #more-content {
  display: block;
}
.input-active {
  position: absolute;
  top: 30px;
}


@media screen and (max-width: 895px) {
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
    padding: 12px;
  }
  .search-input {
    margin-bottom: 15px;
  }
}

</style>