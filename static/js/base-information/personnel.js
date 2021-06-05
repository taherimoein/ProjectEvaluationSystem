checkPersonnelFnc = function () {
    var checks = true;
    var errorFields = [];
    
    // Identity Information
    // if ($("#inputFile")[0].files[0] == undefined || !validImageFileType($("#inputFile")[0].files[0]))
    if ($("#inputFile")[0].files[0] != undefined && !validImageFileType($("#inputFile")[0].files[0]))
    {
        checks = false;
        errorFields.push('عکس پروفایل');
    }
    if ($("#inputFName").val().length == 0 || $("#inputFName").val().length > 50)
    {
        checks = false;
        errorFields.push('نام');
        $("#inputFName").addClass('empty');
    }
    else
    {
        $("#inputFName").removeClass('empty');
    }
    if ($("#inputLName").val().length == 0 || $("#inputLName").val().length > 150)
    {
        checks = false;
        errorFields.push('نام خانوادگی');
        $("#inputLName").addClass('empty');
    }
    else
    {
        $("#inputLName").removeClass('empty');
    }
    if ($("#inputFatherName").val().length == 0 || $("#inputFatherName").val().length > 50)
    {
        checks = false;
        errorFields.push('نام پدر');
        $("#inputFatherName").addClass('empty');
    }
    else
    {
        $("#inputFatherName").removeClass('empty');
    }
    if (!validateIranianNationalCode($("#inputNationalCode").val()))
    {
        checks = false;
        errorFields.push('کد ملی');
        $("#inputNationalCode").addClass('empty');
    }
    else
    {
        $("#inputNationalCode").removeClass('empty');
    }
    if (!validateDigit($("#inputBirthCertificateNo").val()) || $("#inputBirthCertificateNo").val().length > 10)
    {
        checks = false;
        errorFields.push('شماره شناسنامه');
        $("#inputBirthCertificateNo").addClass('empty');
    }
    else
    {
        $("#inputBirthCertificateNo").removeClass('empty');
    }

    // Personnel Information
    if ($("#inputGender").val() == '0')
    {
        checks = false;
        errorFields.push('جنسیت');
        $("#inputGender").next('.select2').find('.select2-selection--single').addClass('empty');
    }
    else
    {
        $("#inputGender").next('.select2').find('.select2-selection--single').removeClass('empty');
    }
    if ($("#inputMaritalStatus").val() == '0')
    {
        checks = false;
        errorFields.push('وضعیت تأهل');
        $("#inputMaritalStatus").next('.select2').find('.select2-selection--single').addClass('empty');
    }
    else
    {
        $("#inputMaritalStatus").next('.select2').find('.select2-selection--single').removeClass('empty');
    }
    if ($("#inputNumberOfChildren").val().length != 0 && !validateDigit($("#inputNumberOfChildren").val()))
    {
        checks = false;
        errorFields.push('تعداد فرزندان');
        $("#inputNumberOfChildren").addClass('empty');
    }
    else
    {
        $("#inputNumberOfChildren").removeClass('empty');
    }
    if (!validateDate($("#inputBirthDate").val()))
    {
        checks = false;
        errorFields.push('تاریخ تولد');
        $("#inputBirthDate").addClass('empty');
    }
    else
    {
        $("#inputBirthDate").removeClass('empty');
    }
    if ($("#inputBirthPlace").val().length == 0 || $("#inputBirthPlace").val().length > 50)
    {
        checks = false;
        errorFields.push('محل تولد');
        $("#inputBirthPlace").addClass('empty');
    }
    else
    {
        $("#inputBirthPlace").removeClass('empty');
    }
    if ($("#inputDegree").val() == '0')
    {
        checks = false;
        errorFields.push('مقطع تحصیلی');
        $("#inputDegree").next('.select2').find('.select2-selection--single').addClass('empty');
    }
    else
    {
        $("#inputDegree").next('.select2').find('.select2-selection--single').removeClass('empty');
    }

    // Work Information
    if ($("#inputInsuranceNumber").val().length != 10)
    {
        checks = false;
        errorFields.push('شماره بیمه');
        $("#inputInsuranceNumber").addClass('empty');
    }
    else
    {
        $("#inputInsuranceNumber").removeClass('empty');
    }
    
    if ($("#inputRole").val().length == 0 || $("#inputRole").val().length > 50)
    {
        checks = false;
        errorFields.push('سمت سازمانی');
        $("#inputRole").addClass('empty');
    }
    else
    {
        $("#inputRole").removeClass('empty');
    }
    if ($("#inputCompany").val() == null)
    {
        checks = false;
        errorFields.push('شرکت');
        $("#inputCompany").next('.select2').find('.select2-selection--single').addClass('empty');
    }
    else
    {
        $("#inputCompany").next('.select2').find('.select2-selection--single').removeClass('empty');
    }
    if ($("#inputRelevantDeputy").val() == '0')
    {
        checks = false;
        errorFields.push('معاونت');
        $("#inputRelevantDeputy").next('.select2').find('.select2-selection--single').addClass('empty');
    }
    else
    {
        $("#inputRelevantDeputy").next('.select2').find('.select2-selection--single').removeClass('empty');
    }
    if ($("#inputManagement").val() == '0')
    {
        checks = false;
        errorFields.push('مدیریت');
        $("#inputManagement").next('.select2').find('.select2-selection--single').addClass('empty');
    }
    else
    {
        $("#inputManagement").next('.select2').find('.select2-selection--single').removeClass('empty');
    }
    if ($("#inputJobGroup").val() == '0')
    {
        checks = false;
        errorFields.push('گروه شغلی');
        $("#inputJobGroup").next('.select2').find('.select2-selection--single').addClass('empty');
    }
    else
    {
        $("#inputJobGroup").next('.select2').find('.select2-selection--single').removeClass('empty');
    }
    if ($("#inputJob").val() == '0')
    {
        checks = false;
        errorFields.push('عنوان شغل');
        $("#inputJob").next('.select2').find('.select2-selection--single').addClass('empty');
    }
    else
    {
        $("#inputJob").next('.select2').find('.select2-selection--single').removeClass('empty');
    }

    // Communication Information
    if (!validateMobileNumber($("#inputMobileNumber").val()))
    {
        checks = false;
        errorFields.push('شماره همراه');
        $("#inputMobileNumber").addClass('empty');
    }
    else
    {
        $("#inputMobileNumber").removeClass('empty');
    }
    if ($("#inputLocalPhone").val().length != 0 && !validatePhoneNumber($("#inputLocalPhone").val()))
    {
        checks = false;
        errorFields.push('شماره ثابت');
        $("#inputLocalPhone").addClass('empty');
    }
    else
    {
        $("#inputLocalPhone").removeClass('empty');
    }
    if ($("#inputEmail").val().length != 0 && !validateEmail($("#inputEmail").val()))
    {
        checks = false;
        errorFields.push('پست الکترونیکی');
        $("#inputEmail").addClass('empty');
    }
    else
    {
        $("#inputEmail").removeClass('empty');
    }
    if ($("#inputAddress").val().length == 0)
    {
        checks = false;
        errorFields.push('آدرس');
        $("#inputAddress").addClass('empty');
    }
    else
    {
        $("#inputAddress").removeClass('empty');
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
checkChangePasswordFnc = function () {
    var checks = true;
    var errorFields = [];
    if (!validatePassword($("#inputPassword").val()))
    {
        checks = false;
        errorFields.push('رمز عبور');
        $("#inputPassword").addClass('empty');
    }
    else
    {
        $("#inputPassword").removeClass('empty');
    }
    if (!validateRepeatPassword($("#inputPassword").val(), $("#inputRepeatPassword").val()))
    {
        checks = false;
        errorFields.push('تکرار رمز عبور');
        $("#inputRepeatPassword").addClass('empty');
    }
    else
    {
        $("#inputRepeatPassword").removeClass('empty');
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