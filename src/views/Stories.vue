<template>
    <div id="stories-app">
    <navBar></navBar>

    <div id="loading"><i  class="fas fa-sync" id="loading-icon"></i></div>
	
    <h5 id="app-title" class="text-center">
            <strong class="h-opacity">{{ appTitle }} <b  v-if="$route.path.includes('search')" class="text-green">{{ query() }}</b></strong>
            <i v-if="scrollAble" v-on:click="reloadStories()" class="fas fa-sync" id="reload"></i>
    </h5>
    <div id="stories">
		<theStory v-for="story in stories" v-bind:key="story.id" :story="story" @removeSaved="removeStory"></theStory>

        <div v-if="!stories.length" id="no-news"><h5><b>Ni novic</b></h5></div>
	</div>
    </div>
</template>

<script>
import { getAPI } from '../axios-api'
import navBar from '../components/navBar'
import theStory from '../components/theStory'
export default {
    name: 'Stories',
    components: {
        navBar,
        theStory,
    },
    data () {
        return {
            stories: [],
            appTitle: '',
            allLoaded: false,
            scrollAble: true,
        }
    },
    created () {
        this.getAPIData()
        window.addEventListener('scroll', this.infiniteScroll)
        this.checkScroll()
    },
    updated (){
        this.allLoaded = false
    },
    watch:{
        $route (){
            this.scrollAble = false
            this.getAPIData()
            document.body.scrollTop = document.documentElement.scrollTop = 0
            this.checkScroll()
        }
    },
    methods: {
        checkScroll () {
            if (this.$route.path.includes('saved') || this.$route.path.includes('search')) {
                this.scrollAble = false
            } else {
                this.scrollAble = true
            }
        },
        getAPIData(reload = null) {
        getAPI.get(this.$route.path, {
            params: { reload: reload }
        })
        .then(response => {
            this.stories = response.data.stories
            this.appTitle = response.data.app_title
            if (reload) {document.getElementById("loading").style.display = "none"}
        })
        },
        query() {
            let searchQuery = this.$route.path.split('/')[2]
            return searchQuery
        },
        reloadStories() {
            document.getElementById("loading").style.display = "block"
            this.getAPIData(true)
        },
        removeStory(id) {
            let i = this.stories.map(item => item.id).indexOf(id)
            this.stories.splice(i, 1)
        },   

        infiniteScroll() {
        window.onscroll = () => {
            let  bottomOfWindow = window.innerHeight + window.pageYOffset >= document.body.offsetHeight
            if (bottomOfWindow  && this.scrollAble && !this.allLoaded) {
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

<style scoped>

#stories-app {
    margin: 10px 10%;
    font-family: Arial, Helvetica, sans-serif;
}
#app-title {                       
    background-color: #1E1E1E;
    padding: 10px 10px 10px 45px;
    margin: 30px 0 10px 0;

}
#reload {
    float: right;
    padding: 3px;
    padding-right: 6px;
    color: #80cde5;
    opacity: 75%;
}
#reload:hover {
    cursor: pointer;
    opacity: 100%;
}
#no-news {
    position: absolute;
    left: 50%;
    top: 50%;
    -webkit-transform: translateX(-50%);
    transform: translateX(-50%);
    color: #595959;
}
#loading {
    display: none;
    position:fixed;
    padding:0;
    margin:0;
    top:0;
    left:0;
    width: 100%;
    height: 100%;
    background:rgba(255,255,255,0.1);
    z-index: 600;
}
#loading-icon {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    color: #80cde5;
    font-size: 10vh;
    opacity: 0.5;
}
@media screen and (max-width: 600px) {
    #stories-app {
        margin: 10px 3%;
    }
}

</style>