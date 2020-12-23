<template>
    <div id="stories-app">
    <Nav></Nav>
	<div id="stories">
        <h1>{{ APIData.title}}</h1>
		<div v-for="story in APIData" v-bind:key="story.id" class="story">
			<div class="content px-3">
				<small class="text-small">{{ story.date }}</small>
				<h5>{{story.title}}</h5>
				<p class="mb-1">{{ story.summary }}</p>
				<small class="text-blue p-1"><strong>{{ story.page }}</strong></small>
			</div>
			<div class="toolbar">
				<div class="save-div">
					<i v-if="story.saved == true" class="far fa-bookmark save text-green"></i>
                    <i v-else class="fas fa-bookmark save text-green"></i>
				</div>  
				<div class="visit-div">
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
            APIData: []
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
    }

    
}
</script>

<style>
.stories-app {
    margin: 0 10%;
    background-color: rgb(237,240,244);
    font-family: Arial, Helvetica, sans-serif;
}
#stories {
    margin: 80px 0 20px 0;
}
.story {
    background-color: white;
    border-bottom: 1px solid rgb(227,230,234);
    display: flex;
    flex-direction: row;
}

.toolbar {
    width: 50px;
    border-left: 1px solid rgb(227,230,234);
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
    border-top: 1px solid rgb(227,230,234);
}
.visit, .save {
    font-size: 20px;
}

.content {
    flex: 1;
    padding: 10px;
}

</style>