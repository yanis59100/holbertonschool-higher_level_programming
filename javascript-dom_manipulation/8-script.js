const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';

document.addEventListener('DOMContentLoaded', () => {
    fetch(url)
    .then(response => response.json())
    .then(data => {
        const translate = data.hello;
        const Hello = document.getElementById('hello');

        Hello.textContent = translate;
    });
})