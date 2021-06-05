checkCompanySection1Fnc = function () {
    var checks = true;
    var errorFields = [];
    // if ($("#inputLogo")[0].files[0] != undefined && !validImageFileType($("#inputLogo")[0].files[0]))
    if ($("#inputLogo")[0].files[0] == undefined || !validImageFileType($("#inputLogo")[0].files[0]))
    {
        checks = false;
        errorFields.push('لوگو');
    }
    if ($("#inputTitle").val().length == 0 || $("#inputTitle").val().length > 255)
    {
        checks = false;
        errorFields.push('عنوان شرکت');
        $("#inputTitle").addClass('empty');
    }
    else
    {
        $("#inputTitle").removeClass('empty');
    }
    if ($("#inputCooprationType").val() == 'contractor' && $("#inputParentCompany").val() == null)
    {
        checks = false;
        errorFields.push('شرکت مالک');
        $("#inputParentCompany").next('.select2').find('.select2-selection--single').addClass('empty');
    }
    else
    {
        $("#inputParentCompany").next('.select2').find('.select2-selection--single').removeClass('empty');
    }
    if ($("#inputType").val() == 'legal' && !validateDigit($("#inputRegisterationNumber").val()))
    {
        checks = false;
        errorFields.push('شماره ثبت');
        $("#inputRegisterationNumber").addClass('empty');
    }
    else
    {
        $("#inputRegisterationNumber").removeClass('empty');
    }
    if (!validateIranianNationalCode($("#inputNationalCode").val()))
    {
        checks = false;
        errorFields.push('شماره ملی');
        $("#inputNationalCode").addClass('empty');
    }
    else
    {
        $("#inputNationalCode").removeClass('empty');
    }
    // if ($("#inputCompanyMembers").val().length == 0)
    // {
    //     checks = false;
    //     errorFields.push('لیست کارکنان شرکت');
    //     $("#inputCompanyMembers").next('.select2').find('.select2-selection--multiple').addClass('empty');
    // }
    // else
    // {
    //     $("#inputCompanyMembers").next('.select2').find('.select2-selection--multiple').removeClass('empty');
    // }
    if ($("#inputPhoneNumber").val().length != 0 && !validatePhoneNumber($("#inputPhoneNumber").val()))
    {
        checks = false;
        errorFields.push('شماره ثابت');
        $("#inputPhoneNumber").addClass('empty');
    }
    else
    {
        $("#inputPhoneNumber").removeClass('empty');
    }
    if (!validateMobileNumber($("#inputMobileNumber-1").val()))
    {
        checks = false;
        errorFields.push('تلفن همراه 1');
        $("#inputMobileNumber-1").addClass('empty');
    }
    else
    {
        $("#inputMobileNumber-1").removeClass('empty');
    }
    if ($("#inputMobileNumber-2").val().length > 0 && !validateMobileNumber($("#inputMobileNumber-2").val()))
    {
        checks = false;
        errorFields.push('تلفن همراه 2');
        $("#inputMobileNumber-2").addClass('empty');
    }
    else
    {
        $("#inputMobileNumber-2").removeClass('empty');
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
    if (!validateDigit($("#inputZipCode").val()) || $("#inputZipCode").val().length != 10)
    {
        checks = false;
        errorFields.push('کد پستی');
        $("#inputZipCode").addClass('empty');
    }
    else
    {
        $("#inputZipCode").removeClass('empty');
    }
    if ($("#inputEmail").val().length != 0 && !validateEmail($("#inputEmail").val()))
    {
        checks = false;
        errorFields.push('آدرس الکترونیکی');
        $("#inputEmail").addClass('empty');
    }
    else
    {
        $("#inputEmail").removeClass('empty');
    }
    if (!validateDigit($("#inputSafetyCertificateNumber").val()) || $("#inputSafetyCertificateNumber").val().length > 30)
    {
        checks = false;
        errorFields.push('شماره گواهینامه صلاحیت ایمنی');
        $("#inputSafetyCertificateNumber").addClass('empty');
    }
    else
    {
        $("#inputSafetyCertificateNumber").removeClass('empty');
    }
    if (!validateDate($("#inputSafetyCertificateValidationDate").val()))
    {
        checks = false;
        errorFields.push('تاریخ اعتبار صلاحیت ایمنی');
        $("#inputSafetyCertificateValidationDate").addClass('empty');
    }
    else
    {
        $("#inputSafetyCertificateValidationDate").removeClass('empty');
    }
    if ($("#inputSafetyCertificateFile")[0].files[0] == undefined)
    {
        checks = false;
        errorFields.push('پیوست (نسخه صلاحیت ایمنی)');
    }
    if (checks)
    {
        $(".alert-message.error-message.error-section-1").hide();
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

        $(".alert-message-text.error-text.error-text-section-1").html(errorText);
        $(".alert-message.error-message.error-section-1").show();
    }
    return checks;
}

checkCompanySection2Fnc = function () {
    var checks = true;
    var errorFields = [];
    if ($("#inputCeo").val() == null)
    {
        checks = false;
        errorFields.push('مدیر عامل');
        $("#inputCeo").next('.select2').find('.select2-selection--single').addClass('empty');
    }
    else
    {
        $("#inputCeo").next('.select2').find('.select2-selection--single').removeClass('empty');
    }
    if ($("#inputRepresentative").val() == '0')
    {
        checks = false;
        errorFields.push('نماینده شرکت');
        $("#inputRepresentative").next('.select2').find('.select2-selection--single').addClass('empty');
    }
    else
    {
        $("#inputRepresentative").next('.select2').find('.select2-selection--single').removeClass('empty');
    }
    if (checks)
    {
        $(".alert-message.error-message.error-section-2").hide();
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

        $(".alert-message-text.error-text.error-text-section-2").html(errorText);
        $(".alert-message.error-message.error-section-2").show();
    }
    return checks;
}