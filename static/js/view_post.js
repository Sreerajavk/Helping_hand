

$(document).ready(function () {

    get_data();

});



function get_data() {

        $.ajax({
        url : '/view_post/' ,
        type : 'post' ,
        dataType: 'json',

        success : function (response) {


                //alert(response.data)

                $('#google_loader').css('opacity' ,  '0');
                var i;

                for (i=0; i<response.data.length ; i++){

                    var main_div = $('#main_div');

                    var div = $('<div class="container-div"></div>');
                    //div.css('id' , 'Question' + (i+1));

                    var title_div = $('<div  style="font-size: 20px;"></div>');
                    var title = $('<span></span>')
                    title.html(response.data[i].title)
                    title_div.append(title)
                    div.append(title_div)

                    var body_div = $('<div></div>');
                    body_div.html(response.data[i].body)
                    div.append(body_div)


                    var read_more = $('<div>\n' +
                        '                <a class="btn btn-primary" href="#">\n' +
                        '                  Read More\n' +
                        '                </a>\n' +
                        '              </div>');

                    div.append(read_more)

                    main_div.append(div)




                }

                 $('#submit_button').css('opacity' , '1');

                var deadline = new Date(Date.parse(new Date()) +  30 * 60 *   1000);
                initializeClock('clockdiv', deadline);

                //var submit = $('<button type="submit" class="btn btn-success btn-lg" id="submit_button" style="margin-bottom: 2em;">Submit</button>');

                //main_div.append(submit);

        } ,

        fail : function () {


            alert("eeee");

        } ,

    });



}