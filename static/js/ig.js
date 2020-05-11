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

})(jQuery);

