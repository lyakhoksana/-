// 📁 articles/static/js/parallax.js
// Эффект параллакса для иконок + логотипа

$(document).ready(function() {

    // === Инициализация переменных ===
    var scrolled = 0;
    var yPosition;

    // Элементы для параллакса: иконки + логотип
    var $parallaxIcons = $('.icons-for-parallax img');
    var $parallaxLogo = $('#main-logo');

    // Сохраняем исходную позицию логотипа
    var logoOriginalTop = $parallaxLogo.position().top;

    // === Обработчик прокрутки ===
    $(window).scroll(function() {
        // Обновляем значение прокрутки
        scrolled = $(window).scrollTop();


        for (var i = 0; i < $parallaxIcons.length; i++) {
            // Скорость зависит от позиции: чем дальше, тем медленнее
            var speed = parseFloat($parallaxIcons.eq(i).data('speed')) || (0.15 * (i + 1));
            yPosition = scrolled * speed;
            $parallaxIcons.eq(i).css({ top: yPosition + 'px' });
        }

        // Логотип движется очень медленно (0.03) — создаёт эффект глубины
        var logoYPosition = logoOriginalTop + (scrolled * 0.03);
        $parallaxLogo.css({ top: logoYPosition + 'px' });
    });


    console.log('parallax.js загружен!');
    console.log('Иконок для параллакса: ' + $parallaxIcons.length);
    console.log('Логотип для параллакса: ' + ($parallaxLogo.length > 0));
});