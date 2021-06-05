checkJobGroupFnc = function () {
    var checks = true;
    var errorFields = [];
    if ($("#inputJobGroupTitle").val().length == 0 || $("#inputJobGroupTitle").val().length > 255)
    {
        checks = false;
        errorFields.push('عنوان گروه شغلی');
        $("#inputJobGroupTitle").addClass('empty');
    }
    else
    {
        $("#inputJobGroupTitle").removeClass('empty');
    }
    var jobElements = $(".main-item");
    var jobChecks = true;
    for (var item of jobElements)
    {
        var jobTitleLength = $(item).find('input').first().val().length;
        if (jobTitleLength == 0 || jobTitleLength > 255)
        {
            $(item).find('input').first().addClass('empty');
            if (jobChecks)
            {
                jobChecks = false;
                errorFields.push('یک یا چند فیلد از فیلد های شغل');
            }
        }
        else
        {
            $(item).find('input').first().removeClass('empty');
        }
    }

    var firstChecks = checks;
    checks = checks && jobChecks;

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
            if (!firstChecks)
            {
                errorText = '' +
                'فیلدهای ';
            }
            errorText += '' +
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
            if (!firstChecks)
            {
                errorText = '' +
                'فیلد ';
            }
            errorText += '' +
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