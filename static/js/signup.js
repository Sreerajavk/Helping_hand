    // $("#username").keyup(function () {
    //
    //
    //
    //     // alert('sdfsdf');
    //   var username = $('#username').val();
    //   //alert(username);
    //   //$('#loader_img3').css('opacity' , '1');
    //   $('#username_spin').removeClass('fas');
    //   $('#username_spin').addClass('fa fa-spinner fa-pulse fa-fw fa-2x');
    //   $('#username_spin').css({'opacity':'1' } );
    //   $('#username_spin').css({'color':'#000' });
    //
    //   //$('#username').setCustomValidity("");
    //   //$('#email_spin').css({'opacity':'1'  , 'width':'15px' , 'color': '#fff','position':'absolute','top':'60px','right':'10px'});
    //   $.ajax({
    //     url: '/login/validate_username/',
    //     data: {
    //       'username': username
    //     },
    //     dataType: 'json',
    //     success: function (data) {
    //         var element = $('#username').get(0)
    //       $('#username_spin').removeClass('fa fa-spinner fa-pulse');
    //
    //
    //       if(data.status=='400'){
    //       $('#label_username').html('Username exits or Invalid ');
    //       $('#label_username').css('color', '#f00');
    //       $('#username_spin').removeClass('fa fa-check');
    //       $('#username_spin').addClass('fa fa-exclamation-triangle');
    //
    //       $('#username_spin').css({'color':'#f00' });
    //       element.setCustomValidity("Username is Invalid");
    //
    //       }
    //
    //       else{
    //         $('#username_spin').removeClass('fa fa-exclamation-triangle');
    //         $('#username_spin').addClass('fa fa-check ');
    //       $('#label_username').html('Valid Username');
    //       $('#label_username').css('color','#000');
    //       $('#username_spin').css({'color':'#0f0' } );
    //        element.setCustomValidity('');}
    //
    //       /*
    //       if(data.length == 'none'){
    //          $('#label_username').html('Enter your username');
    //          $('#label_username').css('color','#fff');
    //         $('#username_spin').removeClass('fas fa-exclamation-triangle fa-check' );
    //       }
    //        */
    //
    //       //$('#loader_img3').css('opacity' , '0');
    //
    //     },
    //     error: function(date){
    //       $('#loader_img3').css('opacity' , '0');
    //         alert('something went wrong');
    //     }
    //
    //   });
    //
    // });



$('#signup_form').on('submit',function(event){


    //alert("sdfsdf");

    event.preventDefault();
    //loader begin spigging
    $('#loader_img1').css('opacity' , '1');
    //$('#warning_txt').css('opacity' , '0');


    var last_name = $('#last_name').val();
    // alert(last_name);
    var mobile = $('#mobile').val();
    var email = $('#email').val();
    var first_name = $('#first_name').val();
    var username = $('#username').val();
    var password = $('#pass').val();
    var re_password = $('#repeat-pass').val();


    if (password !=re_password){
        alert("paaword does not match")
    }

    else{
        $.post('/signup/',{

        username:username,
        password:password,
        first_name : first_name ,
        last_name : last_name ,
        username : username ,
        first_name : first_name ,
        email : email ,
        mobile : mobile,


    })
    .done(function(response){
        // request successfull
        $('#loader_img1').css('opacity' , '0');
        if ( response.status == '200'){
            // redirect to home page
            //print('sdfjhsfi')
            window.location = "/home";
        }

        else if( response.status == '400'){
            alert("Incorrect Password");
            $('#loader_img1').css('opacity' , '0');
        // show_warning(response.text);
        }

        else{
            alert("Already completed exam");
        }




    })
    .fail(function(response){
        // request failed
        $('#loader_img').css('opacity' , '0');
        // show_warning('Something went wrong')
        $('#loader_img1').css('opacity' , '0');

    });
    }




});



$('#signup_inst_form').on('submit',function(event){


    //alert("sdfsdf");

    event.preventDefault();
    //loader begin spigging
    $('#loader_img1').css('opacity' , '1');
    //$('#warning_txt').css('opacity' , '0');


    var last_name = $('#last_name').val();
    // alert(last_name);
    var mobile = $('#mobile').val();
    var email = $('#email').val();
    var first_name = $('#first_name').val();
    var username = $('#username').val();
    var password = $('#pass').val();
    var re_password = $('#repeat-pass').val();
    var account_name = $('#account_name').val();
    var account_number = $('#account_number').val();
    var ifsc = $('#ifsc').val();



    if (password !=re_password){
        alert("paaword does not match")
    }

    else{
        $.post('/signup_inst/',{

        username:username,
        password:password,
        first_name : first_name ,
        last_name : last_name ,
        username : username ,
        first_name : first_name ,
        email : email ,
        mobile : mobile,
        account_name : account_name  ,
        account_number : account_number ,
        ifsc: ifsc


    })
    .done(function(response){
        // request successfull
        $('#loader_img1').css('opacity' , '0');
        if ( response.status == '200'){
            // redirect to home page
            //print('sdfjhsfi')
            window.location = "/home";
        }

        else if( response.status == '400'){
            alert("Incorrect Password");
            $('#loader_img1').css('opacity' , '0');
        // show_warning(response.text);
        }

        else{
            alert("Already completed exam");
        }




    })
    .fail(function(response){
        // request failed
        $('#loader_img').css('opacity' , '0');
        // show_warning('Something went wrong')
        $('#loader_img1').css('opacity' , '0');

    });
    }




});


$('#login_form').on('submit',function(event){


    //alert("sdfsdf");

    event.preventDefault();
    //loader begin spigging
    $('#loader_img1').css('opacity' , '1');
    //$('#warning_txt').css('opacity' , '0');


    var username = $('#username').val();
    var password = $('#pass').val();




        $.post('/login/',{

        username:username,
        password:password,



    })
    .done(function(response){
        // request successfull
        $('#loader_img1').css('opacity' , '0');
        if ( response.status == '200'){
            // redirect to home page
            //print('sdfjhsfi')
            window.location = "/home";
        }

        else if( response.status == '400'){
            alert("Incorrect Password");
            $('#loader_img1').css('opacity' , '0');
        // show_warning(response.text);
        }

        else if( response.status == '300'){
            alert("verify your email");
            $('#loader_img1').css('opacity' , '0');
        // show_warning(response.text);
        }

        else{
            alert("Already completed exam");
        }




    })
    .fail(function(response){
        // request failed
        $('#loader_img').css('opacity' , '0');
        // show_warning('Something went wrong')
        $('#loader_img1').css('opacity' , '0');

    });




});




$('#issue_form').on('submit',function(event){


    // alert("sdfsdf");

    event.preventDefault();
    //loader begin spigging
    $('#loader_img1').css('opacity' , '1');
    //$('#warning_txt').css('opacity' , '0');


    var title = $('#title').val();
    var body = $('#body').val();

    // alert(title);




        $.post('/add_post/',{

        title:title,
        body:body,



    })
    .done(function(response){
        // request successfull
        $('#loader_img1').css('opacity' , '0');
        if ( response.status == '200'){
            // redirect to home page
            //print('sdfjhsfi')
            window.location = "/home";
        }

        else if( response.status == '400'){
            alert("Incorrect Password");
            $('#loader_img1').css('opacity' , '0');
        // show_warning(response.text);
        }

        else if( response.status == '300'){
            alert("verify your email");
            $('#loader_img1').css('opacity' , '0');
        // show_warning(response.text);
        }

        else{
            alert("Already completed exam");
        }




    })
    .fail(function(response){
        // request failed
        $('#loader_img').css('opacity' , '0');
        // show_warning('Something went wrong')
        $('#loader_img1').css('opacity' , '0');

    });




});