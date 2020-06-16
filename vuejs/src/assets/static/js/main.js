var vueInstance = new Vue({
    el: '#app',
    data: {
        result: null,
    },
    methods: {
        startSearch(){
            fetch('http://127.0.0.1:8000/api/research/?url='+document.getElementById('search').value)
                .then(response => {
                    return response.json()
                })
                .then(data => {
                    //
                    content = ''
                    for(i=0; i<data['histogram'].length;i++)
                    {
                        pair=data['histogram'][i];
                        content+=
                        `
                            <tr>
                            <td>${pair['word']}</td>
                            <td>${pair['count']}</td>
                            </tr>
                        `
                    }

                    document.getElementById( 'table-content' ).innerHTML        = content;
                    })
                .catch(err => {
                    console.log("Something error here!")
                })
        }
    },
    computed: {
        
    },
})