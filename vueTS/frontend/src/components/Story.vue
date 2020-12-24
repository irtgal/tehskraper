<template>

		<div  class="story" :id="story.id">
			<div  v-bind:class="{ seen: story.seen }" class="content px-3">
				<small class="text-small">{{ story.date }}</small>
				<h5 v-on:click="openStory(story)" class="hover">{{story.title}}</h5>
				<p class="mb-1">{{ story.summary }}</p>
				<small class="text-blue p-1"><strong>{{ story.page }}</strong></small>
			</div>
			<div class="toolbar">
                <!-- fontawesome je buggy, hence workaround -->
				<div v-on:click="toggleSaved(story)" v-bind:class="{ hidden: story.saved }" class="save-div">
                    <i class="far fa-bookmark save text-green"></i>
				</div>  
                <div v-on:click="toggleSaved(story)" v-bind:class="{ hidden: !story.saved }" class="save-div">
                    <i class="fas fa-bookmark save text-green"></i>
				</div>  

				<div v-on:click="openStory(story)" class="visit-div">
					<i class="fas fa-external-link-alt visit text-blue"></i>
				</div>
			</div>
		</div>
</template>

<script>
import { getAPI } from '../axios-api'


export default {
    name: 'Story',
    props: ['stories', 'story'],
    methods: {
        openStory(item) {
            var id = item.id
            getAPI.get('/seen/'+ id +'/')
            .then(response => {
                if (response){item.seen = true}                
            })
            window.open(item.slug)
        },
        toggleSaved(item) {
            var id = item.id
            getAPI.get('/save/'+ id +'/')
            .then(response => {
                item.saved = response.data
            })
            if (this.$route.path === "/saved/"){
                document.getElementById(item.id).style.display = "none";
            }
        },

    },

    
}
</script>

<style>
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

.hidden {
    display: none;
}
</style>