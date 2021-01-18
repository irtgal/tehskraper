	 var app = new Vue({
      delimiters: ['[[', ']]'],
      el: '#app',
      data: {
          stories: stories,
      },
      methods: {
          greet: function(name) {
              console.log('Hello from ' + name + '!')
          }
      }
    });