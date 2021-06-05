checkSecretaryPointsFnc = function () {
    var checks = true;
    var errorFields = [];
    var percentagePointElements = $(".percentage-point");

    var percentage = true;
    for (var item of percentagePointElements)
    {
        if ($(item).val().length == 0)
        {
            $(item).addClass('empty');
            if (percentage)
            {
                errorFields.push('امتیاز درصدی');
                percentage = false;
            }
        }
        else
        {
            $(item).removeClass('empty');
        }
    }
    checks = percentage;
    if (checks)
    {
        $(".alert-message.error-message").hide();
    }
    else
    {
        var errorItems = '';
        $(".alert-items").html('');
        for (var item of errorFields)
        {
            errorItems += item + '، ';
        }
        var errorText = '';
        if (errorFields.length == 1)
        {
            errorItems = errorItems.substr(0, errorItems.length - 2) + ' ';
            errorText = '' +
            'فیلد ' +
            '<span class="alert-items">' + errorItems + '</span>' +
            'به درستی تکمیل نشده است. ' +
            'برای اطلاعات بیشتر به راهنمای روبروی فیلد ' +
            ' (' +
            '<i class="fas fa-info-circle"></i>' +
            ') ' +
            'مراجعه نمائید.'
        }
        errorText = '' +
        'یک یا چند فیلد از فیلدهای ' +
        '<span class="alert-items">' + errorItems + '</span>' +
        'به درستی تکمیل نشده اند. ' +
        'برای اطلاعات بیشتر به راهنمای روبروی هر فیلد ' +
        '(' +
        '<i class="fas fa-info-circle"></i>' +
        ') ' +
        'مراجعه نمائید.'
        $(".alert-message-text.error-text").html(errorText);
        $(".alert-message.error-message").show();
    }
    return checks;
}