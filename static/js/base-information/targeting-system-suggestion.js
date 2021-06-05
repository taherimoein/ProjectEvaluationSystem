checkTargetFnc = function () {
    var checks = true;
    var errorFields = [];
    if (!validateYear($("#inputYear").val()))
    {
        checks = false;
        errorFields.push('سال');
        $("#inputYear").addClass('empty');
    }
    else
    {
        $("#inputYear").removeClass('empty');
    }
    if (!validateFloat($("#inputPerCapitaOfferingSuggestEmployer").val()))
    {
        checks = false;
        errorFields.push('سرانه سال ارائه پیشنهاد کارفرما');
        $("#inputPerCapitaOfferingSuggestEmployer").addClass('empty');
    }
    else
    {
        $("#inputPerCapitaOfferingSuggestEmployer").removeClass('empty');
    }
    if (!validateFloat($("#inputPerCapitaAcceptSuggestEmployer").val()))
    {
        checks = false;
        errorFields.push('سرانه پذیرش پیشنهاد کارفرما');
        $("#inputPerCapitaAcceptSuggestEmployer").addClass('empty');
    }
    else
    {
        $("#inputPerCapitaAcceptSuggestEmployer").removeClass('empty');
    }
    if (!validateFloat($("#inputPerCapitaExecuteSuggestEmployer").val()))
    {
        checks = false;
        errorFields.push('سرانه اجرای پیشنهاد کارفرما');
        $("#inputPerCapitaExecuteSuggestEmployer").addClass('empty');
    }
    else
    {
        $("#inputPerCapitaExecuteSuggestEmployer").removeClass('empty');
    }
    if (!validateFloat($("#inputParticipationRateEmployer").val()))
    {
        checks = false;
        errorFields.push('نرخ مشارکت کارفرما');
        $("#inputParticipationRateEmployer").addClass('empty');
    }
    else
    {
        $("#inputParticipationRateEmployer").removeClass('empty');
    }
    if (!validateFloat($("#inputPerCapitaOfferingSuggestContractor").val()))
    {
        checks = false;
        errorFields.push('سرانه سال ارائه پیشنهاد پیمانکار');
        $("#inputPerCapitaOfferingSuggestContractor").addClass('empty');
    }
    else
    {
        $("#inputPerCapitaOfferingSuggestContractor").removeClass('empty');
    }
    if (!validateFloat($("#inputPerCapitaAcceptSuggestContractor").val()))
    {
        checks = false;
        errorFields.push('سرانه پذیرش پیشنهاد پیمانکار');
        $("#inputPerCapitaAcceptSuggestContractor").addClass('empty');
    }
    else
    {
        $("#inputPerCapitaAcceptSuggestContractor").removeClass('empty');
    }
    if (!validateFloat($("#inputPerCapitaExecuteSuggestContractor").val()))
    {
        checks = false;
        errorFields.push('سرانه اجرای پیشنهاد پیمانکار');
        $("#inputPerCapitaExecuteSuggestContractor").addClass('empty');
    }
    else
    {
        $("#inputPerCapitaExecuteSuggestContractor").removeClass('empty');
    }
    if (!validateFloat($("#inputParticipationRateContractor").val()))
    {
        checks = false;
        errorFields.push('نرخ مشارکت پیمانکار');
        $("#inputParticipationRateContractor").addClass('empty');
    }
    else
    {
        $("#inputParticipationRateContractor").removeClass('empty');
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

checkTargetFilterFnc = function () {
    var checks = true;
    var errorFields = [];
    if (!validateYear($("#inputYear").val()))
    {
        checks = false;
        errorFields.push('سال');
        $("#inputYear").addClass('empty');
    }
    else
    {
        $("#inputYear").removeClass('empty');
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


$(document).ready(function () {
    $(function () {
        $('[data-toggle="tooltip"]').tooltip();
    })
})