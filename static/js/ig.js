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
    


   var Categories_ja = {'tech': 'テクノロジー', 'agri': '農業', 'web': 'Web', 'AI': 'AI', 'religion': '宗教', 'feeling': '五感' };
   

   var category1_get = arg.test1;
   var category2_get = arg.test2;
   var category3_get = arg.test3;
   var category1 = null;
   var category2 = null;
   var category3 = null;

   for (var i=0; i<4; i++) {
        for (var key in Categories_ja) {
            if (category1_get == key && category1 == null) {
                category1 = Categories_ja[key];
            }
            else if (category2_get == key && category2 == null) {
                category2 = Categories_ja[key];
            }
            else if (category3_get == key && category3 == null) {
                category3 = Categories_ja[key];
            }
        }
    }

    $('.idea_generated').on('click', function(){

        // for (var i=0; i<4; i++) {
        //     if (category1 == null) {
        //         category1 = $(this).find('.category_ja1').text();
        //     }
        //     else if (category2 == null) {
        //         category2 = $(this).find('.category_ja2').text();
        //     }
        //     else if (category3 == null) {
        //         category3 = $(this).find('.category_ja3').text();
        //     }

        // }

        var  categories = $('#id_category').children();
        console.log(categories);

        for (var i=0; i<categories.length; i++) {
            if (category1 == categories.eq(i).text()){
                categories.eq(i).attr('selected', 'selected');
            }
            else if (category2 == categories.eq(i).text()){
                categories.eq(i).attr('selected', 'selected');
            }
            else if (category3 == categories.eq(i).text()){
                categories.eq(i).attr('selected', 'selected');
            }
        }
        $('#category1').find('.current').text(category1);
        $('#category2').find('.current').text(category2);
        $('#category3').find('.current').text(category3);
    });
        
    $('.idea_generated').on('click', function(){
        var tag1 = $(this).find('.idea1').text();
        var tag2 = $(this).find('.idea2').text();
        var tag3 = $(this).find('.idea3').text();

        var  tags = $('#id_tags').children();
        for (var i=0; i<tags.length; i++) {
            if (tag1 == tags.eq(i).text()){
                tags.eq(i).attr('selected', 'selected');
            }
            else if (tag2 == tags.eq(i).text()){
                tags.eq(i).attr('selected', 'selected');
            }
            else if (tag3 == tags.eq(i).text()){
                tags.eq(i).attr('selected', 'selected');
            }
        }
        $('#tag1').find('.current').text(tag1);
        $('#tag2').find('.current').text(tag2);
        $('#tag3').find('.current').text(tag3);
    });
})(jQuery);

