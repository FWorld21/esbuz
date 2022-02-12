document.addEventListener('DOMContentLoaded', () => {
  const swiper2 = new Swiper('.swiper-reviews', {
    loop: true,
    autoplay: {
      delay: 4000,
      disableOnInteraction: false,
    },
    spaceBetween: 20,
    breakpoints: {
      768: {
        slidesPerView: 1,
        centeredSlides: true,
      },
      1024: {
        slidesPerView: 2,
        spaceBetween: 50,
        centeredSlides: true,
      },
      1230: {
        slidesPerView: 3,
        spaceBetween: 400,
      },
    },
  });
});
