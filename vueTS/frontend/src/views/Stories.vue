<template>
    <div id="stories-app">
    <Nav></Nav>
	<div id="stories">
        <h5 id="app-title"><strong>{{ appTitle }}</strong></h5>

		<story v-for="story in stories" v-bind:key="story.id" :story="story"></story>
		

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
        }
    },
    created () {
        this.getAPIData()
    },
    watch:{
        $route (){
            this.getAPIData();
            document.body.scrollTop = document.documentElement.scrollTop = 0;
        }
    },
    methods: {
        getAPIData(){
        getAPI.get(this.$route.path,)
        .then(response => {
            this.stories = response.data.stories
            this.appTitle = response.data.app_title
        })
        .catch(err => {
            console.log(err)
        })
        },
    },
     
}
</script>

<style>

#stories-app {
    margin: 10px 10%;
    min-height: 91vh;
    font-family: Arial, Helvetica, sans-serif;
}

#app-title {
    background-color: white;
    border: 1px solid #c5cbd3;
    padding: 10px;
    margin-top: 20px;
    text-align: center;

}

@media screen and (max-width: 600px) {
    #stories-app {
        padding: 10px 3%;
    }
}

</style>