$('#open_shadow_box').click(function (event) {
    event.preventDefault();
    $('.all').addClass('blur');
    $('#shadow-box').addClass('open_shadow');
});

async function acceptButtonClicked() {
    $('.all').removeClass('blur');
    $('#shadow-box').removeClass('open_shadow');
    var flightType = $('input[name="flight-type"]:checked').val();
    if (flightType === 'excel') {
        return flightType;
    } else if (flightType === 'web') {
        return flightType;
    }
    else {
        return "";
    }
}

export { acceptButtonClicked };