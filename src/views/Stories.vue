<template>
    <div id="stories-app">
	
    <h5 id="app-title" class="text-center">
            <strong class="h-opacity">{{ appTitle }} <b  v-if="slug == 'search'" class="text-green">{{ query() }}</b></strong>
            <i v-show="scrollAble" v-on:click="refresh()" class="fas fa-sync" id="refresh"></i>
    </h5>

     
    <div id="stories">
        <transition-group name="fade">
            <theStory  v-for="story in stories" v-bind:key="story.id" :story="story" @removeSaved="removeStory"></theStory>
        </transition-group>
        
        <transition name="fade">
            <div v-if="!stories.length" id="no-news"><h5><b>Ni novic</b></h5></div>
        </transition>
    
	</div>

    <usageStats v-if="slug == 'saved'"></usageStats>


    <div id="loading-div"><i  class="fas fa-sync fa-spin" id="loading-icon"></i></div>

    </div>
</template>

<script>
import { getAPI } from '../axios-api'
import theStory from '../components/theStory'
import usageStats from '../components/usageStats'
export default {
    name: 'Stories',
    components: {
        theStory,
        usageStats,
    },
    data () {
        return {
            stories: [],
            appTitle: '',
            allLoaded: false,
            scrollAble: true,
            slug: '',
        }
    },
    mounted () {
        this.getAPIData()
        window.addEventListener('scroll', this.infiniteScroll)
        this.checkSlug()
        this.checkScroll()
    },
    updated (){
        this.allLoaded = false
    },
    watch:{
        $route (){
            this.stories = []
            this.getAPIData()
            this.checkSlug()
            this.checkScroll()
            document.body.scrollTop = document.documentElement.scrollTop = 0
        }
    },
    methods: {
        checkScroll () {
            var prevented = ['saved', 'search', 'stats']
            if (prevented.includes(this.slug)) {
                this.scrollAble = false
            } else {
                this.scrollAble = true
            }
        },
        checkSlug () {
            this.slug = this.$route.path.split("/").slice(1)[0]
        },
        getAPIData() {
        getAPI.get(this.$route.path)
        .then(response => {
            this.stories = response.data.stories
            this.appTitle = response.data.app_title
        })
        },
        refresh() {
        document.getElementById("loading-div").style.display = "flex"

        getAPI.get(this.$route.path, {
            params: { refresh: true }
        })
        .then(response => {
            this.appTitle = response.data.app_title
            var newStories = response.data.stories.reverse() //v loopu jih nalaga od prvega do zadnjega
            if (newStories.length){
                for (var i = 0; i < newStories.length; i++){
                    var newStory = newStories[i]
                    newStory.new = true
                    this.stories.unshift(newStory)
                }
            }
            document.getElementById("loading-div").style.display = "none"
        })  
        },
        query() {
            let searchQuery = this.$route.path.split('/')[2]
            return decodeURIComponent(searchQuery)
        },
        removeStory(id) {
            let i = this.stories.map(item => item.id).indexOf(id)
            this.stories.splice(i, 1)
        },   

        infiniteScroll() {
        window.onscroll = () => {
            let  bottomOfWindow = window.innerHeight + window.pageYOffset >= document.body.offsetHeight
            if (bottomOfWindow  && this.scrollAble && !this.allLoaded && this.stories.length) {
                let last_story = this.stories[this.stories.length - 1].id
                getAPI.get(this.$route.path, {
                params: { last_story: last_story }
                })
                .then(response => {
                if (response.data.error){this.allLoaded = true}
                else {
                    let new_stories = response.data.stories
                    var i
                    for (i = 0; i < new_stories.length; i++) {this.stories.push(new_stories[i]) }     
                    }
                })
            }
        }

        }
    },

}
</script>

<style>

#stories-app {
    margin: 10px 10%;
    font-family: Arial, Helvetica, sans-serif;
}
#app-title {                       
    background-color: #1E1E1E;
    padding: 10px;
    margin: 30px 0 10px 0;

}
#refresh {
    float: right;
    padding-right: 4px;
    margin-left: -35px;
    color:  #C0C0C0;
    opacity: 100%;
    font-size: 25px;
}
#refresh:hover {
    cursor: pointer;
    opacity: 75%;
}
#stories {
    position: relative;
    min-height: 10vh;
}
#no-news {
    position: absolute;
    top: 6.5vh;
    left: 50%;
    color: #595959;
    font-size: 50px;
    transform: translate(-50%, -50%);    
}
#loading-div {
    display: none;
    justify-content: center;
    align-items: center;
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background:rgba(255,255,255,0.1);
    z-index: 600;
}
#loading-icon {
    display: block;
    position: absolute;
    color: #80cde5;
    font-size: 15vh;
    opacity: 0.7;
}
@media screen and (max-width: 600px) {
    #stories-app {
        margin: 10px 3%;
    }
}

.fade-enter-active, .fade-leave-active {
  transition: all .2s;
}
.fade-enter, .fade-leave-to{
  opacity: 0;
}
.fade-enter-active {
  transition-delay: .2s;
}
</style>