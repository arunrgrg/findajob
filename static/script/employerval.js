$(document).ready(function() {
    var jq = $.noConflict();
    jq("#employer_reg").validate({
        rules: {
            er_firstname: {
                required: true,
                minlength: 4,
                maxlength: 10
            },
            er_email: {
                required: true,
                email: true
            },
            er_password: {
                required: true,
                minlength: 8
            },
            er_conpassword: {
                required: true,
                minlength: 8,
                equalTo: "#er_password"
            },
            er_mobile: {
                required: true,
                number: true,
                minlength: 10
            },
        },
        messages: {
            er_firstname: {
                required: "Enter your firstname"
            },
            er_email: {
                required: "Enter your email"
            },
            er_password: {
                required: "Enter your password"
            },
            er_conpassword: {
                required: "Re Enter your password"
            },
            er_mobile: {
                required: "Enter your mobile number"
            }
        }
    })
})