document.addEventListener("DOMContentLoaded", function () {
    const observer = new MutationObserver(() => {
        const logo = document.querySelector('header .app-logo');
        if (logo && !logo.dataset.customRedirect) {
            logo.dataset.customRedirect = 'true'; // avoid multiple bindings
            logo.addEventListener('click', function (e) {
                e.preventDefault();
                window.location.href = '/app/home'; // set your route
            });
        }
    });

    // Observe DOM changes to catch async loading of logo
    observer.observe(document.body, {
        childList: true,
        subtree: true,
    });
});