document.addEventListener('DOMContentLoaded', () => {
  const burgerBtn = document.querySelector('#burger-icon');
  const mobileMenu = document.querySelector('#mobile-menu');
  const mobileSearch = document.querySelector('#mobile-search');
  const mobileSearchForm = document.querySelector('#mobile-search-form');

  burgerBtn.addEventListener('click', () => {
    mobileSearchForm.classList.add('hidden');
    mobileMenu.classList.toggle('hidden');
  });

  mobileSearch.addEventListener('click', () => {
    mobileMenu.classList.add('hidden');
    mobileSearchForm.classList.toggle('hidden');
  });
  

});




