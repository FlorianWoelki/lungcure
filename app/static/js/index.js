var modal = document.getElementById('id01');
window.onclick = function (event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}

if (document.cookie.split(';').filter((item) => item.trim().startsWith('logged_in=')).length) {
    const signupForm = document.getElementById('sign-up-form');
    signupForm.style.display = 'none';
    const paymentForm = document.getElementById('payment-form');
    paymentForm.style.display = 'block';
}

function checkLoginData() {
    const email = $('#login_email').val();
    const password = $('#login_pswd').val();

    // Really dump mockup data checking
    if (email === 'admin@admin.com' && password === 'admin') {
        document.cookie = 'logged_in=1';
        location.reload();
    }
}