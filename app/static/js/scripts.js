window.addEventListener('DOMContentLoaded', event => {

    // Highlight the section headings as you scroll through the page
    const sideNav = document.body.querySelector('#sideNav');
    if (sideNav) {
        new bootstrap.ScrollSpy(document.body, {
            target: '#sideNav',
            rootMargin: '0px 0px -40%',
        });
    };

    function toggleView() {
        var icons = document.getElementById("dev-icons");
        var text = document.getElementById("dev-text");

        if (icons.style.display === "none") {
            icons.style.display = "flex";
            text.style.display = "none";
        } else {
            icons.style.display = "none";
            text.style.display = "block";
        }
    };
});