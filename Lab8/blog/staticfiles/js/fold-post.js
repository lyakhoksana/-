document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('.fold-button').forEach(function(btn) {
        btn.addEventListener('click', function(e) {
            var post = e.target.closest('.one-post');
            var isFolded = post.classList.toggle('folded');
            e.target.innerHTML = isFolded ? 'развернуть' : 'свернуть';
        });
    });
});