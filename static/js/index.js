let popup = document.getElementById("popup");
const email = document.getElementById("email_form");

function validateEmail(email) {
    // Regular expression to match email format
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

    return emailRegex.test(email);
}
function warning() {
    document.querySelector(".img").setAttribute("src", "../static/res/cross.png");
    document.querySelector(".popup h2").innerHTML = "מלא את השדה !";
    document.querySelector(".popup div").innerHTML = 'לצערנו אי אפשר לשלוח לך את הקובץ ללא הרשמה.';
    popup.classList.add("open_popup");
}
function openPopup() {
    if (email.value != '' && validateEmail(email.value)) {
        document.querySelector(".img").setAttribute("src", "../static/res/correct.png");
        document.querySelector(".popup h2").innerHTML = "נרשמת בהצלחה !";
        document.querySelector(".popup div").innerHTML = "האיימיל שלך נשמר בהצלחה <br>ברגע זה קובץ אקסל שמכיל בה את הטיסות הכי זולות להיום נשלח למייל שלך.";
        popup.classList.add("open_popup");
    }
    else {
        warning()
    }
}
function closePopup() {
    email.value = "";
    popup.classList.remove("open_popup");
}
