let elementsInFAQ = document.querySelectorAll(".faq-element");


if(elementsInFAQ) {
    elementsInFAQ.forEach(function(el) {
        el.querySelector('.faq-question').onclick = function() {
            let answerInFAQ = el.querySelector('.faq-answer');
            let answerStyle = answerInFAQ.getAttribute('style');
            let crossInFAQ = el.querySelector('.faq-cross');
            if(answerStyle === 'max-height: 0px') {
                let answerP = answerInFAQ.querySelector('p')
                let answerHeight = answerP.offsetHeight;
                let answerHeightStyle = 'max-height: ' + answerHeight + 'px';
                answerInFAQ.setAttribute('style', answerHeightStyle);
                // crossInFAQ.setAttribute('style', 'transform: rotate(-135deg)')
                crossInFAQ.setAttribute('style', 'transform: rotate(-45deg)')
            }
            else {
                answerInFAQ.setAttribute('style', 'max-height: 0px');
                crossInFAQ.setAttribute('style', 'transform: rotate(0deg)')
            }
        }
    });
}











