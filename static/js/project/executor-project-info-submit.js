
checkActivitiesFieldsFnc = function () {
    var checks = true;
    var errorFields = [];
    var activitiesList = $(".row-list .added-task");

    var task = true;
    var startDate = true;
    var endDate = true;
    var executor = true;
    var percent = true;
    var output = true;
    
    var inputField;
    
    for (item of activitiesList)
    {
        inputField = $(item).find("input[val='task']");
        if ($(inputField).val().length == 0)
        {
            $(inputField).addClass('empty');
            if (task)
            {
                errorFields.push('فعالیت');
                task = false;
            }
        }
        else
        {
            $(inputField).removeClass('empty');
        }
        inputField = $(item).find("input[val='start-date']");
        if (!validateDate($(inputField).val()))
        {
            $(inputField).addClass('empty');
            if (startDate)
            {
                errorFields.push('تاریخ شروع');
                startDate = false;
            }
        }
        else
        {
            $(inputField).removeClass('empty');
        }
        inputField = $(item).find("input[val='end-date']");
        if (!validateDate($(inputField).val()))
        {
            $(inputField).addClass('empty');
            if (endDate)
            {
                errorFields.push('تاریخ پایان');
                endDate = false;
            }
        }
        else
        {
            $(inputField).removeClass('empty');
        }
        inputField = $(item).find("select[val='executor']");
        if ($(inputField).val() == null)
        {
            $(inputField).next('.select2').find(".select2-selection--single").addClass('empty');
            if (executor)
            {
                errorFields.push('مسئول انجام');
                executor = false;
            }
        }
        else
        {
            $(inputField).next('.select2').find(".select2-selection--single").removeClass('empty');
        }
        inputField = $(item).find("input[val='percent'");
        if (!validateDigit($(inputField).val()) || parseInt($(inputField).val()) > 100)
        {
            $(inputField).addClass('empty');
            if (percent)
            {
                errorFields.push('درصد مشارکت');
                percent = false;
            }
        }
        else
        {
            $(inputField).removeClass('empty');
        }
        inputField = $(item).find("input[val='outputs']");
        if ($(inputField).val().length == 0)
        {
            $(inputField).addClass('empty');
            if (output)
            {
                errorFields.push('خروجی');
                output = false;
            }
        }
        else
        {
            $(inputField).removeClass('empty');
        }
    }
    checks = task && startDate && endDate && executor && percent && output;
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
        $(".alert-message-text.error-text.error-fields-text").html(errorText);
        $(".alert-message.error-message.error-fields").show();
    }
    return checks;
}

checkExecutorProjectInfoFnc = function () {
    var checks = true;
    var errorFields = [];
    if ($("#inputDisadvantages").val().length == 0)
    {
        checks = false;
        errorFields.push('روش پیشین و معایب آن');
        $("#inputDisadvantages").addClass('empty');
    }
    else
    {
        $("#inputDisadvantages").removeClass('empty');
    }
    if ($("#inputImprovement").val().length == 0)
    {
        checks = false;
        errorFields.push('روش بهبود یافته و مزایای آن');
        $("#inputImprovement").addClass('empty');
    }
    else
    {
        $("#inputImprovement").removeClass('empty');
    }
    var impactCheckbox = $(".impact-checkbox");
    var impactCheckboxCheck = false;
    for (var item of impactCheckbox)
    {
        if ($(item).is(":checked"))
        {
            impactCheckboxCheck = true;
            break;
        }
    }
    if (!impactCheckboxCheck && !$("#customCheck5").is(":checked"))
    {
        checks = false;
        errorFields.push('اثر گذاری پیشنهاد');
    }
    if ($("#customCheck5").is(":checked") && $("#inputCustomCheck5").val().length == 0)
    {
        checks = false;
        errorFields.push('سایر');
        $("#inputCustomCheck5").addClass('empty');
    }
    else
    {
        $("#inputCustomCheck5").removeClass('empty');
    }
    if ($("#inputDomain").val().length == 0)
    {
        checks = false;
        errorFields.push('دامنه اجراء');
        $("#inputDomain").addClass('empty');
    }
    else
    {
        $("#inputDomain").removeClass('empty');
    }
    if ($("#inputApplication-time").val().length == 0)
    {
        checks = false;
        errorFields.push('مواقع كاربرد');
        $("#inputApplication-time").addClass('empty');
    }
    else
    {
        $("#inputApplication-time").removeClass('empty');
    }
    if ($("#inputCost").val().length == 0)
    {
        checks = false;
        errorFields.push('هزینه های انجام پیشنهاد');
        $("#inputCost").addClass('empty');
    }
    else
    {
        $("#inputCost").removeClass('empty');
    }
    if (!validateDigit($("#inputSave").val()) || $("#inputSave").val().length > 15)
    {
        checks = false;
        errorFields.push('محاسبه صرفه جویی/ سود حاصل از اجرا');
        $("#inputSave").addClass('empty');
    }
    else
    {
        $("#inputSave").removeClass('empty');
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
checkTechnicalCommitteePorjectInfoFnc = function () {
    var checks = true;
    var errorFields = [];
    if (!validateDigit($("#inputSave").val()) || $("#inputSave").val().length > 15)
    {
        checks = false;
        errorFields.push('محاسبه صرفه جویی/ سود حاصل از اجرا');
        $("#inputSave").addClass('empty');
    }
    else
    {
        $("#inputSave").removeClass('empty');
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
checkCompleteTaskFnc = function () {
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