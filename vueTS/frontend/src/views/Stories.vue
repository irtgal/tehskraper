<template>
    <div id="stories-app">
    <Nav></Nav>
	<div id="stories">
        <h6 id="app-title"><strong>Novo</strong></h6>
		<div v-for="story in APIData" v-bind:key="story.id" class="story">
			<div  v-bind:class="{ seen: story.seen }" class="content px-3">
				<small class="text-small">{{ story.date }}</small>
				<h5>{{story.title}}</h5>
				<p class="mb-1">{{ story.summary }}</p>
				<small class="text-blue p-1"><strong>{{ story.page }}</strong></small>
			</div>
			<div class="toolbar">
                <h1>{{ story.saved}}</h1>
				<div v-on:click="toggleSaved(story.id)"  class="save-div">
                    <font-awesome-icon icon="user-secret" />
                    <i v-bind:class="{ hidden: story.saved}" class="far fa-bookmark save text-green"></i>
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
    data () {
        return {
            APIData: [],
        }
    },
    components: {
        Nav
    },
    created () {
        getAPI.get('/index/',)
        .then(response => {
            console.log('getAPI dela')
            this.APIData = response.data
        })
        .catch(err => {
            console.log(err+"NEDELA")
        })
    },
    methods: {
        openStory(id) {
            var clickedStory = this.APIData.find(x => x.id === id)
            clickedStory.seen = true
            window.open(clickedStory.slug)
        },
        toggleSaved(id) {
            var clickedStory = this.APIData.find(x => x.id === id)
            clickedStory.saved = !clickedStory.saved
            console.log(clickedStory.saved)
        }
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