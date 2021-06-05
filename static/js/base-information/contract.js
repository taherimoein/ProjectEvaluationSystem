checkContractFnc = function () {
    var checks = true;
    var errorFields = [];
    if ($("#inputSubject").val().length == 0 || $("#inputSubject").val().length > 255)
    {
        checks = false;
        errorFields.push('موضوع قرارداد');
        $("#inputSubject").addClass('empty');
    }
    else
    {
        $("#inputSubject").removeClass('empty');
    }
    if ($("#inputCompany").val() == null || $("#inputCompany").val() == $("#inputTargetCompany").val())
    {
        checks = false;
        errorFields.push('شرکت');
        $("#inputCompany").next('.select2').find('.select2-selection--single').addClass('empty');
    }
    else
    {
        $("#inputCompany").next('.select2').find('.select2-selection--single').removeClass('empty');
    }
    if ($("#inputTargetCompany").val() == null || $("#inputCompany").val() == $("#inputTargetCompany").val())
    {
        checks = false;
        errorFields.push('شرکت طرف قرارداد');
        $("#inputTargetCompany").next('.select2').find('.select2-selection--single').addClass('empty');
    }
    else
    {
        $("#inputTargetCompany").next('.select2').find('.select2-selection--single').removeClass('empty');
    }
    if (!validateDate($("#inputStartDate").val()) || !validateDeltaTime(customJalaliToGregorianFnc($("#inputStartDate").val()), customJalaliToGregorianFnc($("#inputEndDate").val())))
    {
        checks = false;
        errorFields.push('تاریخ شروع قرارداد');
        $("#inputStartDate").addClass('empty');
    }
    else
    {
        $("#inputStartDate").removeClass('empty');
    }
    if (!validateDate($("#inputEndDate").val()) || !validateDeltaTime(customJalaliToGregorianFnc($("#inputStartDate").val()), customJalaliToGregorianFnc($("#inputEndDate").val())))
    {
        checks = false;
        errorFields.push('تاریخ پایان قرارداد');
        $("#inputEndDate").addClass('empty');
    }
    else
    {
        $("#inputEndDate").removeClass('empty');
    }
    if ($("#inputFile").val() == undefined || $("#inputFile").val().length == 0)
    {
        checks = false;
        errorFields.push('پیوست');
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