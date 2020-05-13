(function ($) {
    var num = 0;
    $('.button').on('click', function(){
        $(this).data("click", ++num);
        var click =  $(this).data('id');
        var id =  $(this).attr('id');
        if (num == 1) {
            $('#selected1').text(click);
            $('input[name="test1"]').val(id);
        }else if (num == 2) {
            $('#selected2').text(click);
            $('input[name="test2"]').val(id);
        }else if (num == 3) {
            $('#selected3').text(click);
            $('input[name="test3"]').val(id);
        }else if (num > 3) {
            $('#choice').text('もう選択できません');
        }

    });
    $('#clear').on('click', function(){
        num = 0;
        $('#selected1').text('選択してください');
        $('#selected2').text('選択してください');
        $('#selected3').text('選択してください');
        $('#choice').text('三つ選択してください');
    });
    $('.submit').on('click', function(){
        num = 0;
    });
    
    // $('.dropdown').hover(
    //     function() {
    //         //カーソルが重なった時
    //         $(this).find('.small_category').removeClass('close');
    //     }, function() {
    //         //カーソルが離れた時
    //         $(this).find('.small_category').addClass('close');
    //     }
    // );
                

    // post_form.html
    var arg  = new Object;
    url = location.search.substring(1).split('&');
    
   for(i=0; url[i]; i++) {
       var k = url[i].split('=');
       arg[k[0]] = k[1];
   }
    


   var Categories_ja = {'tech': 'テクノロジー', 'agri': '農業', 'feeling': '五感', 'web': 'Web', 'AI': 'AI', 'religion': '宗教' }

   var category1 = arg.test1;
   var category2 = arg.test2;
   var category3 = arg.test3;

   for (var i=0; i<4; i++) {
       for (var key in Categories_ja) {
           if (category1 == key) {
               category1 = Categories_ja[key];
           }
           else if (category2 == key) {
               category2 = Categories_ja[key];
           }
           else if (category3 == key) {
               category3 = Categories_ja[key];
           }
       }
  }
   




    $('.idea_generated').on('click', function(){
        $('#category1').find('.current').text(category1);
        $('#category2').find('.current').text(category2);
        $('#category3').find('.current').text(category3);
    });
    $('.idea_generated').on('click', function(){
        var tag1 = $(this).find('.idea1').text();
        var tag2 = $(this).find('.idea2').text();
        var tag3 = $(this).find('.idea3').text();
        $('#tag1').find('.current').text(tag1);
        $('#tag2').find('.current').text(tag2);
        $('#tag3').find('.current').text(tag3);
    });
})(jQuery);

