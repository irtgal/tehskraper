<template>
    <div id="stories-app">

    <div id="loading"><i  class="fas fa-sync" id="loading-icon"></i></div>
    <usageStats v-if="slug == 'saved'"></usageStats>
	
    <h5 id="app-title" class="text-center">
            <strong class="h-opacity">{{ appTitle }} <b  v-if="slug == 'search'" class="text-green">{{ query() }}</b></strong>
            <i v-show="scrollAble" v-on:click="refreshStories()" class="fas fa-sync" id="refresh"></i>
    </h5>
    <div id="stories">
		<theStory v-for="story in stories" v-bind:key="story.id" :story="story" @removeSaved="removeStory"></theStory>

        <div v-if="!stories.length" id="no-news"><h5><b>Ni novic</b></h5></div>
	</div>
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
    created () {
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
            this.scrollAble = false
            this.getAPIData()
            document.body.scrollTop = document.documentElement.scrollTop = 0
            this.checkSlug()
            this.checkScroll()
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
        getAPIData(refresh = null) {
        getAPI.get(this.$route.path, {
            params: { refresh: refresh }
        })
        .then(response => {
            this.stories = response.data.stories
            this.appTitle = response.data.app_title
            if (refresh) {document.getElementById("loading").style.display = "none"}
        })
        },
        query() {
            let searchQuery = this.$route.path.split('/')[2]
            return decodeURIComponent(searchQuery)
        },
        refreshStories() {
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
    padding: 3px;
    padding-right: 6px;
    margin-left: -35px;
    color: #80cde5;
    opacity: 75%;
}
#refresh:hover {
    cursor: pointer;
    opacity: 100%;
}
#no-news {
    position: relative;
    margin:  auto;
    color: #595959;
    font-size: 50px;
    margin: 30vh auto 5vh auto;
    width: 78px;
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