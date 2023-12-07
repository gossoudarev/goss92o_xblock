/* Javascript for goss8XBlock. */
function Goss92XBlock(runtime, element, context) {

    window.updateScore = function (result) {
        $('.score', element).text(result.score);
        localStorage['score'] = result.score;
        localStorage['score_' + Math.random()] = result.score;
        localUpdate(result.score);
    }

    window.handlerUrl = runtime.handlerUrl(element, 'set_score2');

    init_goss(context); // important! here we initiate the week number check

    $('#gosssend').click(buttonClick);

    $(function ($) {
        console.log('*x92***********');
        /* Here's where you'd do things on page load. */
    });
}

