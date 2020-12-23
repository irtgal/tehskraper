<template>
    <div id="stories-app">
    <Nav></Nav>
	<div id="stories">
        <h6 id="app-title"><strong>{{ appTitle }}</strong></h6>
		<div v-for="story in stories" v-bind:key="story.id" class="story">
			<div  v-bind:class="{ seen: story.seen }" class="content px-3">
				<small class="text-small">{{ story.date }}</small>
				<h5 v-on:click="openStory(story.id)" class="hover">{{story.title}}</h5>
				<p class="mb-1">{{ story.summary }}</p>
				<small class="text-blue p-1"><strong>{{ story.page }}</strong></small>
			</div>
			<div class="toolbar">
                <!-- fontawesome je buggy, zato je mal grdo -->
				<div v-on:click="toggleSaved(story.id)" v-bind:class="{ hidden: story.saved }" class="save-div">
                    <i class="far fa-bookmark save text-green"></i>
				</div>  
                <div v-on:click="toggleSaved(story.id)" v-bind:class="{ hidden: !story.saved }" class="save-div">
                    <i class="fas fa-bookmark save text-green"></i>
				</div>  

				<div v-on:click="openStory(story.id)" class="visit-div">
					<i class="fas fa-external-link-alt visit text-blue"></i>
				</div>
			</div>
		</div>
	</div>
    </div>
</template>

<script>
import { getAPI } from '../axios-api'
import Nav from '../components/Nav'


export default {
    name: 'Stories',
    components: {
        Nav
    },
    data () {
        return {
            stories: [],
            appTitle: '',
        }
    },
    created () {
        this.getAPIData();

    },
    watch:{
        $route (){
            this.getAPIData();
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
        openStory(id) {
            var clickedStory = this.stories.find(x => x.id === id)
            getAPI.get('/seen/'+ id +'/')
            .then(response => {
                if (response){clickedStory.seen = true}                
            })
            window.open(clickedStory.slug)
        },
        toggleSaved(id) {
            var clickedStory = this.stories.find(x => x.id === id)
            getAPI.get('/save/'+ id +'/')
            .then(response => {
                clickedStory.saved = response.data
            })
        }
    },
    updated(){
        console.log("updated");
    }

    
}
</script>

<style>

#stories-app {
    padding: 10px 10%;
    background-color: rgb(237,240,244);
    font-family: Arial, Helvetica, sans-serif;
}

#app-title {
    background-color: white;
    color: #333;
    border: 1px solid #c5cbd3;
    padding: 10px;
    margin-top: 20px;
    text-align: center;

}
.story {
    background-color: white;
    border: 1px solid #c5cbd3;
    border-bottom: none;
    display: flex;
    flex-direction: row;
}
.story:last-child {
  border-bottom: 1px solid #c5cbd3;
}
.toolbar {
    width: 50px;
    border-left: 1px solid #c5cbd3;
    display: flex;
    flex-direction: column;
    color: #7a8185;
}
.save-div, .visit-div {
    flex: 1;
    text-align: center;
    display: flex;
    justify-content: center;
    align-items: center;
    cursor: pointer;
}
.save-div:hover .save, .visit-div:hover .visit {
    filter: brightness(90%);
    cursor: pointer;
}
.visit-div {
    border-top: 1px solid #c5cbd3;
}
.visit, .save {
    font-size: 20px;
}

.content {
    flex: 1;
    padding: 10px;
}
@media screen and (max-width: 600px) {
    #stories-app {
        padding: 10px 3%;
    }
}
.hidden {
    display: none;
}
</style>