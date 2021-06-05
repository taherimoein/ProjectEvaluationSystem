checkSecretarySessionReportFnc = function() {
    var checks = true;
    var errorFields = [];
    var errorFields2 = [];
    if (!validateDigit($("#inputSessionCount").val()))
    {
        checks = false;
        errorFields.push('تعداد جلسات برگزار شده');
        $("#inputSessionCount").addClass('empty');
    }
    else
    {
        $("#inputSessionCount").removeClass('empty');
    }
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
    var presentSessionCount = $(".present-session-count");
    var activityRatio = $(".activity-ratio");
    var presentSessionCountStatus = true;
    var activityRatioStatus = true;
    for (var item of presentSessionCount)
    {
        if (!validateDigit($(item).val()) || (validateDigit($("#inputSessionCount").val()) && parseInt($(item).val()) > parseInt($("#inputSessionCount").val())))
        {
            $(item).addClass('empty');
            if (presentSessionCountStatus)
            {
                presentSessionCountStatus = false;
                errorFields2.push('تعداد جلسات حضور');
            }
        }
        else
        {
            $(item).removeClass('empty');
        }
    }
    for (var item of activityRatio)
    {
        if (!validateZeroToOne($(item).val()))
        {
            $(item).addClass('empty');
            if (activityRatioStatus)
            {
                activityRatioStatus = false;
                errorFields2.push('ضریب فعالیت');
            }
        }
        else
        {
            $(item).removeClass('empty');
        }
    }
    checks = presentSessionCountStatus && activityRatioStatus;
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