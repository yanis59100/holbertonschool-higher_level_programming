const addItemElement = document.getElementById('add_item');
const myList = document.querySelector('.my_list');

addItemElement.addEventListener('click', () => {
  const newItem = document.createElement('li');
  newItem.textContent = 'Item';
  myList.appendChild(newItem);
});
