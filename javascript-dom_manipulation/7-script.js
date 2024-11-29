fetch('https://swapi-api.hbtn.io/api/films/?format=json')
.then(response => response.json())
.then(data => {
    const films = data.results;
    const listMovies = document.getElementById('list_movies');
  
films.forEach(film => {
    const listItem = document.createElement('li');

    listItem.textContent = film.title;
    listMovies.appendChild(listItem);
  });
})