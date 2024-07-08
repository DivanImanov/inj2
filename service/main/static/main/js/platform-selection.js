// let currentPlatform = 'xbox'
let buttonIcons = document.querySelectorAll('.move-input img')


function SelectPlatform(value) {
    localStorage.setItem('selectedtem', document.querySelector('.platform-list select').value)
    buttonIcons.forEach(function(buttonIcon) {
        let pathToButtonIcon = buttonIcon.src
        let newPathToButtonIcon = pathToButtonIcon.split('/')
        newPathToButtonIcon[7] = value
        newPathToButtonIcon = newPathToButtonIcon.join('/')
        buttonIcon.setAttribute('src', newPathToButtonIcon)
        // localStorage.setItem('selectedtem', document.querySelector('.platform-list select').value)
    })
}


// Break the script above for some reason

// document.querySelector('.platform-list select').onchange = function() {
//     localStorage.setItem('selectedtem', document.querySelector('.platform-list select').value);
// };

if (localStorage.getItem('selectedtem')) {
    document.getElementById(localStorage.getItem('selectedtem')).selected = true;
    SelectPlatform(localStorage.getItem('selectedtem'))
} else {
    SelectPlatform('xbox')
}
