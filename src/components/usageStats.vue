<template>
    <div id="stats-app">
    <h5 class="text-center"><strong class="h-opacity">Statistika</strong></h5>
    <div  v-if="dataReady" class="stats-flex">
      <div class="item-flex">
        <pie-chart :data="chartData" :options="chartOptions" id="pie-chart"></pie-chart>
        <small class="m-opacity">Razporejenost ogledanih novic</small>
      </div>
      <div class="item-flex day-avg-div">
        <h1>{{ dayAverage }}</h1>
        <small class="m-opacity">Dnevno povprečje ogledanih novic</small>
      </div>
    </div>

    </div>
</template>

<script>
import  pieChart  from './pie-chart.js'
import { getAPI } from '../axios-api'
export default {
    name: 'usageStats',
    components: {
        pieChart,
    },
    data () {
        return {
      dataReady: false,
      dayAverage: 0,
      chartOptions: {
      },
      chartData: {
        hoverBackgroundColor: "red",
        hoverBorderWidth: 10,
        labels: ["Slo-tech", "Monitor", "Računališke novice"],
        datasets: [
          {
            label: "Data One",
            backgroundColor: ["#71c171", "#80cde5", "#f3bd72"],
            data: [],
          },
        ],
      },
        }
    },
    mounted () {
      this.getStats()
    },
    updated (){
    },
    watch:{
        $route (){
        }
    },
    methods: {
        buildPie (response){
          let stats = response.data
          this.chartData.datasets[0].data = [stats.st_count, stats.mn_count, stats.rn_count]
          this.dataReady = true
        },
        getStats() {
            getAPI.get('/stats/')
            .then(response => {
                if (response){
                  this.buildPie(response)
                  this.dayAverage = response.data.day_avg
                }                
            })
        },
    },

}
</script>

<style scoped>
#stats-app {
    background-color: #1E1E1E;
    padding: 10px;
    margin: 30px 0 10px 0;
    text-align:  center;
}
.stats-flex {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
}
.item-flex {
  flex: 1;
}
#pie-chart {
    width: 15rem;
    margin: auto;
}

@media (max-width: 700px) {
  .stats-flex {
    flex-direction: column;
  }
  .item-flex {
    margin: 10px;
  }
}
</style>