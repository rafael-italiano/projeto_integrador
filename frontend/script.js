document.addEventListener('DOMContentLoaded', function() {
    const slider = document.querySelector('.slider');
    const sliderContainer = slider.querySelector('.slider-container');
    const slides = sliderContainer.querySelectorAll('.slide');
    const prevBtn = slider.querySelector('.arrow.prev');
    const nextBtn = slider.querySelector('.arrow.next');
    let currentIndex = 0;

    function showSlide(index) {
        slides.forEach((slide, i) => {
            if (i === index) {
                slide.style.display = 'block';
            } else {
                slide.style.display = 'none';
            }
        });
    }

    function nextSlide() {
        currentIndex = (currentIndex === slides.length - 1) ? 0 : currentIndex + 1;
        showSlide(currentIndex);
    }

    function prevSlide() {
        currentIndex = (currentIndex === 0) ? slides.length - 1 : currentIndex - 1;
        showSlide(currentIndex);
    }

    nextBtn.addEventListener('click', nextSlide);
    prevBtn.addEventListener('click', prevSlide);

    setInterval(nextSlide, 3000); // Altere o tempo (em milissegundos) para trocar automaticamente os slides
});
