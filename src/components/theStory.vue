<template>
		<div  class="story" v-bind:id="story.id">
            <i v-if="story.new" class="fas fa-circle story-new"></i>
			<div  v-bind:class="{ seen: story.seen }" class="content px-3 break-long-words">
				<small class="text-small m-opacity">{{ story.date }}</small>
				<h5 v-on:click="openStory(story)" class="hover h-opacity">{{story.title}}</h5>
				<p class="mb-1 hover m-opacity" v-on:click="openStory(story)">{{ story.summary }}</p>
				<small class="text-blue p-1 h-opacity"><strong>{{ story.page }}</strong></small>
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
            window.open(item.url)
        },
        toggleSaved(item) {
            var id = item.id
            getAPI.get('/save/'+ id +'/')
            .then(response => {
                item.saved = response.data
            })
            if (this.$route.path === "/saved/"){
                this.$emit('removeSaved', item.id)
            }
        },

    },

    
}
</script>

<style>
.story {
    background-color: #1E1E1E;
    border: 1px solid #333333;
    border-bottom: none;
    display: flex;
    flex-direction: row;
    position: relative;
}
.story:last-child {
  border-bottom: 1px solid #333333;
}
.toolbar {
    width: 50px;
    border-left: 1px solid #333333;
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
.save-div:hover, .visit-div:hover {
    background-color: #1a1a1a;
}
.save-div:hover .save, .visit-div:hover .visit {
    opacity: 75%;
}
.visit-div {
    border-top: 1px solid #333333;
}
.visit, .save {
    font-size: 20px;
}
.content {
    flex: 1;
    padding: 10px;
}
.story-new {
    position: absolute;
    font-size: 9px;
    left: 50%;
    top: 20px;
    color: #80cde5;
    transform: translate(-50%, -50%);
}
.break-long-words {
  overflow-wrap: break-word;
  word-wrap: break-word;
  word-break: break-all;
  word-break: break-word;
  hyphens: auto;
}
.hidden {
    display: none;
}
</style>