import { setCookie } from '../js/cookies.js';
import { acceptButtonClicked } from '../jquery/show_box.js'


let popup = document.getElementById("popup");
const email = document.getElementById("email_form");

$('#main_button').click(function () {
    email.value = "";
    popup.classList.remove("open_popup");
});


function openPopup() {
    document.querySelector(".img").setAttribute("src", "../static/res/correct.png");
    document.querySelector(".popup h2").innerHTML = "נרשמת בהצלחה !";
    document.querySelector(".popup div").innerHTML = "האיימיל שלך נשמר בהצלחה <br>ברגע זה קובץ אקסל שמכיל בה את הטיסות הכי זולות להיום נשלח למייל שלך.";
    popup.classList.add("open_popup");
}
function warning() {
    document.querySelector(".img").setAttribute("src", "../static/res/cross.png");
    document.querySelector(".popup h2").innerHTML = "מלא את השדה !";
    document.querySelector(".popup div").innerHTML = 'לצערנו אי אפשר לשלוח לך את הקובץ ללא הרשמה.';
    popup.classList.add("open_popup");
}
function confirmweb() {
    document.querySelector(".img").setAttribute("src", "../static/res/correct.png");
    document.querySelector(".popup h2").innerHTML = "נרשמת בהצלחה !";
    document.querySelector(".popup div").innerHTML = "רענן את הדף.";
    popup.classList.add("open_popup");
}

function validateEmail(e) { const a = /^[^\s@]+@[^\s@]+\.[^\s@]+$/; return a.test(e) }


$('#accept-button').on('click', async function (e) {
    e.preventDefault();
    var email = $("#email_form").val();
    var flightType = await acceptButtonClicked();
    if (validateEmail(email) && email != '' && flightType != '') {
        openPopup();
        setCookie(flightType, 'true', 365);
        if (flightType != "web") {
            $.ajax({
                type: 'POST',
                url: '/',
                data: {
                    email: $("#email_form").val(),
                    flightType: flightType,
                }
            });

        }
        else {
            confirmweb()
        }
    }
    else {
        warning();
    }
});





