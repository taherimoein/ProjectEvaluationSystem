checkNationalCodeAndMobileFnc = function() {
    var checks = true;
    var errorFields = [];
    if ($("#inputNcode").val().length != 0 && !validateIranianNationalCode($("#inputNcode").val()))
    {
        checks = false;
        errorFields.push('کد ملی');
        $("#inputNcode").addClass('empty');
    }
    else
    {
        $("#inputNcode").removeClass('empty');
    }
    if ($("#inputMobile").val().length != 0 && !validateMobileNumber($("#inputMobile").val()))
    {
        checks = false;
        errorFields.push('شماره موبایل');
        $("#inputMobile").addClass('empty');
    }
    else
    {
        $("#inputMobile").removeClass('empty');
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
checkDraftSuggestionUserFnc = function () {
    var checks = true;
    var errorFields = [];
    if ($("#inputEconomic").val().length != 0 && (!validateDigit($("#inputEconomic").val()) || $("#inputEconomic").val().length > 15))
    {
        checks = false;
        errorFields.push('میزان صرفه اقتصادی');
        $("#inputEconomic").addClass('empty');
    }
    else
    {
        $("#inputEconomic").removeClass('empty');
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
        $("html, body").animate({
            scrollTop: $(".alert-section.main").offset().top - 20
        }, 1000);
    }
    return checks;
}
checkCreateSuggestionUserFnc = function () {
    var checks = true;
    var errorFields = [];
    if ($("#inputTitle").val().length == 0)
    {
        checks = false;
        errorFields.push('عنوان پیشنهاد');
        $("#inputTitle").addClass('empty');
    }
    else
    {
        $("#inputTitle").removeClass('empty');
    }
    if ($("#inputCommittee").val() == '0')
    {
        checks = false;
        errorFields.push('عنوان کمیته');
        $("#inputCommittee").next(".select2").find(".select2-selection--single").addClass('empty');
    }
    else
    {
        $("#inputCommittee").next(".select2").find(".select2-selection--single").removeClass('empty');
    }
    if ($("#inputSubject").val() == '0')
    {
        checks = false;
        errorFields.push('موضوع پیشنهاد');
        $("#inputSubject").next(".select2").find(".select2-selection--single").addClass('empty');
    }
    else
    {
        $("#inputSubject").next(".select2").find(".select2-selection--single").removeClass('empty');
    }
    if ($("#inputProblems").val().length == 0)
    {
        checks = false;
        errorFields.push('شرح وضعیت فعلی و مشکلات');
        $("#inputProblems").addClass('empty');
    }
    else
    {
        $("#inputProblems").removeClass('empty');
    }
    if ($("#inputDescription").val().length == 0)
    {
        checks = false;
        errorFields.push('شرح پیشنهاد');
        $("#inputDescription").addClass('empty');
    }
    else
    {
        $("#inputDescription").removeClass('empty');
    }
    if ($("#inputBenefit").val().length == 0)
    {
        checks = false;
        errorFields.push('شرح مزایای حاصل از اجرای پیشنهاد');
        $("#inputBenefit").addClass('empty');
    }
    else
    {
        $("#inputBenefit").removeClass('empty');
    }
    if ($("#inputPlane").val().length == 0)
    {
        checks = false;
        errorFields.push('مراحل واقدامات مورد نیاز');
        $("#inputPlane").addClass('empty');
    }
    else
    {
        $("#inputPlane").removeClass('empty');
    }
    if ($("#inputEconomic").val().length != 0 && (!validateDigit($("#inputEconomic").val()) || $("#inputEconomic").val().length > 15))
    {
        checks = false;
        errorFields.push('میزان صرفه اقتصادی');
        $("#inputEconomic").addClass('empty');
    }
    else
    {
        $("#inputEconomic").removeClass('empty');
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
        $("html, body").animate({
            scrollTop: $(".alert-section.main").offset().top - 20
        }, 1000);
    }
    return checks;
}
checkCreateSuggestionGuestFnc = function () {
    var checks = true;
    var errorFields = [];
    if ($("#inputFirstName").val().length == 0)
    {
        checks = false;
        errorFields.push('نام');
        $("#inputFirstName").addClass('empty');
    }
    else
    {
        $("#inputFirstName").removeClass('empty');
    }
    if ($("#inputLastName").val().length == 0)
    {
        checks = false;
        errorFields.push('نام خانوادگی');
        $("#inputLastName").addClass('empty');
    }
    else
    {
        $("#inputLastName").removeClass('empty');
    }
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
    if ($("#inputRole").val().length == 0)
    {
        checks = false;
        errorFields.push('سمت سازمانی');
        $("#inputRole").addClass('empty');
    }
    else
    {
        $("#inputRole").removeClass('empty');
    }
    if ($("#inputOrg").val().length == 0)
    {
        checks = false;
        errorFields.push('سازمان');
        $("#inputOrg").addClass('empty');
    }
    else
    {
        $("#inputOrg").removeClass('empty');
    }
    if (!validateMobileNumber($("#inputMobile").val()))
    {
        checks = false;
        errorFields.push('شماره موبایل');
        $("#inputMobile").addClass('empty');
    }
    else
    {
        $("#inputMobile").removeClass('empty');
    }
    if ($("#inputTitle").val().length == 0)
    {
        checks = false;
        errorFields.push('عنوان پیشنهاد');
        $("#inputTitle").addClass('empty');
    }
    else
    {
        $("#inputTitle").removeClass('empty');
    }
    if ($("#inputCommittee").val() == '0')
    {
        checks = false;
        errorFields.push('عنوان کمیته');
        $("#inputCommittee").next(".select2").find(".select2-selection--single").addClass('empty');
    }
    else
    {
        $("#inputCommittee").next(".select2").find(".select2-selection--single").removeClass('empty');
    }
    if ($("#inputSubject").val() == '0')
    {
        checks = false;
        errorFields.push('موضوع پیشنهاد');
        $("#inputSubject").next(".select2").find(".select2-selection--single").addClass('empty');
    }
    else
    {
        $("#inputSubject").next(".select2").find(".select2-selection--single").removeClass('empty');
    }
    if ($("#inputProblems").val().length == 0)
    {
        checks = false;
        errorFields.push('شرح وضعیت فعلی و مشکلات');
        $("#inputProblems").addClass('empty');
    }
    else
    {
        $("#inputProblems").removeClass('empty');
    }
    if ($("#inputDescription").val().length == 0)
    {
        checks = false;
        errorFields.push('شرح پیشنهاد');
        $("#inputDescription").addClass('empty');
    }
    else
    {
        $("#inputDescription").removeClass('empty');
    }
    if ($("#inputBenefit").val().length == 0)
    {
        checks = false;
        errorFields.push('شرح مزایای حاصل از اجرای پیشنهاد');
        $("#inputBenefit").addClass('empty');
    }
    else
    {
        $("#inputBenefit").removeClass('empty');
    }
    if ($("#inputPlane").val().length == 0)
    {
        checks = false;
        errorFields.push('مراحل واقدامات مورد نیاز');
        $("#inputPlane").addClass('empty');
    }
    else
    {
        $("#inputPlane").removeClass('empty');
    }
    if ($("#inputEconomic").val().length != 0 && (!validateDigit($("#inputEconomic").val()) || $("#inputEconomic").val().length > 15))
    {
        checks = false;
        errorFields.push('میزان صرفه اقتصادی');
        $("#inputEconomic").addClass('empty');
    }
    else
    {
        $("#inputEconomic").removeClass('empty');
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
        $("html, body").animate({
            scrollTop: $(".alert-section.main").offset().top - 20
        }, 1000);
    }
    return checks;
}
checkCreateSuggestionRecommenderFnc = function () {
    var checks = true;
    var errorFields = [];
    var recommenderRows = $(".row-list .added-member");
    var selectedOptions = [];
    var recommenderEmpty = true;
    for (item of recommenderRows)
    {
        if ($(item).find("select.recommender-select").val() != null)
        {
            selectedOptions.push($(item).find("select.recommender-select").val());
        }
        else if ($(".row-list .added-member").length != 1)
        {
            checks = false;
            recommenderEmpty = false;
            errorFields.push(' پیشنهاد دهنده ی اضافه شده نمیتواند خالی باشد. در صورت عدم نیاز به پیشنهاد دهنده سطر مورد نظر را حذف نمائید.');
            $(".row-list .select2-selection--single").addClass('empty');
            break;
        }
    }
    if (recommenderEmpty)
    {
        var uniqueOptions = [...new Set(selectedOptions)];
        if (selectedOptions.length != uniqueOptions.length)
        {
            checks = false;
            errorFields.push(' وارد کردن پیشنهاد دهنده تکراری مجاز نمیباشد.');
            $(".row-list .select2-selection--single").addClass('empty');
        }
        else
        {
            $(".row-list .select2-selection--single").removeClass('empty');
        }
    }
    if (checks)
    {
        $(".alert-message.error-message.error-recommender-fields").hide();
    }
    else
    {
        var errorItems = '';
        $(".alert-recommender-items").html('');
        for (var item of errorFields)
        {
            errorItems += item + '، ';
        }
        var errorText = '';
        if (errorFields.length > 1)
        {
            errorText = '' +
            '<span class="alert-recommender-items">' + errorItems + '</span>'
        }
        else {
            errorItems = errorItems.substr(0, errorItems.length - 2) + ' ';
            errorText = '' +
            '<span class="alert-recommender-items">' + errorItems + '</span>'
        }

        $(".alert-message-text.error-text.error-recommender-fields-text").html(errorText);
        $(".alert-message.error-message.error-recommender-fields").show();
        $("html, body").animate({
            scrollTop: $(".alert-section.recommenders").offset().top - 20
        }, 1000);
    }
    return checks;
}
checkCreateSuggestionPercentFnc = function () {
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
        else if ($(".row-list > .added-member").length > 1)
        {
            var checkPercentEdges = true;
            for (item of percentRows)
            {
                if ($(item).find("input").val() > 70 || 10 > $(item).find("input").val())
                {
                    checks = false;
                    checkPercentEdges = false;
                    $(item).find("input").addClass('empty');
                }
                else
                {
                    $(item).find("input").removeClass('empty');
                }
            }
            if (!checkPercentEdges)
            {
                errorFields.push('درصد مشارکت در پیشنهاد های گروهی بایستی از 10 بیشتر و از 70 کمتر باشد.');
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
        $("html, body").animate({
            scrollTop: $(".alert-section.recommenders").offset().top - 20
        }, 1000);
    }
    return checks;
}
checkReferToExpertExpertsFnc = function () {
    var checks = true;
    var errorFields = [];
    var expertRows = $(".refer-to-expert");
    var selectedOptions = [];
    var expertEmpty = true;
    for (item of expertRows)
    {
        if ($(item).find("select.expert-select").val() != null)
        {
            selectedOptions.push($(item).find("select.expert-select").val());
        }
        else if ($(".refer-to-expert").length != 1)
        {
            checks = false;
            expertEmpty = false;
            errorFields.push('کارشناس اضافه شده نمیتواند خالی باشد. در صورت عدم نیاز به کارشناس سطر مورد نظر را حذف نمائید.');
            $(".refer-to-expert .select2-selection--single").addClass('empty');
            break;
        }
        else
        {
            expertEmpty = false;
        }
    }
    if (expertEmpty)
    {
        var uniqueOptions = [...new Set(selectedOptions)];
        if (selectedOptions.length != uniqueOptions.length)
        {
            checks = false;
            errorFields.push(' وارد کردن کارشناس تکراری مجاز نمیباشد.');
            $(".refer-to-expert .select2-selection--single").addClass('empty');
        }
        else
        {
            $(".refer-to-expert .select2-selection--single").removeClass('empty');
        }
    }
    if (checks)
    {
        $(".alert-message.error-message.error-expert-fields").hide();
    }
    else
    {
        var errorItems = '';
        $(".alert-expert-items").html('');
        for (var item of errorFields)
        {
            errorItems += item + '، ';
        }
        var errorText = '';
        if (errorFields.length > 1)
        {
            errorText = '' +
            '<span class="alert-expert-items">' + errorItems + '</span>'
        }
        else {
            errorItems = errorItems.substr(0, errorItems.length - 2) + ' ';
            errorText = '' +
            '<span class="alert-expert-items">' + errorItems + '</span>'
        }

        $(".alert-message-text.error-text.error-expert-fields-text").html(errorText);
        $(".alert-message.error-message.error-expert-fields").show();
    }
    return checks;
}
checkSecretaryReferToExpertFnc = function () {
    var checks = true;
    var textarea = true;
    var select = true;
    var errorFields = [];
    var referToExpertForms = $(".refer-to-expert-form .refer-to-expert");
    for (item of referToExpertForms)
    {
        if ($(item).find("textarea").val().length == 0)
        {
            checks = false;
            textarea = false;
            $(item).find("textarea").addClass('empty');
        }
        else
        {
            $(item).find("textarea").removeClass('empty');
        }
        if ($(item).find("select").val() == null)
        {
            checks = false;
            select = false;
            $(item).find('.select2-selection--single').addClass('empty');
        }
        else
        {
            $(item).find('.select2-selection--single').removeClass('empty');
        }
    }

    if (!textarea)
    {
        errorFields.push('توضیحات');
    }
    if (!select)
    {
        errorFields.push('کارشناس');
    }

    
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

        $(".alert-message-text.error-text.main-error-text").html(errorText);
        $(".alert-message.error-message.main-error").show();
    }
    return checks;
}
checkSecretaryTransferToCommitteeFnc = function () {
    var checks = true;
    var errorFields = [];
    if ($("#inputCommitteeDescription").val().length == 0)
    {
        checks = false;
        errorFields.push('توضیحات');
        $("#inputCommitteeDescription").addClass('empty');
    }
    else
    {
        $("#inputCommitteeDescription").removeClass('empty');
    }

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

        $(".alert-message-text.error-text.main-error-text").html(errorText);
        $(".alert-message.error-message.main-error").show();
    }
    return checks;
}
checkExpertAnswerFnc = function () {
    var checks = true;
    var errorFields = [];
    if ($("#inputExpertDescription").val().length == 0)
    {
        checks = false;
        errorFields.push('توضیحات');
        $("#inputExpertDescription").addClass('empty');
    }
    else
    {
        $("#inputExpertDescription").removeClass('empty');
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
checkSuggestRejectFnc = function () {
    var checks = true;
    var errorFields = [];
    if ($("#inputCheckResultReason").val() == '0')
    {
        checks = false;
        errorFields.push('دلیل');
        $("#inputCheckResultReason").addClass('empty');
    }
    else
    {
        $("#inputCheckResultReason").removeClass('empty');
    }
    if ($("#inputRejectResultDescription").val().length == 0)
    {
        checks = false;
        errorFields.push('توضیحات');
        $("#inputRejectResultDescription").addClass('empty');
    }
    else
    {
        $("#inputRejectResultDescription").removeClass('empty');
    }
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

        $(".alert-message-text.error-text.main-error-text").html(errorText);
        $(".alert-message.error-message.main-error").show();
    }
    return checks;
}
var sufficiencySolution = false;
var suggestEffect = false;
var matchingJob = false;
var matchingRecall = false;
var singleOrPlural = false;
checkSuggestAcceptFnc = function () {
    var checks = true;
    var errorFields = [];
    // if ($("#inputCheckResultDescription").val().length == 0)
    // {
    //     checks = false;
    //     errorFields.push('توضیحات');
    //     $("#inputCheckResultDescription").addClass('empty');
    // }
    // else
    // {
    //     $("#inputCheckResultDescription").removeClass('empty');
    // }
    if ($("#inputSufficiencySolution").val() == '0')
    {
        checks = false;
        errorFields.push('کفایت راه حل');
        $("#inputSufficiencySolution").addClass('empty');
    }
    else
    {
        sufficiencySolution = true;
        $("#inputSufficiencySolution").removeClass('empty');
    }
    if ($("#inputSuggestEffect").val() == '0')
    {
        checks = false;
        errorFields.push('تاثیر پیشنهاد');
        $("#inputSuggestEffect").addClass('empty');
    }
    else
    {
        suggestEffect = true
        $("#inputSuggestEffect").removeClass('empty');
    }
    if (!validateDigit($("#inputSuggestMatterPoint").val()))
    {
        checks = false;
        errorFields.push('امتیاز (ماهیت پیشنهاد)');
        $("#inputSuggestMatterPoint").addClass('empty');
    }
    else
    {
        $("#inputSuggestMatterPoint").removeClass('empty');
    }
    if ($("#inputMatchingJob").val() == '0')
    {
        checks = false;
        errorFields.push('میزان هم سویی با شغل');
        $("#inputMatchingJob").addClass('empty');
    }
    else
    {
        matchingJob = true;
        $("#inputMatchingJob").removeClass('empty');
    }
    if (!validateDigit($("#inputMatchingJobPoint").val()))
    {
        checks = false;
        errorFields.push('امتیاز (میزان هم سویی با شغل)');
        $("#inputMatchingJobPoint").addClass('empty');
    }
    else
    {
        $("#inputMatchingJobPoint").removeClass('empty');
    }
    if ($("#inputMatchingRecall").val() == '0')
    {
        checks = false;
        errorFields.push('میزان هم سویی با فراخوان');
        $("#inputMatchingRecall").addClass('empty');
    }
    else
    {
        matchingRecall = true;
        $("#inputMatchingRecall").removeClass('empty');
    }
    if (!validateDigit($("#inputMatchingRecallPoint").val()))
    {
        checks = false;
        errorFields.push('امتیاز (میزان هم سویی با فراخوان)');
        $("#inputMatchingRecallPoint").addClass('empty');
    }
    else
    {
        $("#inputMatchingRecallPoint").removeClass('empty');
    }
    if ($("#inputSingleOrPlural").val() == '0')
    {
        checks = false;
        errorFields.push('فردی یا گروهی بودن پیشنهاد');
        $("#inputSingleOrPlural").addClass('empty');
    }
    else
    {
        singleOrPlural = true;
        $("#inputSingleOrPlural").removeClass('empty');
    }
    if (!validateDigit($("#inputSingleOrPluralPoint").val()))
    {
        checks = false;
        errorFields.push('امتیاز (کار گروهی)');
        $("#inputSingleOrPluralPoint").addClass('empty');
    }
    else
    {
        $("#inputSingleOrPluralPoint").removeClass('empty');
    }
    if ($("#inputSpecialSuggestPrice").val().length != 0 && (!validateDigit($("#inputSpecialSuggestPrice").val()) || $("#inputSpecialSuggestPrice").val().length > 15))
    {
        checks = false;
        errorFields.push('صرفه جویی حاصل از پیشنهاد');
        $("#inputSpecialSuggestPrice").addClass('empty');
    }
    else
    {
        $("#inputSpecialSuggestPrice").removeClass('empty');
    }
    if ($("#inputCheckSuggestType").val() == '0')
    {
        checks = false;
        errorFields.push('سنجش نوع پیشنهاد');
        $("#inputCheckSuggestType").addClass('empty');
    }
    else
    {
        $("#inputCheckSuggestType").removeClass('empty');
    }
    if ($("#inputExecutor").val() == null)
    {
        checks = false;
        errorFields.push('مجری');
        $("#inputExecutor").next(".select2").find(".select2-selection--single").addClass('empty');
    }
    else
    {
        $("#inputExecutor").next(".select2").find(".select2-selection--single").removeClass('empty');
    }
    var executionDeadlineJalali = $("#inputExecuteDeadline").val();
    var executionDeadline = JalaliDate.jalaliToGregorian(executionDeadlineJalali.substr(0, 4), executionDeadlineJalali.substr(5, 2), executionDeadlineJalali.substr(8, 2));
    var date1 = new Date(); 
    var date2 = new Date(executionDeadline[1] + "/" + executionDeadline[2] + "/" + executionDeadline[0]); 

    var Difference_In_Time =  date2.getTime() - date1.getTime();

    var Difference_In_Days = Math.round(Difference_In_Time / (1000 * 3600 * 24)).toFixed(0);
    if (!validateDate($("#inputExecuteDeadline").val()) || ($("#inputCheckSuggestType").val() == 'normal' && Difference_In_Days > 90) || (($("#inputCheckSuggestType").val() == 'special' || $("#inputCheckSuggestType").val() == 'qualitatively') && Difference_In_Days > 365))
    {
        checks = false;
        errorFields.push('مهلت اجرا');
        $("#inputExecuteDeadline").addClass('empty');
    }
    else
    {
        $("#inputExecuteDeadline").removeClass('empty');
    }
    if ($("#inputNeededExport").val().length == 0)
    {
        checks = false;
        errorFields.push('خروجی های مورد انتظار');
        $("#inputNeededExport").addClass('empty');
    }
    else
    {
        $("#inputNeededExport").removeClass('empty');
    }
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
        
        $(".alert-message-text.error-text.main-error-text").html(errorText);
        $(".alert-message.error-message.main-error").show();
    }
    return checks;
}

checkSuggestAcceptPointsFnc = function () {
    var checks = true;
    // var errorFields = [];
    var validateEssencePointsMatrix = [[[0, 10], [11, 30], [31, 50]], [[11, 30], [31, 50], [51, 80]], [[31, 50], [51, 80], [81, 120]]];
    var validateMatchingPointsMatrix = [[0, 0], [0, 5], [6, 10]];
    var x;
    var y;
    x = parseInt($("#inputSufficiencySolution").val()) - 1;
    y = parseInt($("#inputSuggestEffect").val()) - 1;
    
    if (sufficiencySolution && suggestEffect && $("#inputSuggestMatterPoint").val().length != 0 && (parseInt($("#inputSuggestMatterPoint").val()) < validateEssencePointsMatrix[x][y][0] || parseInt($("#inputSuggestMatterPoint").val()) > validateEssencePointsMatrix[x][y][1]))
    {
        checks = false;
        // errorFields.push('امتیازهای وارد شده در بازه مجاز نمیباشند');
        $("#inputSuggestMatterPoint").addClass('empty');
    }
    else
    {
        // $("#inputSuggestMatterPoint").removeClass('empty');
    }
    x = parseInt($("#inputMatchingJob").val()) - 1;
    if (matchingJob && $("#inputMatchingJobPoint").val().length != 0 && (parseInt($("#inputMatchingJobPoint").val()) < validateMatchingPointsMatrix[x][0] || parseInt($("#inputMatchingJobPoint").val()) > validateMatchingPointsMatrix[x][1]))
    {
        checks = false;
        // errorFields.push('امتیازهای وارد شده در بازه مجاز نمیباشند');
        $("#inputMatchingJobPoint").addClass('empty');
    }
    else
    {
        // $("#inputMatchingJobPoint").removeClass('empty');
    }
    x = parseInt($("#inputMatchingRecall").val()) - 1;
    if (matchingRecall && $("#inputMatchingRecallPoint").val().length != 0 && (parseInt($("#inputMatchingRecallPoint").val()) < validateMatchingPointsMatrix[x][0] || parseInt($("#inputMatchingRecallPoint").val()) > validateMatchingPointsMatrix[x][1]))
    {
        checks = false;
        // errorFields.push('امتیازهای وارد شده در بازه مجاز نمیباشند');
        $("#inputMatchingRecallPoint").addClass('empty');
    }
    else
    {
        // $("#inputMatchingRecallPoint").removeClass('empty');
    }
    x = parseInt($("#inputSingleOrPlural").val()) - 1;
    if (singleOrPlural && $("#inputSingleOrPluralPoint").val().length != 0 && (parseInt($("#inputSingleOrPluralPoint").val()) < validateMatchingPointsMatrix[x][0] || parseInt($("#inputSingleOrPluralPoint").val()) > validateMatchingPointsMatrix[x][1]))
    {
        checks = false;
        // errorFields.push('امتیازهای وارد شده در بازه مجاز نمیباشند');
        $("#inputSingleOrPluralPoint").addClass('empty');
    }
    else
    {
        // $("#inputSingleOrPluralPoint").removeClass('empty');
    }
    
    if (checks)
    {
        $(".alert-message.error-message.error-points-fields").hide();
    }
    else
    {
        // var errorItems = '';
        // $(".alert-recommender-items").html('');
        // for (var item of errorFields)
        // {
        //     errorItems += item + '، ';
        // }
        // var errorText = '';
        // if (errorFields.length > 1)
        // {
        //     errorText = '' +
        //     '<span class="alert-recommender-items">' + errorItems + '</span>'
        // }
        // else {
        //     errorItems = errorItems.substr(0, errorItems.length - 2) + ' ';
        //     errorText = '' +
        //     '<span class="alert-recommender-items">' + errorItems + '</span>'
        // }
        var errorText = 'امتیاز های وارد شده در بازه مجاز نمیباشند.'
        $(".alert-message-text.error-text.error-points-fields-text").html(errorText);
        $(".alert-message.error-message.error-points-fields").show();
        $("html, body").animate({
            scrollTop: $(".alert-section").offset().top - 20
        }, 1000);
    }
    return checks;
}

checkSecretaryEditSuggesitonFnc = function () {
    var checks = true;
    var errorFields = [];
    if ($("#inputProblems").val().length == 0)
    {
        checks = false;
        errorFields.push('شرح وضعیت فعلی و مشکلات');
        $("#inputProblems").addClass('empty');
    }
    else
    {
        $("#inputProblems").removeClass('empty');
    }
    if ($("#inputDescription").val().length == 0)
    {
        checks = false;
        errorFields.push('شرح پیشنهاد');
        $("#inputDescription").addClass('empty');
    }
    else
    {
        $("#inputDescription").removeClass('empty');
    }
    if ($("#inputBenefit").val().length == 0)
    {
        checks = false;
        errorFields.push('شرح مزایای حاصل از اجرای پیشنهاد');
        $("#inputBenefit").addClass('empty');
    }
    else
    {
        $("#inputBenefit").removeClass('empty');
    }
    if ($("#inputPlane").val().length == 0)
    {
        checks = false;
        errorFields.push('مراحل واقدامات مورد نیاز');
        $("#inputPlane").addClass('empty');
    }
    else
    {
        $("#inputPlane").removeClass('empty');
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