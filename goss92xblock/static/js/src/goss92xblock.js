/* Javascript for goss8XBlock. */
function Goss92XBlock(runtime, element) {

    window.updateScore = function (result) {
        $('.score', element).text(result.score);
    }

    window.handlerUrl = runtime.handlerUrl(element, 'set_score2');

    $('#gosssend').click(buttonClick);


    $(function ($) {
        console.log('*x92j***********');
        /* Here's where you'd do things on page load. */
    });
}
