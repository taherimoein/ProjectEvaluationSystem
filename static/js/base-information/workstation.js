checkWorkstationFnc = function () {
    var checks = true;
    var errorFields = [];
    if ($("#inputWorkstationTitle").val().length == 0 || $("#inputWorkstationTitle").val().length > 255)
    {
        checks = false;
        errorFields.push('عنوان ایستگاه');
        $("#inputWorkstationTitle").addClass('empty');
    }
    else
    {
        $("#inputWorkstationTitle").removeClass('empty');
    }
    if ($("#inputWorkstationType").val() == '0')
    {
        checks = false;
        errorFields.push('نوع ایستگاه');
        $("#inputWorkstationType").next('.select2').find('.select2-selection--single').addClass('empty');
    }
    else
    {
        $("#inputWorkstationType").next('.select2').find('.select2-selection--single').removeClass('empty');
    }

    if ($("#inputOwner").val() == null)
    {
        checks = false;
        errorFields.push('مالکیت اصلی ایستگاه');
        $("#inputOwner").next('.select2').find('.select2-selection--single').addClass('empty');
    }
    else
    {
        $("#inputOwner").next('.select2').find('.select2-selection--single').removeClass('empty');
    }
    if ($("#inputResponsible").val() == null)
    {
        checks = false;
        errorFields.push('مسئولیت اصلی ایستگاه');
        $("#inputResponsible").next('.select2').find('.select2-selection--single').addClass('empty');
    }
    else
    {
        $("#inputResponsible").next('.select2').find('.select2-selection--single').removeClass('empty');
    }
    var sectionElements = $(".main-item");
    var sectionsValidation = true;
    var ownersValidation = true;
    var responsiblesValidation = true;
    for (var item of sectionElements)
    {
        var field = $(item).find('input[val="section"]').first();
        var fieldValue = field.val();

        if (fieldValue.length == 0 || fieldValue.length > 255)
        {
            $(field).addClass('empty');
            if (sectionsValidation)
            {
                errorFields.push('یک یا چند فیلد از فیلدهای عنوان قسمت')
                sectionsValidation = false;
            }
        }
        else
        {
            $(field).removeClass('empty');
        }
        
        field = $(item).find('select[val="owner"]').first();
        fieldValue = field.val();
        
        if (fieldValue == null)
        {
            $(field).next('.select2').find('.select2-selection--single').addClass('empty');
            if (ownersValidation)
            {
                errorFields.push('یک یا چند فیلد از فیلدهای مالکیت اصلی قسمت')
                ownersValidation = false;
            }
        }
        else
        {
            $(field).next('.select2').find('.select2-selection--single').removeClass('empty');
        }

        field = $(item).find('select[val="responsible"]').first();
        fieldValue = field.val();

        if (fieldValue == null)
        {
            $(field).next('.select2').find('.select2-selection--single').addClass('empty');
            if (responsiblesValidation)
            {
                errorFields.push('یک یا چند فیلد از فیلدهای مسئولیت اصلی قسمت')
                responsiblesValidation = false;
            }
        }
        else
        {
            $(field).next('.select2').find('.select2-selection--single').removeClass('empty');
        }
    }
    var firstChecks = checks;
    checks = checks && sectionsValidation && ownersValidation && responsiblesValidation;
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