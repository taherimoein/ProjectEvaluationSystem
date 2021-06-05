checkLoginFnc = function () {
    var checks = true;
    var errorFields = [];
    if (!validateIranianNationalCode($("#inputNcode").val()))
    {
        checks = false;
        errorFields.push('کد ملی');
        $("#inputNcode").addClass('empty');
    }
    else
    {
        $("#inputNcode").removeClass('empty');
    }
    if ($("#inputPassword").val().length == 0)
    {
        checks = false;
        errorFields.push('رمز عبور');
        $("#inputPassword").addClass('empty');
    }
    else
    {
        $("#inputPassword").removeClass('empty');
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
checkMobileNumberFnc = function () {
    var checks = true;
    var errorFields = [];
    if (!validateMobileNumber($("#inputPhone").val()))
    {
        checks = false;
        errorFields.push('شماره تماس')
        $("#inputPhone").addClass('empty');
    }
    else
    {
        $("#inputPhone").removeClass('empty');
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

        $(".alert-message-text.error-text").html(errorText);
        $(".alert-message.error-message").show();
    }
    return checks;
}
checkMobileNumberNationalCodeFnc = function () {
    var checks = true;
    var errorFields = [];
    if (!validateMobileNumber($("#inputPhone").val()))
    {
        checks = false;
        errorFields.push('شماره تماس')
        $("#inputPhone").addClass('empty');
    }
    else
    {
        $("#inputPhone").removeClass('empty');
    }
    if (!validateIranianNationalCode($("#inputNcode").val()))
    {
        checks = false;
        errorFields.push('کد ملی')
        $("#inputNcode").addClass('empty');
    }
    else
    {
        $("#inputNcode").addClass('empty');
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

        $(".alert-message-text.error-text").html(errorText);
        $(".alert-message.error-message").show();
    }
    return checks;
}
checkAuthCodeFnc = function () {
    var checks = true;
    var errorFields = [];
    if ($("#inputcode").val().length != 6 || !validateDigit($("#inputcode").val()))
    {
        checks = false;
        errorFields.push('کد تایید');
        $("#inputcode").addClass('empty');
    }
    else
    {
        $("#inputcode").removeClass('empty');
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
checkForgotPasswordPasswordsFnc = function () {
    var checks = true;
    var errorFields = [];
    if ($("#inputcode").val().length != 6 || !validateDigit($("#inputcode").val()))
    {
        checks = false;
        errorFields.push('کد تایید');
        $("#inputcode").addClass('empty');
    }
    else
    {
        $("#inputcode").removeClass('empty');
    }
    if (!validatePassword($("#inputPass").val()))
    {
        checks = false;
        errorFields.push('رمز عبور');
        $("#inputPass").addClass('empty');
    }
    else
    {
        $("#inputPass").removeClass('empty');
    }
    if (!validateRepeatPassword($("#inputPass").val(), $("#inputPass2").val()))
    {
        checks = false;
        errorFields.push('تکرار رمز عبور');
        $("#inputPass2").addClass('empty');
    }
    else
    {
        $("#inputPass2").removeClass('empty');
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