checkSuggestionExecutionCheck = function () {
    var checks = true;
    var errorFields = [];
    if ($("#inputDescription").val().length == 0)
    {
        checks = false;
        errorFields.push('توضیحات');
        $("#inputDescription").addClass('empty');
    }
    else
    {
        $("#inputDescription").removeClass('empty');
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
checkRecordDetailsExecutiveFieldsFnc = function () {
    var checks = true;
    var errorFields = [];
    if ($("#inputExecutionDescription").val().length == 0)
    {
        checks = false;
        errorFields.push('شرح اجرائیات');
        $("#inputExecutionDescription").addClass('empty');
    }
    else
    {
        $("#inputExecutionDescription").removeClass('empty');
    }
    if ($("#inputExecutorResponse").val().length == 0)
    {
        checks = false;
        errorFields.push('پاسخ مجری');
        $("#inputExecutorResponse").addClass('empty');
    }
    else
    {
        $("#inputExecutorResponse").removeClass('empty');
    }

    if (checks)
    {
        $(".alert-message.error-message.error-fields").hide();
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

        $(".alert-message-text.error-text.error-fields-text").html(errorText);
        $(".alert-message.error-message.error-fields").show();
    }
    return checks;
}
checkExecutorsFnc = function () {
    var checks = true;
    var errorFields = [];
    var executorRows = $(".row-list .added-member");
    var selectedOptions = [];
    var executorEmpty = true;
    for (item of executorRows)
    {
        if ($(item).find("select.executor-select").val() != null)
        {
            selectedOptions.push($(item).find("select.executor-select").val());
        }
        else if ($(".row-list .added-member").length != 1)
        {
            checks = false;
            executorEmpty = false;
            errorFields.push('مجری اضافه شده نمیتواند خالی باشد. در صورت عدم نیاز به مجری جدید سطر مورد نظر را حذف نمائید.');
            $(".row-list .select2-selection--single").addClass('empty');
            break;
        }
    }
    if (executorEmpty)
    {
        var uniqueOptions = [...new Set(selectedOptions)];
        if (selectedOptions.length != uniqueOptions.length)
        {
            checks = false;
            errorFields.push(' وارد کردن مجری تکراری مجاز نمیباشد.');
            $(".row-list .select2-selection--single").addClass('empty');
        }
        else
        {
            $(".row-list .select2-selection--single").removeClass('empty');
        }
    }
    if (checks)
    {
        $(".alert-message.error-message.error-executor-fields").hide();
    }
    else
    {
        var errorItems = '';
        $(".alert-executor-items").html('');
        for (var item of errorFields)
        {
            errorItems += item + '، ';
        }
        var errorText = '';
        if (errorFields.length > 1)
        {
            errorText = '' +
            '<span class="alert-executor-items">' + errorItems + '</span>'
        }
        else {
            errorItems = errorItems.substr(0, errorItems.length - 2) + ' ';
            errorText = '' +
            '<span class="alert-executor-items">' + errorItems + '</span>'
        }

        $(".alert-message-text.error-text.error-executor-fields-text").html(errorText);
        $(".alert-message.error-message.error-executor-fields").show();
    }
    return checks;
}
checkPercentFnc = function () {
    var checks = true;
    var errorFields = [];
    var percentRows = $(".row-list .percent-row");
    var sum = 0;
    for (item of percentRows)
    {
        sum += parseInt($(item).find("input").val());
    }
    if (sum != 100)
    {
        checks = false;
        errorFields.push('جمع درصدهای مشارکت باید 100 باشد.');
        $(".row-list .percent-row").find('input').addClass('empty');
    }
    else
    {
        $(".row-list .percent-row").find('input').removeClass('empty')
        if ($(".row-list > .added-member").length == 1)
        {
            if($(".row-list .percent-row").find('input').val() != 100)
            {
                checks = false;
                errorFields.push('درصد پیشنهاد فردی بایستی 100 باشد.');
                $(".row-list .percent-row").find('input').addClass('empty');
            }
            else
            {
                $(".row-list .percent-row").find('input').removeClass('empty');
            }
        }
    }
    if (checks)
    {
        $(".alert-message.error-message.error-percent-fields").hide();
    }
    else
    {
        var errorItems = '';
        $(".alert-percent-items").html('');
        for (var item of errorFields)
        {
            errorItems += item + '، ';
        }
        var errorText = '';
        if (errorFields.length > 1)
        {
            errorText = '' +
            '<span class="alert-percent-items">' + errorItems + '</span>'
        }
        else {
            errorItems = errorItems.substr(0, errorItems.length - 2) + ' ';
            errorText = '' +
            '<span class="alert-percent-items">' + errorItems + '</span>'
        }
        $(".alert-message-text.error-text.error-percent-fields-text").html(errorText);
        $(".alert-message.error-message.error-percent-fields").show();
    }
    return checks;
}