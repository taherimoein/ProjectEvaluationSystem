checkSecretaryPointsFnc = function() {
    var checks = true;
    var errorFields = [];
    var errorFields2 = [];
    if (!validateYear($("#inputSessionYear").val()))
    {
        checks = false;
        errorFields.push('سال گزارش دهی');
        $("#inputSessionYear").addClass('empty');
    }
    else
    {
        $("#inputSessionYear").removeClass('empty');
    }
    if ($("#inputSessionMonth").val() == '0')
    {
        checks = false;
        errorFields.push('ماه گزارش دهی');
        $("#inputSessionMonth").addClass('empty');
    }
    else
    {
        $("#inputSessionMonth").removeClass('empty');
    }
    var percentCount = $(".percent-point");
    var percentCountStatus = true;
    for (var item of percentCount)
    {
        if (!validateZeroToOne($(item).val()))
        {
            $(item).addClass('empty');
            if (percentCountStatus)
            {
                percentCountStatus = false;
                errorFields2.push('امتیاز درصدی');
            }
        }
        else
        {
            $(item).removeClass('empty');
        }
    }
    checks = percentCountStatus;
    if (checks)
    {
        $(".alert-message.error-message").hide();
    }
    else
    {
        var errorItems = '';
        var errorItems2 = '';
        $(".alert-items").html('');
        for (var item of errorFields)
        {
            errorItems += item + '، ';
        }
        for (var item of errorFields2)
        {
            errorItems2 += item + '، ';
        }
        var errorText = '';
        if (errorFields.length > 1)
        {
            errorText = '' +
            'فیلدهای ' +
            '<span class="alert-items">' + errorItems + '</span>';
            if (errorFields2.length > 0)
            {
                errorText += ' یک یا چند فیلد از فیلدهای ' +
                '<span class="alert-items">' + errorItems2 + '</span>';
            }
            errorText += 'به درستی تکمیل نشده اند. ' +
            'برای اطلاعات بیشتر به راهنمای روبروی هر فیلد ' +
            '(' +
            '<i class="fas fa-info-circle"></i>' +
            ') ' +
            'مراجعه نمائید.'
        }
        else if (errorFields.length == 1) {
            errorItems = errorItems.substr(0, errorItems.length - 2) + ' ';
            errorText = '' +
            'فیلد ' +
            '<span class="alert-items">' + errorItems + '</span>';
            if (errorFields2.length > 0)
            {
                errorText += ' و یک یا چند فیلد از فیلدهای ' +
                '<span class="alert-items">' + errorItems2 + '</span>';
            }
            errorText += 'به درستی تکمیل نشده است. ' +
            'برای اطلاعات بیشتر به راهنمای روبروی فیلد ' +
            ' (' +
            '<i class="fas fa-info-circle"></i>' +
            ') ' +
            'مراجعه نمائید.'
        }
        else
        {
            if (errorFields2.length > 0)
            {
                errorText += 'یک یا چند فیلد از فیلدهای ' +
                '<span class="alert-items">' + errorItems2 + '</span>';
                errorText += 'به درستی تکمیل نشده است. ' +
                'برای اطلاعات بیشتر به راهنمای روبروی فیلد ' +
                ' (' +
                '<i class="fas fa-info-circle"></i>' +
                ') ' +
                'مراجعه نمائید.'
            }
        }

        $(".alert-message-text.error-text").html(errorText);
        $(".alert-message.error-message").show();
    }
    return checks;
}