/* Javascript for goss8XBlock. */
function Goss92XBlock(runtime, element) {

    function updateScore(result) {
        $('.score', element).text(result.score);
    }

    var handlerUrl = runtime.handlerUrl(element, 'set_score2');

    $('#gosssend').click(function(e) {
        const { value } = element.querySelector('#gossinput');
        if (value.length > 0) {
           fetch(value)
           .then(x => x.json())
           .then(x => {
           	 const { textContent: curr } = element.querySelector('#gosscurrent');
           	 const res = x.message;
           	 if (res == curr) {
                       element.querySelector('#gosssend').insertAdjacentHTML('afterend', '<h1 id="gosscorrect">Correct!</h1>')
                       $.ajax({
                      	 	           type: "POST",
                      	 	           url: handlerUrl,
                      	 	           data: JSON.stringify({"key": "hundred"}),
                      	 	           success: updateScore
                       });      	 	
           	 } else {
           	    //	element.style.background = 'red';
           	 	      alert('Oh NO!');
                      $.ajax({
                                      type: "POST",
                                      url: handlerUrl,
                                      data: JSON.stringify({"key": "zero"}),
                                      success: updateScore
                      });
           	 	
           	 }
           	 
           })
           .catch(x => alert('Error: ' + x))
        	
        }
    });


    $(function ($) {
        console.log('*92***********');
        console.log(element);
        /* Here's where you'd do things on page load. */
    });
}
