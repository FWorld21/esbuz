document.addEventListener('DOMContentLoaded', () => {
  const productBtn = document.querySelector('#product-btn');
  const modalWindow = document.querySelector('#modal');
  const modalExit = document.querySelector('#close');

  productBtn.addEventListener('click', () => {
    modalWindow.classList.remove('hidden');
  });
  modalExit.addEventListener('click', () => {
    modalWindow.classList.add('hidden');
  });
});
