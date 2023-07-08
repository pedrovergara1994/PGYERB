const url = 'https://jsonplaceholder.typicode.com/photos';

try {
	 fetch(url)
   .then(res => res.json())
   .then(data => {
    console.log(data)
     
    const d = data.find(da => da.id == 20)
    console.log(d)
      const productoHTML = document.createElement('li');
      document.querySelector("#idimg").innerHTML += 
    '<form>' +
        '<div>' +
            "<li key='"+d.id+"'>"+
            "<img width='30%' height='30%' src='"+ d.url +"'> </img>'"+
            "</li>" +
        '</div>' +
    '</form>';
      

     });
} catch (error) {
	console.error(error);
}

