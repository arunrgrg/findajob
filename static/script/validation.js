$(document).ready(function() {
    $("#employ-reg").validate({
        rules: {
            firstname: {
                required: true,
                minlength: 4,
                maxlength: 10
            },
            email: {
                required: true,
                email: true
            },
            password: {
                required: true,
                minlength: 8
            },
            con_password: {
                required: true,
                minlength: 8,
                equalTo: "#password"
            },
            mobilenum: {
                required: true,
                number: true,
                minlength: 10
            },
            state: {
                required: true,
            }
        },
        messages: {
            firstname: {
                required: "Enter your firstname"
            },
            email: {
                required: "Enter your email"
            },
            password: {
                required: "Enter your password"
            },
            con_password: {
                required: "Re Enter your password"
            },
            mobilenum: {
                required: "Enter your mobile number"
            }
        }
    })
})












// $(document).ready(function() {
//     var jq = $.noConflict();
//     jq("#post-job").validate({

//         rules: {
//             jobtitle: {
//                 required: true,
//                 minlength: 4,
//                 maxlength: 10
//             },
//             com_name: {
//                 required: true,

//             },
//             p_location: {
//                 required: true,

//             },
//             categories: {
//                 required: true,


//             },
//             Description: {
//                 required: true,

//                 minlength: 10
//             },
//             experience: {
//                 required: true,
//             },
//             Salary: {
//                 required: true,
//             },
//             qualification: {
//                 required: true,
//             }
//         },
//         messages: {
//             jobtitle: {
//                 required: "Enter your job title"
//             },
//             com_name: {
//                 required: "Enter your company name"
//             },
//             p_location: {
//                 required: "select your location"
//             },
//             categories: {
//                 required: "select your categories"
//             },

//         }
//     })
// })