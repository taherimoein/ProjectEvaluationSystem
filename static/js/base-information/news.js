checkNewsFnc = function () {
    var checks = true;
    var errorFields = [];
    if ($("#inputTitle").val().length == 0)
    {
        checks = false;
        errorFields.push('عنوان');
        $("#inputTitle").addClass('empty');
    }
    else
    {
        $("#inputTitle").removeClass('empty');
    }
    if ($("#inputCategory").val() == '0')
    {
        checks = false;
        errorFields.push('دسته بندی خبر');
        $("#inputCategory").next('.select2').find('.select2-selection--single').addClass('empty');
    }
    else
    {
        $("#inputCategory").next('.select2').find('.select2-selection--single').removeClass('empty');
    }
    if ($("#inputDetails").val().length == 0)
    {
        checks = false;
        errorFields.push('شرح خبر');
        $("#inputDetails").addClass('empty');
    }
    else
    {
        $("#inputDetails").removeClass('empty');
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