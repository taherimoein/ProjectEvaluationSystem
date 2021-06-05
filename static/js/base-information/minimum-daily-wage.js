checkMinimumDailyWage = function () {
    var checks = true;
    var errorFields = [];
    if (!validateYear($("#inputYear").val()))
    {
        checks = false;
        errorFields.push('سال');
        $("#inputYear").addClass('empty');
    }
    else
    {
        $("#inputYear").removeClass('empty');
    }
    if (!validateDate($("#inputDate").val()))
    {
        checks = false;
        errorFields.push('تاریخ ابلاغیه');
        $("#inputDate").addClass('empty');
    }
    else
    {
        $("#inputDate").removeClass('empty');
    }
    if ($("#inputNumb").val().length == 0)
    {
        checks = false;
        errorFields.push('شماره ابلاغیه');
        $("#inputNumb").addClass('empty');
    }
    else
    {
        $("#inputNumb").removeClass('empty');
    }
    if ($("#inputValue").val().length == 0)
    {
        checks = false;
        errorFields.push('مقدار دستمزد روزانه');
        $("#inputValue").addClass('empty');
    }
    else
    {
        $("#inputValue").removeClass('empty');
    }

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
        if (errorFields.length > 1)
        {
            errorText = '' +
            'فیلدهای ' +
            '<span class="alert-items">' + errorItems + '</span>' +
            'به درستی تکمیل نشده اند. ' +
            'برای اطلاعات بیشتر به راهنمای روبروی هر فیلد ' +
            '(' +
            '<i class="fas fa-info-circle"></i>' +
            ') ' +
            'مراجعه نمائید.'
        }
        else {
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

        $(".alert-message-text.error-text").html(errorText);
        $(".alert-message.error-message").show();
    }
    return checks;
}