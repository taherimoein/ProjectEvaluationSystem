$(document).ready(function () {
    $('.dropdown-submenu a.test').on("click", function (e) {
        $(this).next('ul').toggle();
        e.stopPropagation();
        e.preventDefault();
    });
});

$(document).on('click', '.close-message', function () {
    $(this).parents('div.alert-message').fadeOut();
});

$(document).ready(function () {
    $('.select2-component').select2({
        dir: "rtl",
        width: "100%"
    });

    $(".select2-static-component").select2({
        dir: "rtl",
        width: "100%",
        minimumResultsForSearch: -1
    })
});

$(".menu-item-subset").hide();

$(".menu-item-title").click(function () {
    $(".menu-item-subset").not($(this).parent().children(".menu-item-subset")).slideUp();
    $(".menu-item-title").not($(this)).children('.collapse-part').children('i').removeClass('open');
    $(this).children('.collapse-part').children('i').toggleClass('open');
    $(this).parent().children(".menu-item-subset").slideToggle();
})

$(".menu-item-subset-sub-menu").hide();

$(".menu-item-subset-title").click(function () {
    $(".menu-item-subset-sub-menu").not($(this).parent().children(".menu-item-subset-sub-menu")).slideUp();
    $(".menu-item-subset-title").not($(this)).children('.indent-part').children('i').removeClass('open');
    $(this).children('.sub-item-part.indent-part').children('i').toggleClass('open');
    $(this).parent().children(".menu-item-subset-sub-menu").slideToggle();
})

// function delay(callback, ms) {
//   var timer = 0;
//   return function() {
//     var context = this, args = arguments;
//     clearTimeout(timer);
//     timer = setTimeout(function () {
//       callback.apply(context, args);
//     }, ms || 0);
//   };
// }

$('[data-toggle="tooltip"]').tooltip();

//Show Image After Select
function readURL(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function (e) {
            $(input).prev('.temp-image').first()
                .attr('src', e.target.result);
        };

        reader.readAsDataURL(input.files[0]);
    }
}

$(".datatable").DataTable({
    'order': []
});