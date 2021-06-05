function validateEmail(email) {
    const reg = /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return reg.test(email);
}

function validateIranianNationalCode(nationalcode) {
    if (!/^\d{10}$/.test(nationalcode))
        return false;

    var reg = /([0-9])\1{9}/
    if (reg.test(nationalcode))
        return false;
 
    const check = +nationalcode[9];
    const sum = Array(9).fill().map((_, i) => +nationalcode[i] * (10 - i)).reduce((x, y) => x + y) % 11;
    return (sum < 2 && check == sum) || (sum >= 2 && check + sum == 11);
}

function validateUsername(username) {
    var reg = /^[-_.a-z\d]+$/;
    return reg.test(username);
}

function validatePassword(password) {
    var reg = /^[A-Za-z0-9@#$%^&+=!()\-\_\.\*\\\/\[\]\{\}?,~`]{8,}$/;
    return reg.test(password);
}

function validateRepeatPassword(password, repeatpassword) {
    if (password == repeatpassword)
    {
        return true;
    }
    else
    {
        return false;
    }
}

function validateMobileNumber (mobilenumber) {
    var reg = /^09\d{9}$/
    return reg.test(mobilenumber);
}

function validatePhoneNumber (phonenumber) {
    var reg = /^0\d{10}$/
    // var reg = /^\d{8}$/
    return reg.test(phonenumber);
}

function validateDate (date) {
    var reg = /^\d{4}\/\d{2}\/\d{2}$/
    return reg.test(date)
}

function validateTime (time) {
    var reg = /^([0-1][0-9]|[2][0-3]):([0-5][0-9])$/
    return reg.test(time)
}

function validateYear (year) {
    var reg = /^1\d{3}$/
    return reg.test(year)
}

function validateDigit (digit) {
    var reg = /^\d+$/
    return reg.test(digit)
}

function validateFloat (float) {
    var reg = /^\d+(.\d+)*$/
    return reg.test(float)
}

function validateZeroToOne (zeroToOne) {
    var reg = /^(0(\.\d+)?|1(\.0+)?)$/
    return reg.test(zeroToOne)
}
const fileTypes = [
    "image/apng",
    "image/bmp",
    "image/gif",
    "image/jpeg",
    "image/pjpeg",
    "image/png",
    "image/svg+xml",
    "image/tiff",
    "image/webp",
    "image/x-icon"
];

function validImageFileType(file) {
    return fileTypes.includes(file.type);
}

function validateDeltaTime(startDate, EndDate) {
    var startDateDateType = new Date(startDate);
    var endDateDateType = new Date(EndDate);
    return startDateDateType.getTime() <= endDateDateType.getTime()
}