<template>
    <div id="stories-app">
    <Nav></Nav>
	<div id="stories">
        <h5 id="app-title" class="text-center">
            <strong>{{ appTitle }} <b  v-if="$route.path.includes('search')" class="text-green">{{ query() }}</b></strong>
            </h5>

		<story v-for="story in stories" v-bind:key="story.id" :story="story"></story>

        <div v-if="!stories" id="no-news"><h5><b>Ni novic</b></h5></div>
	</div>
    </div>
</template>

<script>
import { getAPI } from '../axios-api'
import Nav from '../components/Nav'
import Story from '../components/Story'
export default {
    name: 'Stories',
    components: {
        Nav,
        Story
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
    beforeUpdate (){
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
                console.log("Isnt scrollable")
            } else {
                this.scrollAble = true
            }
        },
        getAPIData() {
        getAPI.get(this.$route.path,)
        .then(response => {
            this.stories = response.data.stories
            this.appTitle = response.data.app_title
            this.checkScroll
        })
        },
        query() {
            this.searchQuery = this.$route.path.split('/')[2]
            return this.searchQuery
        },

        infiniteScroll() {
        window.onscroll = () => {
            let  bottomOfWindow = window.innerHeight + window.pageYOffset >= document.body.offsetHeight
            console.log( this.scrollAble, !this.allLoaded,bottomOfWindow)
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

<style>

#stories-app {
    margin: 10px 10%;
    font-family: Arial, Helvetica, sans-serif;
}

#app-title {                       
    background-color: white;
    border: 1px solid #c5cbd3;
    padding: 10px;
    margin: 30px 0 10px 0;

}
#no-news {
    position: absolute;
    top: 50%; 
    left: 50%;
    transform: translate(-50%, -50%);
    color:  #bfbfbf;
}
#load-div {
    text-align: center;
    font-size: 40px;
    color: #80cde5;;
    margin-top: 30px;
}

@media screen and (max-width: 600px) {
    #stories-app {
        margin: 10px 3%;
    }
}

</style>