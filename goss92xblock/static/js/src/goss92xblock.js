/* Javascript for goss8XBlock. */
function Goss92XBlock(runtime, element) {

    function updateScore(result) {
        $('.score', element).text(result.score);
    }

    var handlerUrl = runtime.handlerUrl(element, 'set_score2');

    $('#gosssend').click(buttonClick);


    $(function ($) {
        console.log('*x92d***********');
        /* Here's where you'd do things on page load. */
    });
}
