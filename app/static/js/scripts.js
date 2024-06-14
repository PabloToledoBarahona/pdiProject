document.addEventListener("DOMContentLoaded", function() {
    const carouselSlide = document.querySelector(".carousel-slide");
    const carouselImages = document.querySelectorAll(".carousel-slide img");

    let counter = 0;
    const size = carouselImages[0].clientWidth;

    function moveSlide(n) {
        if (n === 1 && counter >= carouselImages.length - 1) {
            counter = -1;
        } else if (n === -1 && counter <= 0) {
            counter = carouselImages.length;
        }
        counter += n;
        carouselSlide.style.transform = "translateX(" + (-size * counter) + "px)";
    }

    setInterval(function() {
        moveSlide(1);
    }, 3000);

    document.querySelector(".prev").addEventListener("click", function() {
        moveSlide(-1);
    });

    document.querySelector(".next").addEventListener("click", function() {
        moveSlide(1);
    });
});


document.addEventListener('DOMContentLoaded', () => {
    const menuToggle = document.getElementById('menu-toggle');
    const menu = document.querySelector('.menu');
    
    menuToggle.addEventListener('change', () => {
        if (menuToggle.checked) {
            menu.style.display = 'block';
        } else {
            menu.style.display = 'none';
        }
    });
});
