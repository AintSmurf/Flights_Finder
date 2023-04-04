
let popup = document.getElementById("popup");


function validateEmail(email) {
    // Regular expression to match email format
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

    return emailRegex.test(email);
}

$('#main_button').click(function () {
    email.value = "";
    popup.classList.remove("open_popup");
});

function openPopup() {
    document.querySelector(".img").setAttribute("src", "../static/res/correct.png");
    document.querySelector(".popup h2").innerHTML = "נשלח בהצלחה !";
    document.querySelector(".popup div").innerHTML = "ברגע זה המייל שלך נשלח נענה בהקדם האפשרי.";
    popup.classList.add("open_popup");
}
function warning() {
    document.querySelector(".img").setAttribute("src", "../static/res/cross.png");
    document.querySelector(".popup h2").innerHTML = "מלא את השדה !";
    document.querySelector(".popup div").innerHTML = 'לצערנו אי אפשר לשלוח הודעה ללא מילוי פרטים.';
    popup.classList.add("open_popup");
}
$('#btn').on('click', async function (e) {
    e.preventDefault();
    var email = $("#email").val();
    var name = $("#name").val();
    var message = $("#message").val();
    console.log(email, name, message)
    if (validateEmail(email) && name != '' && message != '') {
        $.ajax({
            type: 'POST',
            url: '/contact',
            data: {
                email: email,
                name: name,
                message: message
            },
            success: function () {
                $("#contact-user-form")[0].reset();
                openPopup()
            },
            error: function () {
                alert("Oops! Something went wrong. Please try again later.");
            }
        });
    }
    else {
        $("#contact-user-form")[0].reset();
        warning()
    }
});
