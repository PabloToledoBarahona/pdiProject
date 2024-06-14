document.addEventListener('DOMContentLoaded', function () {
    const track = document.querySelector('.carousel-track');
    const slides = Array.from(track.children);
    const nextButton = document.querySelector('.carousel-button--right');
    const prevButton = document.querySelector('.carousel-button--left');

    let currentIndex = 0;

    function updateSlides() {
        const amountToMove = slides[currentIndex].getBoundingClientRect().width * currentIndex;
        track.style.transform = 'translateX(-' + amountToMove + 'px)';
    }

    function showNextSlide() {
        if (currentIndex === slides.length - 1) {
            currentIndex = 0;
        } else {
            currentIndex++;
        }
        updateSlides();
    }

    function showPrevSlide() {
        if (currentIndex === 0) {
            currentIndex = slides.length - 1;
        } else {
            currentIndex--;
        }
        updateSlides();
    }

    nextButton.addEventListener('click', showNextSlide);
    prevButton.addEventListener('click', showPrevSlide);

    setInterval(showNextSlide, 3000);
});
