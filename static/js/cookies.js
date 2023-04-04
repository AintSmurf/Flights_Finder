const cookieBanner = document.getElementById('cookie-banner');
const acceptCookiesButton = document.getElementById('accept-cookies');
const rejectCookieButton = document.getElementById('no_cookies');

function setCookie(name, value, days) {
    const date = new Date();
    date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
    const expires = "expires=" + date.toUTCString();
    document.cookie = name + "=" + value + ";" + expires + ";path=/";
}

function getCookie(name) {
    const decodedCookie = decodeURIComponent(document.cookie);
    const cookies = decodedCookie.split(';');
    for (let i = 0; i < cookies.length; i++) {
        var cookie = cookies[i];
        while (cookie.charAt(0) == ' ') {
            cookie = cookie.substring(1);
        }
        if (cookie.indexOf(name) == 0) {
            return cookie.substring(name.length + 1, cookie.length);
        }
    }
    return null;
}


function checkCookie() {
    if (!getCookie('cookie-consent') && !getCookie('no_cookies')) {
        cookieBanner.style.display = 'block';
    } else {
        cookieBanner.style.display = 'none';
    }
}

acceptCookiesButton.addEventListener('click', () => {
    setCookie('cookie-consent', 'true', 365);
    cookieBanner.style.display = 'none';
});

rejectCookieButton.addEventListener('click', (e) => {
    if (!getCookie('no_cookies')) {
        e.preventDefault();
        setCookie('no_cookies', 'true', 365);
        cookieBanner.style.display = 'none';
        $.ajax({
            type: 'POST',
            url: '/remove_user',
        });

    }
});

checkCookie();
export { setCookie };

