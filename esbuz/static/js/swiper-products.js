const swiper = new Swiper('.swiper-top-products', {
  loop: true,
  spaceBetween: 20,
  autoplay: {
    delay: 2500,
    disableOnInteraction: false,
  },
  slidesPerView: 1,
  centeredSlides: true,

  breakpoints: {
    640: {
      slidesPerView: 2,
      centeredSlides: false,
    },
    768: {
      slidesPerView: 3,
      centeredSlides: false,
    },
    1024: {
      slidesPerView: 4,
      centeredSlides: false,
    },
    1230: {
      slidesPerView: 6,
      spaceBetween: 20,
      centeredSlides: false,
    },
  },
});
