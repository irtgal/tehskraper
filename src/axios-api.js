import axios from 'axios'





const getAPI = axios.create({
    baseURL: 'https://tehskraper.herokuapp.com/',
    timeout: 100000,
    
})

export { getAPI }






