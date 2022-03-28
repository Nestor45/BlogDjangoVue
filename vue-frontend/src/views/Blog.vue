<template>
    <div>
        <h1>Este es el Blog</h1>
        <div class="mt-12 max-w-lg mx.auto grid gap-5 lg:grid-cols3 lg:max-w-none">
            <div v-for="posts in APIdata" key="posts.id" class="flex flex-col rounded-lg shadow-lg overflow-hidden">
                <p>{{ posts.title }}</p> 
                {{posts.content}}
            </div>
        </div>
    </div>
</template>

<script>
import {getAPI} from '../axios-api'
export default {
    name: 'Blog',
    data() {
        return {
            APIdata:[]
        }
    },
    created () {
        getAPI.get('/blog/posts/',)
            .then(response => {
                console.log('Post API has recieved data')
                this.APIdata = response.data
            })
            .catch(err => {
                console.log(err)
            })
    }
}
</script>