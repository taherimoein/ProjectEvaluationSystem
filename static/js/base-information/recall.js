checkRecallFnc = function () {
    var checks = true;
    var errorFields = [];
    if ($("#inputName").val().length == 0)
    {
        checks = false;
        errorFields.push('عنوان فراخوان');
        $("#inputName").addClass('empty');
    }
    else
    {
        $("#inputName").removeClass('empty');
    }
    // if ($("#inputBodynews").val().length == 0)
    // {
    //     checks = false;
    //     errorFields.push('متن فراخوان');
    //     $("#inputBodynews").addClass('empty');
    // }
    // else
    // {
    //     $("#inputBodynews").removeClass('empty');
    // }
    if (!validateDate($("#inputDate").val()))
    {
        checks = false;
        errorFields.push('تاریخ اتمام فراخوان');
        $("#inputDate").addClass('empty');
    }
    else
    {
        $("#inputDate").removeClass('empty');
    }
    
    if (!validateTime($("#inputTime").val()))
    {
        checks = false;
        errorFields.push('زمان اتمام فراخوان');
        $("#inputTime").addClass('empty');
    }
    else
    {
        $("#inputTime").removeClass('empty');
    }
    if ($("#inputcommittee").val() == '0')
    {
        checks = false;
        errorFields.push('کمیته مربوطه');
        $("#inputcommittee").addClass('empty');
    }
    else
    {
        $("#inputcommittee").removeClass('empty');
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