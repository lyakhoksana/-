
$(document).ready(function() {


    $('.one-post').hover(
        function(e) {
            $(e.currentTarget).find('.one-post-shadow')
                .stop()
                .animate({ opacity: 0.15 }, 200);
        },
        function(e) {
            $(e.currentTarget).find('.one-post-shadow')
                .stop()
                .animate({ opacity: 0 }, 200);
        }
    );


    $('#main-logo').hover(

        function() {
            var $logo = $(this);
            // Сохраняем исходную ширину при первом наведении
            if (!$logo.data('original-width')) {
                $logo.data('original-width', $logo.width());
            }
            // Увеличиваем ширину на 20px (высота подстроится автоматически)
            $logo.stop().animate({ width: '+600px' }, 300);
        },

        function() {
            var $logo = $(this);
            $logo.stop().animate({
                width: $logo.data('original-width') + 'px'
            }, 300);
        }
    );

    console.log(' highlight-post.js: логотип увеличивается при наведении!');
});