const updateHeaderElement = document.getElementById('update_header');
const header = document.querySelector('header');

updateHeaderElement.addEventListener('click', () => {
  header.textContent = 'New Header!!!';
});
