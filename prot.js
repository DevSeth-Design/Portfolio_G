document.addEventListener('DOMContentLoaded', function() {
    console.log('Website loaded and ready!');
});
function toggleMenu() {
    const links = document.querySelector('.hero-links');
    if (links) {
        links.classList.toggle('show');
        console.log("Menu toggled"); // Logs message for debugging 
    } else {
        console.error('Menu links not found');
    }
}

document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('contact-form').addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent the default form submission

        // Form validation
        const name = document.getElementById('name').value.trim();
        const email = document.getElementById('email').value.trim();
        const phone = document.getElementById('phone').value.trim();
        const message = document.getElementById('message').value.trim();

        if (!name || !email || !phone || !message) {
            alert('All fields are required.');
            return;
        }

        // Validate email format
        const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailPattern.test(email)) {
            alert('Please enter a valid email address.');
            return;
        }

        // Validate phone number format (basic validation)
        const phonePattern = /^[0-9\-\+]{9,15}$/;
        if (!phonePattern.test(phone)) {
            alert('Please enter a valid phone number.');
            return;
        }

        // If validation passes, submit the form
        this.submit();
    });
});
document.addEventListener("DOMContentLoaded", function() {
    const projectItems = document.querySelectorAll('.project-item');
    
    projectItems.forEach(item => {
        item.addEventListener('click', function() {
            const target = item.getAttribute('data-target');
            if (target) {
                window.location.href = target;
            }
        });
    });
});

document.querySelectorAll('.website-link').forEach(link => {
    link.addEventListener('click', function(event) {
        if (this.dataset.hosted === "false") {
            event.preventDefault();
            alert("This website is currently not hosted.");
        }
    });
});

document.querySelectorAll('.website-img').forEach(image => {
    image.addEventListener('click', function() {
        this.classList.toggle('enlarged');
    });
});
