document.addEventListener("DOMContentLoaded", function() {
    const menuToggle = document.getElementById("menu-toggle");
    menuToggle.addEventListener("change", function() {
        const menu = document.querySelector(".menu");
        if (menuToggle.checked) {
            menu.style.display = "block";
        } else {
            menu.style.display = "none";
        }
    });
});
