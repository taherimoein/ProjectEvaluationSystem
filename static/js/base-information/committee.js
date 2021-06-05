checkCommitteeFnc = function () {
    var checks = true;
    var errorFields = [];
    if ($("#inputTitle").val().length == 0)
    {
        checks = false;
        errorFields.push('عنوان کمیته');
        $("#inputTitle").addClass('empty');
    }
    else
    {
        $("#inputTitle").removeClass('empty');
    }
    if ($("#inputRelevantDeputy").val() == '0')
    {
        checks = false;
        errorFields.push('معاونت مربوطه');
        $("#inputRelevantDeputy").addClass('empty');
    }
    else
    {
        $("#inputRelevantDeputy").removeClass('empty');
    }
    if ($("#inputBoss").val() == null)
    {
        checks = false;
        errorFields.push('رئیس کمیته');
        $("#inputBoss").next('.select2').find('.select2-selection--single').addClass('empty');
    }
    else
    {
        $("#inputBoss").next('.select2').find('.select2-selection--single').removeClass('empty');
    }
    if ($("#inputBossDate").val().length != 0 && !validateDate($("#inputBossDate").val()))
    {
        checks = false;
        errorFields.push('تاریخ عضویت رئیس کمیته');
        $("#inputBossDate").addClass('empty');
    }
    else
    {
        $("#inputBossDate").removeClass('empty');
    }
    if ($("#inputSecretary").val() == null)
    {
        checks = false;
        errorFields.push('دبیر کمیته');
        $("#inputSecretary").next('.select2').find('.select2-selection--single').addClass('empty');
    }
    else
    {
        $("#inputSecretary").next('.select2').find('.select2-selection--single').removeClass('empty');
    }
    if ($("#inputSecretaryDate").val().length != 0 && !validateDate($("#inputSecretaryDate").val()))
    {
        checks = false;
        errorFields.push('تاریخ عضویت دبیر کمیته');
        $("#inputSecretaryDate").addClass('empty');
    }
    else
    {
        $("#inputSecretaryDate").removeClass('empty');
    }
    var memberDateList = $(".member-date");
    var memberDate = true;
    for (var item of memberDateList)
    {
        if ($(item).val().length != 0 && !validateDate($(item).val()))
        {
            $(item).addClass('empty');
            if (memberDate)
            {
                memberDate = false;
                errorFields.push('یک یا چند فیلد تاریخ عضویت از اعضا');
            }
        }
        else
        {
            $(item).removeClass('empty');
        }
    }
    checks = memberDate && checks;
    if (checks)
    {
        $(".alert-message.error-message.main-error").hide();
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

        $(".alert-message-text.error-text.main-error").html(errorText);
        $(".alert-message.error-message.main-error").show();
    }
    return checks;
}
checkCommitteeMembersFnc = function () {
    var checks = true;
    var errorFields = [];
    var committeeRows = $(".committee-members .added-member");
    var selectedOptions = [];
    for (item of committeeRows)
    {
        if ($(item).find("select.committee-member-select").val() != null)
        {
            selectedOptions.push($(item).find("select.committee-member-select").val());
        }
        else
        {
            checks = false;
            errorFields.push('عضو اضافه شده نمیتواند خالی باشد. در صورت عدم نیاز به عضو سطر مورد نظر را حذف نمائید.');
            $(".committee-members .select2-selection--single").addClass('empty');
            break;
        }
    }
    if (checks)
    {
        var uniqueOptions = [...new Set(selectedOptions)];
        if (selectedOptions.length != uniqueOptions.length)
        {
            checks = false;
            errorFields.push(' وارد کردن عضو تکراری مجاز نمیباشد.');
            $(".committee-members .select2-selection--single").addClass('empty');
        }
        else
        {
            $(".committee-members .select2-selection--single").removeClass('empty');
        }
    }
    // for (item of committeeRows)
    // {
    //     var memberDate = $(item).find('.date-type').first();
    //     if (memberDate.val().length != 0 && !validateDate(memberDate.val()))
    //     {
    //         memberDate = false;
    //         $('.date-type').addClass('empty');
    //         errorFields2.push(' یک یا چند فیلد "تاریخ عضویت" از اعضا به درستی تکمیل نشده است برای اطلاعات بیشتر به راهنمای روبروی فیلد ' +
    //         ' (' +
    //         '<i class="fas fa-info-circle"></i>' +
    //         ') ' +
    //         'مراجعه نمائید.');
    //     }
    // }
    if (checks)
    {
        $(".alert-message.error-message.error-committee-fields").hide();
    }
    else
    {
        var errorItems = '';
        $(".alert-committee-items").html('');
        for (var item of errorFields)
        {
            errorItems += item + '، ';
        }
        var errorText = '';
        if (errorFields.length > 1)
        {
            errorText = '' +
            '<span class="alert-committee-items">' + errorItems + '</span>'
        }
        else {
            errorItems = errorItems.substr(0, errorItems.length - 2) + ' ';
            errorText = '' +
            '<span class="alert-committee-items">' + errorItems + '</span>'
        }

        $(".alert-message-text.error-text.error-committee-fields-text").html(errorText);
        $(".alert-message.error-message.error-committee-fields").show();
    }
    return checks;
}